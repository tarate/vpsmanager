#!/usr/bin/env python

from bottle import *
import MySQLdb
from pdb import set_trace as st

from utils import _add_vps, _delete_vps, _get_vps_list, _get_vps_details, _edit_vps
from datetime import datetime

app_vps = Bottle()

@app_vps.route('/<filename>')
def file_serv(filename):
    return static_file(filename, './static/')

@app_vps.get('/')
@app_vps.get('/test')
def test():
    redirect('/vps')
    #return "Hello, this is the test page for TARATE VPS Manager System!"

@app_vps.get('/vps/add')
def get_add_vps():
    return template('./template/addvps.tpl')

@app_vps.post('/vps/add')
def post_add_vps():
    '''
    vps has 10 attributes and when add a new one, client need to
    POST the last 8 attributes:
    id
    vps_vender
    vps_ac
    vps_ip
    vps_remark
    vps_status
    vps_type
    vps_score
    vps_price
    '''
    vps_info = {}
    vps_info.update(vps_vender=request.forms.get('vps_vender'))
    vps_info.update(vps_ac=request.forms.get('vps_ac'))
    vps_info.update(vps_ip=request.forms.get('vps_ip'))
    vps_info.update(vps_os=request.forms.get('vps_os'))
    vps_info.update(vps_root_passwd=request.forms.get('vps_root_passwd'))
    vps_info.update(vps_cpanel_addr=request.forms.get('vps_cpanel_addr'))
    vps_info.update(vps_cpanel_user=request.forms.get('vps_cpanel_user'))
    vps_info.update(vps_cpanel_passwd=request.forms.get('vps_cpanel_passwd'))
    vps_info.update(vps_remark=request.forms.get('vps_remark'))
    vps_info.update(vps_type=request.forms.get('vps_type'))

    vps_price = request.forms.get('vps_price')
    if not vps_price.startswith('$'):
        vps_price = '$' + vps_price
    vps_info.update(vps_price=vps_price)
    (result, info) = _add_vps(vps_info)

    if result:
        redirect('/vps')
    else:
        return "Failed: %s" % info

@app_vps.get('/vps/edit/<vid:int>')
def get_edit_vps(vid):
    (result, result_data) = _get_vps_details(vid)
    if result:
        _id, vender, ac, ip, os, root_passwd, cpanel_addr, cpanel_user, cpanel_passwd, remark, status, _type, score, created_time, updated_time, price = result_data[0]
        return template('./template/editvps.tpl', dict(vps_id=_id,
                                                       vps_vender=vender,
                                                       vps_ac=ac,
                                                       vps_ip=ip,
                                                       vps_os=os,
                                                       vps_root_passwd=root_passwd,
                                                       vps_cpanel_addr=cpanel_addr,
                                                       vps_cpanel_user=cpanel_user,
                                                       vps_cpanel_passwd=cpanel_passwd,
                                                       vps_remark=remark,
                                                       vps_status=status,
                                                       vps_type=_type,
                                                       vps_score=score,
                                                       vps_created_time=created_time,
                                                       vps_updated_time=updated_time,
                                                       vps_price=price))

@app_vps.post('/vps/edit/<vid:int>')
def post_edit_vps(vid):
    '''
    vps has 10 attributes and when edit, client need to
    POST the attributes below:
    vps_vender
    vps_ac
    vps_os
    vps_ip
    vps_root_passwd
    vps_cpanel_addr
    vps_cpanel_user
    vps_cpanel_passwd
    vps_remark
    vps_status
    vps_type
    vps_score
    vps_price
    '''
    vps_info = {}
    vps_info.update(vps_vender=request.forms.get('vps_vender'))
    vps_info.update(vps_ac=request.forms.get('vps_ac'))
    vps_info.update(vps_os=request.forms.get('vps_os'))
    vps_info.update(vps_ip=request.forms.get('vps_ip'))
    vps_info.update(vps_root_passwd=request.forms.get('vps_root_passwd'))
    vps_info.update(vps_cpanel_addr=request.forms.get('vps_cpanel_addr'))
    vps_info.update(vps_cpanel_user=request.forms.get('vps_cpanel_user'))
    vps_info.update(vps_cpanel_passwd=request.forms.get('vps_cpanel_passwd'))
    vps_info.update(vps_remark=request.forms.get('vps_remark'))
    vps_info.update(vps_type=request.forms.get('vps_type'))
    vps_info.update(vps_status=request.forms.get('vps_status'))

    vps_price = request.forms.get('vps_price')
    if not vps_price.startswith('$'):
        vps_price = '$' + vps_price
    vps_info.update(vps_price=vps_price)
    (result, info) = _edit_vps(vid ,vps_info)

    if result:
        redirect('/vps/details/%s' % vid)
    else:
        return "Failed: %s" % info

