#!/usr/bin/env python

import MySQLdb
import settings

from datetime import datetime

from pdb import set_trace as st

# This is a script contains lots of utils!
# Basicly, the functions implemented here
# starts with an underline (_).

def _add_vps(vps_info):
    '''
    vps_info is a dict contains the basic information of the
    vps about to add to DB.
    '''
    SQL = 'INSERT INTO tarate_vps (vps_vender, vps_ac, vps_ip, vps_os, vps_root_passwd, vps_cpanel_addr, vps_cpanel_user, vps_cpanel_passwd, vps_remark, vps_status, vps_type, vps_score, vps_created_time, vps_updated_time, vps_price)\
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        conn = MySQLdb.connect(host=settings.DB_HOST, user=settings.DB_USER, passwd=settings.DB_PASSWD, db=settings.DB_NAME)
        cursor = conn.cursor()
        cursor.execute(SQL, (vps_info.get('vps_vender'),
                             vps_info.get('vps_ac'),
                             vps_info.get('vps_ip'),
                             vps_info.get('vps_os'),
                             vps_info.get('vps_root_passwd'),
                             vps_info.get('vps_cpanel_addr'),
                             vps_info.get('vps_cpanel_user'),
                             vps_info.get('vps_cpanel_passwd'),
                             vps_info.get('vps_remark'),
                             'New Added',
                             vps_info.get('vps_type'),
                             0,
                             now,
                             now,
                             vps_info.get('vps_price')
                             )
                      )
        conn.commit()
    except Exception, e:
        return (False, str(e))
    finally:
        try:
            conn.close()
        except:
            pass
    return (True, '')

def _edit_vps(vps_id, vps_info):
    '''
    vps_info is a dict contains the basic information of the
    vps about to update to DB.
    vps_id the id of the vps about to edit.
    '''
    SQL = "UPDATE tarate_vps SET vps_vender='%s', vps_ac='%s', vps_ip='%s', vps_os='%s', vps_root_passwd='%s', vps_cpanel_addr='%s', \
            vps_cpanel_user='%s', vps_cpanel_passwd='%s', vps_remark='%s', vps_type='%s', vps_status='%s', vps_updated_time='%s', vps_price='%s' WHERE id=%d"
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        conn = MySQLdb.connect(host=settings.DB_HOST, user=settings.DB_USER, passwd=settings.DB_PASSWD, db=settings.DB_NAME)
        cursor = conn.cursor()
        cursor.execute(SQL % (vps_info.get('vps_vender'),
                             vps_info.get('vps_ac'),
                             vps_info.get('vps_ip'),
                             vps_info.get('vps_os'),
                             vps_info.get('vps_root_passwd'),
                             vps_info.get('vps_cpanel_addr'),
                             vps_info.get('vps_cpanel_user'),
                             vps_info.get('vps_cpanel_passwd'),
                             vps_info.get('vps_remark'),
                             vps_info.get('vps_type'),
                             vps_info.get('vps_status'),
                             now,
                             vps_info.get('vps_price'),
                             vps_id
                             )
                      )
        conn.commit()
    except Exception, e:
        return (False, str(e))
    finally:
        try:
            conn.close()
        except:
            pass
    return (True, '')

def _get_vps_list(page):
    '''
    Each page contains at most 10 records
    '''
    SQL = 'SELECT id, vps_vender, vps_ip, vps_remark, vps_status, vps_type, vps_score, vps_updated_time, vps_price FROM tarate_vps LIMIT %d, %d';
    try:
        conn = MySQLdb.connect(host=settings.DB_HOST, user=settings.DB_USER, passwd=settings.DB_PASSWD, db=settings.DB_NAME)
        cursor = conn.cursor()
        cursor.execute(SQL % ((page-1) * settings.RECORDS_PER_PAGE, settings.RECORDS_PER_PAGE))
        results = cursor.fetchall();
        return (True, results)
    except Exception, e:
        return (False, str(e))
    finally:
        try:
            conn.close()
        except:
            pass

def _get_vps_details(vid):
    '''
    Get the details information about one certain VPS Server
    '''
    SQL = 'SELECT id, vps_vender, vps_ac, vps_ip, vps_os, vps_root_passwd, vps_cpanel_addr, vps_cpanel_user, vps_cpanel_passwd, vps_remark, vps_status, vps_type, vps_score, vps_created_time, vps_updated_time, vps_price FROM tarate_vps WHERE id = %d';
    try:
        conn = MySQLdb.connect(host=settings.DB_HOST, user=settings.DB_USER, passwd=settings.DB_PASSWD, db=settings.DB_NAME)
        cursor = conn.cursor()
        cursor.execute(SQL % vid)
        results = cursor.fetchall();
        if results:
            return (True, results)
        else:
            return (False, 'Can not find record!')
    except Exception, e:
        return (False, str(e))
    finally:
        try:
            conn.close()
        except:
            pass

def _delete_vps(vid):
    '''
    Delete VPS
    '''
    SQL = 'DELETE FROM tarate_vps WHERE id = %d';
    try:
        conn = MySQLdb.connect(host=settings.DB_HOST, user=settings.DB_USER, passwd=settings.DB_PASSWD, db=settings.DB_NAME)
        cursor = conn.cursor()
        result = cursor.execute(SQL % vid)
        conn.commit()
        if int(result) == 1:
            return (True, result)
        else:
            return (False, 'Can not find record!')
    except Exception, e:
        return (False, str(e))
    finally:
        try:
            conn.close()
        except:
            pass

