SHELL := /bin/bash

HOSTNAME1 = hostname1
IPADDRESS1 = ipaddress1

HOSTNAME2 = hostname2
IPADDRESS2 = ipaddress2

TRUSTEDIP = 1.2.3.4

SELECTOR = default
MAIL_DOMAIN = example.com

ifeq "$(HOSTNAME1)" ""
    override HOSTNAME1 := $(shell read -p "Enter HOSTNAME1: " pwd;echo $$pwd;)
endif

ifeq "$(IPADDRESS1)" ""
    override IPADDRESS1 := $(shell read -p "Enter IPADDRESS1: " pwd;echo $$pwd)
endif

ifeq "$(HOSTNAME2)" ""
    override HOSTNAME2 := $(shell read -p "Enter HOSTNAME2: " pwd;echo $$pwd)
endif

ifeq "$(IPADDRESS2)" ""
    override IPADDRESS2 := $(shell read -p "Enter IPADDRESS2: " pwd;echo $$pwd)
endif

ifeq "$(SELECTOR)" ""
    override SELECTOR := $(shell read -p "Enter SELECTOR: " pwd;echo $$pwd)
endif

ifeq "$(MAIL_DOMAIN)" ""
    override MAIL_DOMAIN := $(shell read -p "Enter MAIL_DOMAIN: " pwd;echo $$pwd)
endif

ifeq "$(TRUSTEDIP)" ""
    override TRUSTEDIP := $(shell read -p "Enter TRUSTEDIP: " pwd;echo $$pwd)
endif

help:
	@echo "#########################################################################################"
	@echo "Make help		show this help message"
	@echo "Make single 		config single Postfix instance, used for VPS with single IP Address"
	@echo "Make dual 		config dual Postfix instance, used for VPS with dual IP Addresses"
	@echo "Make dkim		config OpenDKIM, this will generate new key for OpenDKIM"
	@echo "Make dkim_rm		config OpenDKIM, this will use the exist key signed by ringiermail"
	@echo "Make dkim_tc		config OpenDKIM, this will use the exist key signed by tipcontact"
	@echo "Make start		start OpenDKIM and reload Postfix"
	@echo "#########################################################################################"

single:
	@make HOSTNAME1= IPADDRESS1= do_single

dual:
	@make HOSTNAME1= IPADDRESS1= HOSTNAME2= IPADDRESS2= do_dual

dkim:
	@make SELECTOR= MAIL_DOMAIN= TRUSTEDIP= do_dkim

dkim_rm:
	@make SELECTOR=ya00102_rm MAIL_DOMAIN=ringiermail.com TRUSTEDIP=69.41.161.49 do_dkim_with_rm_key

dkim_tc:
	@make SELECTOR=ya00101_tc MAIL_DOMAIN=tipcontact.com TRUSTEDIP=69.41.164.75 do_dkim_with_tc_key

do_single:
	yum -y install postfix
	cp main1.cf /etc/postfix/main.cf
	cp header_checks /etc/postfix/header_checks
	sed -i "s/{HOSTNAME}/${HOSTNAME1}/g" /etc/postfix/main.cf
	sed -i "s/{IPADDRESS}/${IPADDRESS1}/g" /etc/postfix/main.cf
	chkconfig --level 2345 postfix on
	-service sendmail stop
	-chkconfig sendmail off
	service postfix start
	echo Finish Setting Single Postfix

do_dual:
	yum -y install postfix
	cp main1.cf /etc/postfix/main.cf
	cp header_checks /etc/postfix/header_checks
	sed -i "s/{HOSTNAME}/${HOSTNAME1}/g" /etc/postfix/main.cf
	sed -i "s/{IPADDRESS}/${IPADDRESS1}/g" /etc/postfix/main.cf
	# Add configuration file for postfix2
	cp -rf /etc/postfix /etc/postfix2
	cp main2.cf /etc/postfix2/main.cf
	sed -i "s/{HOSTNAME}/${HOSTNAME2}/g" /etc/postfix2/main.cf
	sed -i "s/{IPADDRESS}/${IPADDRESS2}/g" /etc/postfix2/main.cf
	mkdir -p /var/spool/postfix2
	postfix -c /etc/postfix2 check
	cp postfix2 /etc/init.d/postfix2
	chmod +x /etc/init.d/postfix2
	chkconfig --level 2345 postfix on
	chkconfig --level 2345 postfix2 on
	-service sendmail stop
	-chkconfig sendmail off
	service postfix start
	service postfix2 start
	echo Finish Setting Dual Postfix

