#!/usr/bin/python
#coding=utf-8

import time
import toolkit

from MyCurl import MyCurl as MyCurl
from MyCurl3 import MyCurl3 as MyCurl3

'''
Created on 2016-4-29
@author: Michael Yu
'''

def _enter_conv(userid, convid):
    res = toolkit._add_m_in_conv_id([userid], convid)
    return res

def _exit_conv(userid, convid):
    res = toolkit._remove_m_in_conv_id([userid], convid)
    return res

def _send(senderid, convid, message="hello", withtime=False):
    c = MyCurl3("/1.1/rtm/messages")
    msg = message
    if withtime:
        msg = "%s - %s" % (message, time.ctime())
    res = c.post({"from_peer": senderid, 
                  "message": msg, 
                  "conv_id": convid, 
                  "transient": False})
    return res

# who: username
# room: convid
def _send_by_who_in_conv(username, convid, message="hello", withtime=False):
    sender = toolkit.user_by_username(username)
    return _send(sender.id, convid, message, withtime)

def user_enter_conv_of_creator_title(username, creator, title_beginning):
    user = toolkit.user_by_username(username)
    # latest conversation of creator, with title
    live = toolkit._latest_live_by_creater_startswith_title(creator, title_beginning)
    convid = live.get("conversationId")
    # enter conversation
    _enter_conv(user.id, convid)
    
def user_exit_conv_of_creator_title(username, creator, title_beginning):
    user = toolkit.user_by_username(username)
    # latest conversation of creator, with title
    live = toolkit._latest_live_by_creater_startswith_title(creator, title_beginning)
    convid = live.get("conversationId")
    # exit conversation
    _exit_conv(user.id, convid)
    
def user_send_in_conv_of_creator_title(username, creator, title_beginning, message="hello", withtime=False):
    # latest conversation of creator, with title
    live = toolkit._latest_live_by_creater_startswith_title(creator, title_beginning)
    convid = live.get("conversationId")
    # send message
    return _send_by_who_in_conv(username, convid, message, withtime)
    
def demo():
#    user_enter_conv_of_creator_title("user00004@may.event", "alice@sioeye.com", "alice is")
#    user_exit_conv_of_creator_title("user00003@may.event", "alice@sioeye.com", "alice is")
    user_send_in_conv_of_creator_title("user00002@may.event", "alice@sioeye.com", "alice is", 
                                       message="hello 2", withtime=True)
    
if __name__ == '__main__':
    demo()
    