@app_vps.get('/vps')
@app_vps.get('/vps/<page:int>')
def get_vps_list(page=1):
    '''
    Each page contains at most 10 record!
    '''
    (result, result_data) = _get_vps_list(page)
    data = []
    if not result:
        return "Failed: %s" % result_data
    for record in result_data:
        if not record:
            continue
        _id, vender, ip, remark, status, _type, score, updated_time, price = record
        #_id = '<a href="http://localhost:8000/vps/details/%d">' % int(_id) + str(_id) + '</a>'
        _id = '<a href="/vps/details/%d">' % int(_id) + str(_id) + '</a>'
        if score >= 80:
            #score = '<font color="#00FF00">' + str(score) + '</font>'
            score = '<font color="green">' + str(score) + '</font>'
        elif score >= 60 and score < 80:
            score = '<font color="yellow">' + str(score) + '</font>'
        else:
            score = '<font color="red">' + str(score) + '</font>'

        if (status.lower() == 'running'):
            status = '<font color="green">' + status + '</font>'
        elif status.lower() == 'new added':
            status = '<font color="blue">' + status + '</font>'
        else:
            status = '<font color="red">' + status + '</font>'
        data.append((_id, vender, ip, remark, status, _type, score, updated_time, price))

    return template('./template/vpslist.tpl', result_data=data)

@app_vps.get('/vps/details/<vid:int>')
def get_vps_detail(vid):
    '''
    Get the details about one certain VPS Server
    '''
    (result, result_data) = _get_vps_details(vid)
    if result:
        _id, vender, ac, ip, os, root_passwd, cpanel_addr, cpanel_user, cpanel_passwd, remark, status, _type, score, created_time, updated_time, price = result_data[0]
        if score < 80:
            score = '<font color="red">' + str(score) + '</font>'
        else:
            score = '<font color="#00FF00">' + str(score) + '</font>'

        if status.lower() == 'running':
            status = '<font color="#00FF00">' + status + '</font>'
        elif status.lower() == 'new added':
            status = '<font color="blue">' + status + '</font>'
        else:
            status = '<font color="red">' + status + '</font>'

        if not cpanel_addr.startswith('http'):
            cpanel_addr = 'http://' + cpanel_addr

        cpanel_addr = '<a href="%s" target="blank">' % cpanel_addr + cpanel_addr + '</a>'

        return template('./template/vpsdetail.tpl', dict(vps_id=_id,
                                                         vps_vender=vender,
                                                         vps_ac=ac,
                                                         vps_ip=ip,
                                                         vps_os=os,
                                                         vps_root_passwd=root_passwd,
                                                         vps_cpanel_addr=cpanel_addr,
                                                         vps_cpanel_user=cpanel_user,
                                                         vps_cpanel_passwd=cpanel_passwd,
                                                         vps_remark=remark,
                                                         vps_status=status,
                                                         vps_type=_type,
                                                         vps_score=score,
                                                         vps_created_time=created_time,
                                                         vps_updated_time=updated_time,
                                                         vps_price=price))
    else:
        return result_data

@app_vps.get('/vps/delete/<vid:int>')
def get_delete_vps(vid):
    '''
    delete VPS
    '''
    (result, result_data) = _delete_vps(vid)
    if result:
        redirect('/vps')
    else:
        return result_data

if __name__ == '__main__':
    debug(True)
    run(app=app_vps, host='localhost', port=8000)
