#!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib2, MySQLdb
from datetime import datetime
from time import sleep
from pdb import set_trace as st

URL = 'https://senderscore.org/lookup.php?lookup=%s'
URLOPEN_TIMEOUT = 30
URL_REQUEST_INTERVAL = 30 # otherwise we may get request too frequently
DBHOST = 'localhost'
DBUSER = 'root'
DBPASSWD = 'tgfdsaqwer'
DBNAME = 'tarate'
SQL_UPDATE_SCORE = 'UPDATE tarate_vps SET vps_score = %s, vps_updated_time = %s WHERE vps_ip = %s'
SQL_GET_VPS_IP = 'SELECT vps_ip FROM tarate_vps WHERE vps_status = \'running\''
SQL_SAVE_RECORD_TO_HIS = 'INSERT INTO tarate_vps_score_his (vps_ip, vps_score, vps_updated_time) VALUES \
        (%s, %s, %s)'

def get_score_from_html(ip):
    print 'Start to get score for %s...' % ip
    try:
        handle = urllib2.urlopen(URL % ip, timeout=URLOPEN_TIMEOUT)
        html = handle.read()
        soup = BeautifulSoup(html)
        score = soup.find(id='senderScore').text.strip()
        if score == '?':
            return (True, '-1')
        else:
            return (True, score)
    except Exception, e:
        print 'Error occurs when getting score from web for %s because %s' % (ip, str(e))
        return (False, str(e))
    finally:
        try:
            handle.close()
        except Exception:
            pass

def update_score_to_db(ip, score):
    print 'Start to update score for %s...' % ip
    update_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        conn = MySQLdb.connect(host=DBHOST, user=DBUSER, passwd=DBPASSWD, db=DBNAME)
        cursor = conn.cursor()
        cursor.execute(SQL_UPDATE_SCORE, (score, update_time, ip))
        cursor.execute(SQL_SAVE_RECORD_TO_HIS, (ip, score, update_time))
        conn.commit()
        return True
    except Exception, e:
        print 'Error occurs when updating score to db for %s because %s' % (ip, str(e))
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
            result_of_get_score, score = get_score_from_html(ip)
            if result_of_get_score:
                result_of_update_score = update_score_to_db(ip, score)
                if result_of_update_score:
                    print 'Succeed update score for %s' % ip
            sleep(URL_REQUEST_INTERVAL)
    print 'Done!'
