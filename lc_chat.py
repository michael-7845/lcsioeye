#!/usr/bin/python
# -*- coding: utf-8 -*-  

'''
Created on 2016-5-3
@author: Michael Yu
'''

import sys
import os
import time
import optparse
import toolkit
import chat

def _handle_users_beginner(users, beginner, using_id=False):
    _users = users
    _beginner = beginner
    
    if using_id: # users and beginner are provided in sioeye id
        _users = []
        for sioeye_id in users:
            user = toolkit.user_by_sioeyeid(sioeye_id)
            if user is not None:
                _users.append(user.get("username"))
            else:
                print "Sioeye id '%s' does not exist!" % sioeye_id
        
        user = toolkit.user_by_sioeyeid(beginner) # beginner is in sioeye id
        if user is not None:
            _beginner = user.get("username")
        else:
            print "beginner's Sioeye id '%s' does not exist!" % beginner
            exit(1)
            
    return _users, _beginner, 
    
def _enter(users, beginner, title, using_id=False):
    (_users, _beginner) = _handle_users_beginner(users, beginner, using_id)
    print "users: ", _users
    print "beginner: ", _beginner
    print "title starts with: ", title
    print ">>> running now ..."
    
    for (i,u) in enumerate(_users):
        print "%04d: user(%s) is enterring conversation(created by %s, title starts with '%s')." \
        % (i, u, _beginner, title)
        chat.user_enter_conv_of_creator_title(u, _beginner, title)

def _exit(users, beginner, title, using_id=False):
    (_users, _beginner) = _handle_users_beginner(users, beginner, using_id)
    print "users: ", _users
    print "beginner: ", _beginner
    print "title starts with: ", title
    print ">>> running now ..."
    
    for (i,u) in enumerate(_users):
        print "%04d: user(%s) is exiting conversation(created by %s, title starts with '%s')." \
        % (i, u, _beginner, title)
        chat.user_exit_conv_of_creator_title(u, _beginner, title)
        
def _chat(users, beginner, title, message="=== testing message. ===", withtime=False, interval=0, using_id=False):
    (_users, _beginner) = _handle_users_beginner(users, beginner, using_id)
    print "users: ", _users
    print "beginner: ", _beginner
    print "title starts with: ", title
    print ">>> running now ..."
    
    import time
    for (i,u) in enumerate(_users):
        print "%04d: user(%s) is sending message in conversation(created by %s, title starts with '%s')." \
        % (i, u, _beginner, title)
        chat.user_send_in_conv_of_creator_title(u, _beginner, title, message, withtime)
        time.sleep(interval)

def commandui(args=sys.argv[1:]):
    parser = optparse.OptionParser(usage="%prog [options]", version="%prog 1.0")
    
    parser.add_option("-i", "--in",
                      dest="enter",
                      action="store_true",
                      default=False,
                      help='enter the conversation')
    parser.add_option("-o", "--out",
                      dest="exit",
                      action="store_true",
                      default=False,
                      help='exit the conversation')
    parser.add_option("-c", "--chat",
                      dest="chat",
                      action="store_true",
                      default=False,
                      help='chat, sending message')
    
    parser.add_option("-b", "--beginner",
                      dest="beginner",
                      action="store",
                      default=None,
                      help='the conversation creater, equally the live caster. No default value')
    parser.add_option("-t", "--title",
                      dest="title",
                      action="store",
                      default=None,
                      help='the conversation title, equally the live title, the string beginning with. No default value')
    parser.add_option("-m", "--member", 
                      dest="member",
                      action="store",
                      default=None,
                      help='the conversation participant. No default value')
    parser.add_option("-f", "--file", 
                      dest="file",
                      action="store",
                      default=None,
                      help='file, specifying conversation participant. No default value')
    parser.add_option("--message", 
                      dest="message",
                      action="store",
                      default="hello",
                      help='the sending message. By default, "=== hello ==="')
    parser.add_option("--time",
                      dest="withtime",
                      action="store_true",
                      default=False,
                      help='if sending message postfixes time. By default, not prefix time')
    parser.add_option("--interval", 
                      dest="interval",
                      action="store",
                      default=0,
                      type=int,
                      help='sending interval. By default, 0s, i.e. no delay between sending')
    parser.add_option("--id", "--sioeyeid", 
                      dest="sioeyeid",
                      action="store_true",
                      default=False,
                      help='if the sioeye id is used, instead of username. By default, username is used.')
    
    (options, args) = parser.parse_args(args)
    
    members = []
    if options.file is not None:
        members = toolkit._read_many(options.file)
    elif options.member is not None:
        members.append(options.member)
    else:
        parser.error("no chat members!")
    
    if options.beginner is None:
        parser.error("no chat beginner!")
    
    if options.title is None:
        parser.error("no chat title!")
    
    if options.enter: # enter the conversation
        _enter(members, options.beginner, options.title, options.sioeyeid)
    elif options.exit: # exit the conversation
        _exit(members, options.beginner, options.title, options.sioeyeid)
    elif options.chat:
        _chat(members, options.beginner, options.title, options.message, options.withtime, options.interval, options.sioeyeid)
    else:
        parser.error("Please select action: -i or -o or -c .")

if __name__ == '__main__':
#    commandui(args=['-c', '-b', 'alice@sioeye.com', '-t', "alice is", '-f', 'members.txt'])
#    commandui(args=['-i', '-b', 'ali000', '-t', "alice is", '-f', 'ids.txt', '--time', '--id'])
#    commandui(args=['-c', '-b', 'alice@sioeye.com', '-t', "alice is", '-m', 'user00003@may.event', '--time', '--id'])
#    commandui(args=['-c', '-b', 'ali000', '-t', "alice is", '-m', 'use050', '--time', '--id'])
    commandui()
    
