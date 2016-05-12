#!/usr/bin/python
# -*- coding: utf-8 -*-  

'''
Created on 2016-5-12
@author: Michael Yu
'''

import sys
import os
import optparse
import toolkit
import push

def commandui(args=sys.argv[1:]):
    parser = optparse.OptionParser(usage="%prog [options]", version="%prog 1.0")
    
    parser.add_option("-l", "--live",
                      dest="live_file",
                      action="store",
                      default=None,
                      help="the file specifying the lives' id. By default, lives.txt")
    parser.add_option("-w", "--watcher",
                      dest="watcher_file",
                      action="store",
                      default="watchers.txt",
                      help='the file specifying the watcher (username). No default value, watchers.txt')
    parser.add_option("-i", "--liveid", 
                      dest="liveid",
                      action="store",
                      default=None,
                      help='a live(id) which sends out notification. option "-i" overrides options "-l". No default value')
    parser.add_option("-r", "--receiver", 
                      dest="receiver",
                      action="store",
                      default=None,
                      help='a receiver (username) who receives notification. option "-r" overrides options "-w".No default value')
    
    (options, args) = parser.parse_args(args)
    
    lives = None
    if options.liveid is not None:
        lives = [options.liveid]
    else: 
        lives = toolkit._read_many(options.live_file);
        
    watchers = None
    if options.receiver is not None:
        watchers = [options.receiver]
    else:
        watchers = toolkit._read_many(options.watcher_file);
    
    print '''lives (id: %s) 
will send out notification to 
watchers(username: %s)''' % (lives, watchers)
    for liveid in lives:
        push.send_pushs(liveid, watchers)

if __name__ == '__main__':
#    commandui(args=['-l', 'lives2.txt', '-w', 'watchers2.txt'])
#    commandui(args=['-i', '56cad6cdefa631005c3653b7', '-r', 'alice@sioeye.com'])
#    commandui(args=['-l', 'data/lives.txt', '-w', 'data/watchers.txt'])
#    commandui(args=['-i', '56e8d393c4c97100515463ff', '-r', 'user00001@may.event', '-l', 'lives.txt', '-w', 'watchers.txt'])
    commandui()
    