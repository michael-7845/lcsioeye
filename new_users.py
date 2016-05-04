#!/usr/bin/python
#coding=utf-8
import time
import json
import toolkit

#from MyCurl import users_C
from MyDict import MyDict

from MyCurl import MyCurl as MyCurl
from MyCurl2 import MyCurl2 as MyCurl2

'''
Created on 2016-4-27
@author: Michael Yu
'''

################### Configuration Code Area - Begin
# (nickname, username, email, password)
# NEW_USERS = [("user00001", "user00001@may.event", "user00001@may.event", "12345678"),
#             ("user00002", "user00001@may.event", "user00002@may.event", "12345678"),
#             ("user00003", "user00001@may.event", "user00003@may.event", "12345678"),
#             ...]
_user_prefix = "user"
_user_range = range(13,14) # (1, 2, 3)
_mail_postfix = "@may.event"
_password = "12345678"

def _prepareUserInfo(user_prefix=_user_prefix,
                    user_range=_user_range,
                    mail_postfix=_mail_postfix,
                    password=_password):
    res = []
    for i in user_range:
        d = MyDict()
        d.nickname = "%s%05d" % (user_prefix, i)
        d.username = "%s%05d%s" % (user_prefix, i, mail_postfix) 
        d.email = "%s%05d%s" % (user_prefix, i, mail_postfix)
        d.password = password
        res.append(d)
    return res
#################### Configuration Code Area End
    
def createNewUsers(user_prefix, user_range, mail_postfix, password):
    NEW_USERS = _prepareUserInfo(user_prefix, user_range, mail_postfix, password)
    users_C = MyCurl("/1.1/users")
    
    for u in NEW_USERS:
        print "creating user: " + str(u)
        res = users_C.post({"username":u.username,
                            "email":u.email,
                            "password":u.password})
        print res
        
        res = _updateNickname(u.username, u.nickname)
        print res
        
        res = _update_sioeye_id(u.username, u.password)
        print res
        
# deviceId must be active and binding to the user
# using my mi's installationId
def _updateNickname(username, nickname, password="12345678", pushId="ABCDEFGHIJKLMNOPQRSTUVWXYZ000001"):
    print "========================"
    print username, "'s nickname will update to: ", nickname
        
    bind_device_C = MyCurl2("/1.1/functions/app_bind_device", username)
    res = bind_device_C.post({"push_id": pushId, "dev_type": "AndroidApp", 
                        "devInfo": "sioeye app", "appName": "Sioeye", 
                        "version": "1.4.0"})
    time.sleep(0.5)
    
    devlist = toolkit.active_device_by_username(username)
    devid = ""
    if devlist is not None:
        devid = devlist[0].id
        
    user_update_C = MyCurl2("/1.1/functions/user_update", username)
    res = user_update_C.post({"deviceId":devid,"nickname":nickname})
    time.sleep(0.2)
    
    return res
    
# /functions/cloud_update_sioeye_id
def _update_sioeye_id(username, password="12345678"):
    print "========================"
    print username, "will update sioeye id"
    
    login_C = MyCurl("/1.1/login")
    res = login_C.post({"username":username,"password":password})
    resjson = json.loads(res)
    print resjson['sessionToken']
    
    update_sioeye_id_C = MyCurl("/1.1/functions/cloud_update_sioeye_id")
    update_sioeye_id_C.add_sessiontoken_to_headers(resjson['sessionToken'])
    update_sioeye_id_C.showheaders()
    res = update_sioeye_id_C.post({})
    resjson = json.loads(res)
    print resjson
    
if __name__ == '__main__':
    pass
    