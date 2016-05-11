#!/usr/bin/python
# -*- coding: utf-8 -*-  

'''
Created on 2016-5-3
@author: Michael Yu
'''

import sys
import os
import optparse
import toolkit
import chat

def _enter(users, beginner, title):
    for u in users:
        chat.user_enter_conv_of_creator_title(u, beginner, title)

def _exit(users, beginner, title):
    for u in users:
        chat.user_exit_conv_of_creator_title(u, beginner, title)
        
def _chat(users, beginner, title, message="=== testing message. ===", withtime=False):
    for u in users:
        chat.user_send_in_conv_of_creator_title(u, beginner, title, message, withtime)

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
    
    (options, args) = parser.parse_args(args)
    
    members = []
    if options.file is not None:
        members = toolkit._read_many(options.file)
    elif options.member is not None:
        members.append(options.member)
    else:
        parser.error("no chat members!")
    print members
    
    if options.beginner is None:
        parser.error("no chat beginner!")
    
    if options.title is None:
        parser.error("no chat title!")
    
    if options.enter: # enter the conversation
        _enter(members, options.beginner, options.title)
    elif options.exit: # exit the conversation
        _exit(members, options.beginner, options.title)
    elif options.chat:
        _chat(members, options.beginner, options.title, options.message, options.withtime)
    else:
        parser.error("Please select action: -i or -o or -c .")

if __name__ == '__main__':
#    commandui(args=['-c', '-b', 'alice@sioeye.com', '-t', "alice is", '-f', 'data/members.txt'])
#    commandui(args=['-c', '-b', 'alice@sioeye.com', '-t', "alice is", '-m', 'user00003@may.event', '--time'])
    commandui()
    
