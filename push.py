#!/usr/bin/python
#coding=utf-8

'''
Created on 2016-5-12

@author: michael yu
'''

import toolkit
from MyCurl import MyCurl as MyCurl

def _pushs_by_usernames(usernames):
    pushs = {}
    for username in usernames:
        d_result = toolkit.active_device_by_username(username)
        if len(d_result) == 0:
            pushs[username] = None
        else:
            pushs[username] = str(d_result[0].get("pushId").id)
    return pushs
    
def _send_push(target_push_id, nickname, live_id, user_id):
    push_C = MyCurl("/1.1/push")
    data = {
            "where":{"objectId":target_push_id},
            "data": {"type": 0,
                     "liveType": "Partial",
                     "action": "com.hike.hiliveapp.LIVE_STATUS",
                     "alert": "Your friend %s is on live." % nickname,
                     "liveId": live_id,
                     "userId": user_id}
            }
    res = push_C.post(data)
    return res
    
def send_pushs(liveid, watchers):
    pushs = _pushs_by_usernames(watchers)
    caster = toolkit.caster_by_live_id(liveid)
    (nickname, live_id, user_id) = (caster.get("nickname"), liveid, caster.id)
    
    for username in pushs:
        if pushs[username] is None:
            print "%s has no active device!" % username
        else:
            print "sending live(id: %s)'s notification to %s's device(id: %s) now." % \
                      (live_id, username, pushs[username])
            print _send_push(pushs[username], nickname, live_id, user_id)
    
    
if __name__ == '__main__':
    send_pushs("56cad6b17db2a200519b615d", ("alice@sioeye.com", "user00001@may.event", "user00002@may.event"))
    