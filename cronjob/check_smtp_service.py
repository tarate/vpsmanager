#!/usr/bin/env python

from bs4 import BeautifulSoup
import smtplib, MySQLdb
from datetime import datetime
from pdb import set_trace as st

DBHOST = 'localhost'
DBUSER = 'root'
DBPASSWD = 'tgfdsaqwer'
DBNAME = 'tarate'
#TODO: FIXME!
SQL_UPDATE_SMTP_STATUS = 'UPDATE tarate_vps SET vps_score = %s, vps_updated_time = %s WHERE vps_ip = %s'
SQL_GET_VPS_IP = 'SELECT vps_ip FROM tarate_vps WHERE vps_status = \'running\''

def get_smtp_status(ip):
    print 'Start to get smtp service status for %s...' % ip
    try:
        handle = smtplib.SMTP(host=ip, port=25, timeout=10)
        return (True, 'on')
    except Exception, e:
        print 'Error occurs when getting smtp status for %s because %s' % (ip, str(e))
        return (True, 'off')
    finally:
        try:
            handle.close()
        except Exception:
            pass

def update_smtp_status_to_db(ip, score):
    print 'Start to update smtp status for %s...' % ip
    update_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        conn = MySQLdb.connect(host=DBHOST, user=DBUSER, passwd=DBPASSWD, db=DBNAME)
        cursor = conn.cursor()
        #TODO: FIXME!
        cursor.execute(SQL_UPDATE_SMTP_STATUS, (score, update_time, ip))
        conn.commit()
        return True
    except Exception, e:
        print 'Error occurs when updating smtp status to db for %s because %s' % (ip, str(e))
        return False
    finally:
        try:
            conn.close()
        except Exception:
            pass

def get_all_vps_ip():
    print 'Start to get all running vps\' ips...'
    try:
        conn = MySQLdb.connect(host=DBHOST, user=DBUSER, passwd=DBPASSWD, db=DBNAME)
        cursor = conn.cursor()
        cursor.execute(SQL_GET_VPS_IP)
        results = cursor.fetchall()
        if results:
            return (True, results)
        else:
            return (False, 'No Data Found!')
    except Exception, e:
        print 'Error occurs when getting all ips of running vps because %s' % str(e)
        return (False, str(e))
    finally:
        try:
            conn.close()
        except Exception:
            pass

if __name__ == '__main__':
    result_of_get_ip, ips = get_all_vps_ip()
    if result_of_get_ip:
        for ip in ips:
            if not ip:
                continue
            else:
                ip = ip[0]
            result_of_get_smtp_status, status = get_smtp_status(ip)
            if result_of_get_smtp_status:
                result_of_update_smtp_status = update_smtp_status_to_db(ip, status)
                if result_of_update_smtp_status:
                    print 'Succeed update smtp status for %s' % ip
    print 'Done!'
