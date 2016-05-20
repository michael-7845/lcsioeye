#!/usr/bin/python
#coding=utf-8
import json
import leancloud
import MyEnv

from leancloud import Query

# initialize the environment to Sioeye_UT03
leancloud.init(MyEnv.appid, MyEnv.appkey)
#leancloud.init(MyEnv.appid, master_key=MyEnv.masterkey)
#if you want to use us environment, uncomment it.
#leancloud.use_region('US')

'''
Created on 2016-4-27
@author: Michael Yu
'''

#debug_flag = True
debug_flag = False
    
################################## file category
def _read_many(filepath):
    import os
    if not os.path.exists(filepath):
        print "%s does not exist!" % filepath
        exit(1)
    
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
        if o is None:
            print None
            return
        d = dict(o.dump())
        for (k,v) in d.items():
            print "%10s : %-s" % (k,v)
            
def showo_inStr(o):
    if debug_flag:
        if o is None:
            print None
            return
        print o.dump()
            
print_func = showo_inStr
    
# print the query's result list
def showrl(qr, show_func=print_func):
    if debug_flag:
        for o in qr:
            show_func(o)
        print len(qr)
    
################################## leancloud - device
def active_device_by_username(username):
    user = user_by_username(username)
    dq = Query("Device")
    dq.equal_to("caster", user)
    dq.equal_to("status", "Active")
    device_list = dq.find()
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
    
def user_by_sioeyeid(id):
    query = Query("UserInfo")
    query.equal_to("sioeyeId", id)
    query.include("userId")
    ui = None
    try:
        ui = query.first()
    except leancloud.errors.LeanCloudError:
        pass 
    user = None
    if ui is not None:
        user = ui.get("userId")
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
    (u, ui, ua) = (None, None, None)
    if user is not None:
        print "=== user ==="
        showfunc(user)
        u = user
    if user_info is not None:
        print "=== user info ==="
        showfunc(user_info)
        ui = user_info
    if user_avatar is not None:
        print "=== user avatar==="
        showfunc(user_avatar)
        ua = user_avatar
#    print "%s: %s" % (username, user_info.get("sioeyeId"))
    print "------------ next ------------"
    return u, ui, ua
    
# To print <many> users
def many_users(many):
    print MyEnv.appid, MyEnv.appkey
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
#    print mem
#    print list(set(mem)) 
    # remove the repeated item
    conv.set("m", list(set(mem)))
    conv.save()
    
def _remove_m_in_conv_id(delmem, convid):
    cq = Query("_Conversation")
    cq.equal_to("objectId", convid)
    conv = cq.first()
    
    mem_list = conv.get("m")
    mem = list(set(mem_list) - set(delmem))
#    print mem
    conv.set("m", list(set(mem)))
    conv.save()
    
################################## new : 
def my_fans(username, howmany=100):
    user = user_by_username(username)
    
    fans_q = Query("_Follower")
    fans_q.equal_to("user", user)
    fans_q.limit(howmany)
    fans_q.include("follower")
    fans_res = fans_q.find()
    showrl(fans_res, show_func=showo_inStr)
    
    f_q = Query("_Follower")
    f_q.equal_to("user", user)
    f_q.limit(howmany)
    device_q = Query("Device")
    device_q.matches_key_in_query("caster", "follower", f_q)
    device_q.equal_to("status", "Active")
    device_q.include("caster")
    device_q.limit(howmany)
    device_res = device_q.find()
    showrl(device_res, show_func=showo_inStr)
    
    d = {}
    for f in fans_res:
        follower = f.get("follower")
        active_dev = None
        for dev in device_res:
            if dev.get("caster").id == follower.id:
                active_dev = dev
        d[follower.get('username')] = (follower, active_dev)
    return d
    
############################# new : my_fans
def my_fans_demo():
    d = my_fans("pengfei.lin@ck-telecom.com", 500)
    
    # output to file
    outf = open("felix_fans.txt", 'w')
#    out_format = "%-30s, %-30s, %-30s, %-30s"
    out_format = "%s,%s,%s,%s"
    print >>outf, out_format % ("username", "email", "user-id", "active-device-id")
    for rn in sorted([n[::-1] for n in d.keys()]):
        rrn = rn[::-1]; fans = d[rrn][0]; device = d[rrn][1]
        if device is not None:
            print >>outf, out_format % (fans.get("username"), fans.get("email"), fans.id, device.id)
#        else:
#            print >>outf, out_format % (fans.get("username"), fans.get("email"), fans.id, None)
    outf.close()

############################# new : leancloud - live
def live_by_username(username, howmany):
    lq = Query("Live")
    user = user_by_username(username)
    lq.equal_to("caster", user)
    lq.limit(howmany)
    results = lq.find()
#    for res in results:
#        print "username: %s, user id: %s, live id: %s, nickname: %s" % (username, 
#                    user.id, res.id, user.get("nickname"))
    return results
    
def caster_by_live_id(live_id):
    lq = Query("Live")
    lq.equal_to("objectId", live_id)
    lq.include("caster")
    live = lq.first()
    return live.get("caster")
    
if __name__ == '__main__':
    pass
    
    
    
