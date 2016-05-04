#!/usr/bin/python
#coding=utf-8
import json
import leancloud
import MyEnv

from leancloud import Query

# initialize the environment to Sioeye_UT03
leancloud.init(MyEnv.appid, MyEnv.appkey)

'''
Created on 2016-4-27
@author: Michael Yu
'''

debug_flag = True
#debug_flag = False
    
################################## file category
def _read_many(filepath):
    f = open(filepath, "r")
    data = [line.strip() for line in f.readlines() if len(line) > 0]
    f.close()
    while '' in data:
        data.remove('')
    return data
    
################################# debug category
def showo_inDict(o):
    if debug_flag:
        print "-----------"
        d = dict(o.dump())
        for (k,v) in d.items():
            print "%10s : %-s" % (k,v)
            
def showo_inStr(o):
    if debug_flag:
        print o.dump()
            
print_func = showo_inDict
    
# print the query's result list
def showrl(qr, show_func=print_func):
    if debug_flag:
        for o in qr:
            show_func(o)
        print len(qr)
    
################################## leancloud - device
def active_device_by_username(username):
    print "========= %s" % username
    uq = Query("_User")
    uq.equal_to("username", username)
    user = uq.first()
    showo_inDict(user)
    
    dq = Query("Device")
    dq.equal_to("caster", user)
    dq.equal_to("status", "Active")
    device_list = dq.find()
    showrl(device_list)
    return device_list
    
################################## leancloud - user
# To print user id, by username
def user_by_username(username):
    query = Query("_User")
    query.equal_to('username', username)
    user = query.first()
#    if user is not None:
#        showo_inDict(user)
    return user
    
# To print user's import properties, by username
def user_info_by_username(username, showfunc=showo_inDict):
    query = Query("_User")
    query.include("sioeyeInfo")
    query.include("sioeyeInfo.avatar")
    
    query.equal_to('username', username)
    user = query.first()
    user_info = user.get("sioeyeInfo")
    user_avatar = user_info.get("avatar")
    if user is not None:
        print "=== user ==="
        showfunc(user)
    if user_info is not None:
        print "=== user info ==="
        showfunc(user_info)
    if user_avatar is not None:
        print "=== user avatar==="
        showfunc(user_avatar)
        
#    print "%s: %s" % (username, user_info.get("sioeyeId"))
    print "------------ next ------------"
    
# To print <many> users
def many_users(many):
    query = Query("_User")
    query.descending("createdAt")
    query.include("sioeyeInfo")
    query.limit(many)
    users = query.find()
    return users
    
# print user's username without sioeyeId
def _username_without_sioeye_id(many):
    has_sioeyeId = []
    has_no_sioeyeId = []
    has_no_userinfo = []
    
    query = Query("_User")
    query.include("sioeyeInfo")
    query.include("sioeyeInfo.avatar")
    
    query.limit(many)
    users = query.find()
    
    for (i, u) in enumerate(users):
        u_info = u.get("sioeyeInfo")
        
        sioeyeId = None
        if u_info is not None:
            sioeyeId = u_info.get("sioeyeId")
        
        if u_info is None:
            has_no_userinfo.append(u.get("username"))
        elif sioeyeId is None:
            has_no_sioeyeId.append(u.get("username"))
        else:
            has_sioeyeId.append(u.get("username"))
        
    return (has_sioeyeId, has_no_userinfo, has_no_sioeyeId)
    
################################## leancloud - live
def _latest_live_by_creater_startswith_title(username, title):
    lq = Query("Live")
    caster = user_by_username(username)
    lq.equal_to("caster", caster)
    lq.startswith("keyword", title)
    lq.descending("createdAt")
    live = lq.first()
    showo_inDict(live)
    return live
    
################################## leancloud - conversation
def _latest_convs_by_creater(username):
    cq = Query("_Conversation")
    creater = user_by_username(username)
    cq.equal_to("c", creater.id)
    cq.descending("createdAt")
    convs = cq.find()
    return convs
    
def _add_m_in_conv_id(newmem, convid):
    cq = Query("_Conversation")
    cq.equal_to("objectId", convid)
    conv = cq.first()
    
    mem_list = conv.get("m")
    mem = mem_list + newmem
    # remove the repeated item
    conv.set("m", list(set(mem)))
    conv.save()
    
def _remove_m_in_conv_id(delmem, convid):
    cq = Query("_Conversation")
    cq.equal_to("objectId", convid)
    conv = cq.first()
    
    mem_list = conv.get("m")
    mem = list(set(mem_list) - set(delmem))
    conv.set("m", list(set(mem)))
    conv.save()
    
if __name__ == '__main__':
    pass
    