do_dkim:
	yum install -y sendmail-devel openssl-devel gcc
	wget http://judezhan.com/src/opendkim-2.4.2.tar.gz
	tar zxvf opendkim-2.4.2.tar.gz
	cd opendkim-2.4.2 && ./configure --sysconfdir=/etc --prefix=/usr/local --localstatedir=/var && make && make install
	groupadd opendkim
	useradd -r -g opendkim -G mail -s /sbin/nologin -d /var/run/opendkim -c "OpenDKIM" opendkim
	mkdir -p /var/run/opendkim
	chown opendkim:opendkim /var/run/opendkim
	chmod 700 /var/run/opendkim
	mkdir -p /etc/opendkim/keys
	chown -R opendkim:opendkim /etc/opendkim
	chmod -R go-wrx /etc/opendkim/keys
	cp ./opendkim-2.4.2/contrib/init/redhat/opendkim /etc/init.d/
	chmod 755 /etc/init.d/opendkim
	mkdir -p /etc/opendkim/keys/${MAIL_DOMAIN}
	/usr/local/bin/opendkim-genkey -D /etc/opendkim/keys/${MAIL_DOMAIN}/ -d ${MAIL_DOMAIN} -s ${SELECTOR}
	cp /etc/opendkim/keys/${MAIL_DOMAIN}/${SELECTOR}.private /etc/opendkim/keys/${MAIL_DOMAIN}/${SELECTOR}
	chown -R opendkim:opendkim /etc/opendkim/keys/${MAIL_DOMAIN}
	cp ./opendkim.conf /etc/opendkim.conf
	cp ./KeyTable /etc/opendkim/KeyTable
	sed -i "s/{SELECTOR}/${SELECTOR}/g" /etc/opendkim/KeyTable
	sed -i "s/{MAIL_DOMAIN}/${MAIL_DOMAIN}/g" /etc/opendkim/KeyTable
	cp ./SigningTable /etc/opendkim/SigningTable
	sed -i "s/{SELECTOR}/${SELECTOR}/g" /etc/opendkim/SigningTable
	sed -i "s/{MAIL_DOMAIN}/${MAIL_DOMAIN}/g" /etc/opendkim/SigningTable
	cp ./TrustedHosts /etc/opendkim/TrustedHosts
	echo ${MAIL_DOMAIN} >> /etc/opendkim/TrustedHosts
	echo ${TRUSTEDIP} >> /etc/opendkim/TrustedHosts
	chkconfig --level 2345 opendkim on
	echo Finish Setting OpenDKIM
	@echo "#####################################################################################################"
	@echo "Now please add the TXT data in /etc/opendkim/keys/${MAIL_DOMAIN}/${SELECTOR}.txt to your DNS record!"
	@echo "Otherwise, the DKIM won't work!"
	@echo "#####################################################################################################"

do_dkim_with_rm_key:
	yum install -y sendmail-devel openssl-devel gcc
	wget http://judezhan.com/src/opendkim-2.4.2.tar.gz
	tar zxvf opendkim-2.4.2.tar.gz
	cd opendkim-2.4.2 && ./configure --sysconfdir=/etc --prefix=/usr/local --localstatedir=/var && make && make install
	groupadd opendkim
	useradd -r -g opendkim -G mail -s /sbin/nologin -d /var/run/opendkim -c "OpenDKIM" opendkim
	mkdir -p /var/run/opendkim
	chown opendkim:opendkim /var/run/opendkim
	chmod 700 /var/run/opendkim
	mkdir -p /etc/opendkim/keys
	chown -R opendkim:opendkim /etc/opendkim
	chmod -R go-wrx /etc/opendkim/keys
	cp ./opendkim-2.4.2/contrib/init/redhat/opendkim /etc/init.d/
	chmod 755 /etc/init.d/opendkim
	mkdir -p /etc/opendkim/keys/${MAIL_DOMAIN}
	/usr/local/bin/opendkim-genkey -D /etc/opendkim/keys/${MAIL_DOMAIN}/ -d ${MAIL_DOMAIN} -s ${SELECTOR}
	# We use the exist key here!
	cp ./opendkim_rm.private /etc/opendkim/keys/${MAIL_DOMAIN}/${SELECTOR}
	chmod 600 /etc/opendkim/keys/${MAIL_DOMAIN}/${SELECTOR}
	rm /etc/opendkim/keys/${MAIL_DOMAIN}/${SELECTOR}.private
	cp ./opendkim_rm.txt /etc/opendkim/keys/${MAIL_DOMAIN}/${SELECTOR}.txt
	# Finish override the new generated keys!
	chown -R opendkim:opendkim /etc/opendkim/keys/${MAIL_DOMAIN}
	cp ./opendkim.conf /etc/opendkim.conf
	cp ./KeyTable /etc/opendkim/KeyTable
	sed -i "s/{SELECTOR}/${SELECTOR}/g" /etc/opendkim/KeyTable
	sed -i "s/{MAIL_DOMAIN}/${MAIL_DOMAIN}/g" /etc/opendkim/KeyTable
	cp ./SigningTable /etc/opendkim/SigningTable
	sed -i "s/{SELECTOR}/${SELECTOR}/g" /etc/opendkim/SigningTable
	sed -i "s/{MAIL_DOMAIN}/${MAIL_DOMAIN}/g" /etc/opendkim/SigningTable
	cp ./TrustedHosts /etc/opendkim/TrustedHosts
	echo ${MAIL_DOMAIN} >> /etc/opendkim/TrustedHosts
	echo ${TRUSTEDIP} >> /etc/opendkim/TrustedHosts
	chkconfig --level 2345 opendkim on
	echo Finish Setting OpenDKIM
	@echo "#####################################################################################################"
	@echo "Now please add the TXT data in /etc/opendkim/keys/${MAIL_DOMAIN}/${SELECTOR}.txt to your DNS record!"
	@echo "Otherwise, the DKIM won't work!"
	@echo "#####################################################################################################"

do_dkim_with_tc_key:
	yum install -y sendmail-devel openssl-devel gcc
	wget http://judezhan.com/src/opendkim-2.4.2.tar.gz
	tar zxvf opendkim-2.4.2.tar.gz
	cd opendkim-2.4.2 && ./configure --sysconfdir=/etc --prefix=/usr/local --localstatedir=/var && make && make install
	groupadd opendkim
	useradd -r -g opendkim -G mail -s /sbin/nologin -d /var/run/opendkim -c "OpenDKIM" opendkim
	mkdir -p /var/run/opendkim
	chown opendkim:opendkim /var/run/opendkim
	chmod 700 /var/run/opendkim
	mkdir -p /etc/opendkim/keys
	chown -R opendkim:opendkim /etc/opendkim
	chmod -R go-wrx /etc/opendkim/keys
	cp ./opendkim-2.4.2/contrib/init/redhat/opendkim /etc/init.d/
	chmod 755 /etc/init.d/opendkim
	mkdir -p /etc/opendkim/keys/${MAIL_DOMAIN}
	/usr/local/bin/opendkim-genkey -D /etc/opendkim/keys/${MAIL_DOMAIN}/ -d ${MAIL_DOMAIN} -s ${SELECTOR}
	# We use the exist key here!
	cp ./opendkim_tc.private /etc/opendkim/keys/${MAIL_DOMAIN}/${SELECTOR}
	chmod 600 /etc/opendkim/keys/${MAIL_DOMAIN}/${SELECTOR}
	rm /etc/opendkim/keys/${MAIL_DOMAIN}/${SELECTOR}.private
	cp ./opendkim_tc.txt /etc/opendkim/keys/${MAIL_DOMAIN}/${SELECTOR}.txt
	# Finish override the new generated keys!
	chown -R opendkim:opendkim /etc/opendkim/keys/${MAIL_DOMAIN}
	cp ./opendkim.conf /etc/opendkim.conf
	cp ./KeyTable /etc/opendkim/KeyTable
	sed -i "s/{SELECTOR}/${SELECTOR}/g" /etc/opendkim/KeyTable
	sed -i "s/{MAIL_DOMAIN}/${MAIL_DOMAIN}/g" /etc/opendkim/KeyTable
	cp ./SigningTable /etc/opendkim/SigningTable
	sed -i "s/{SELECTOR}/${SELECTOR}/g" /etc/opendkim/SigningTable
	sed -i "s/{MAIL_DOMAIN}/${MAIL_DOMAIN}/g" /etc/opendkim/SigningTable
	cp ./TrustedHosts /etc/opendkim/TrustedHosts
	echo ${MAIL_DOMAIN} >> /etc/opendkim/TrustedHosts
	echo ${TRUSTEDIP} >> /etc/opendkim/TrustedHosts
	chkconfig --level 2345 opendkim on
	echo Finish Setting OpenDKIM
	@echo "#####################################################################################################"
	@echo "Now please add the TXT data in /etc/opendkim/keys/${MAIL_DOMAIN}/${SELECTOR}.txt to your DNS record!"
	@echo "Otherwise, the DKIM won't work!"
	@echo "#####################################################################################################"

start:
	hash -r
	service opendkim start
	postfix reload
