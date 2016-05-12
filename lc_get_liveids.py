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

def commandui(args=sys.argv[1:]):
    parser = optparse.OptionParser(usage="%prog [options] username", version="%prog 1.0")
    
    parser.add_option("-o", "--out",
                      dest="out",
                      action="store",
                      default="get_liveids_result.txt",
                      help='user name output file. By default, get_liveids_result.txt')
    parser.add_option("-n", "--number",
                      dest="number",
                      action="store",
                      default=10,
                      type="int",
                      help="limit every username's live number. By default, 10")
    
    (options, args) = parser.parse_args(args)
    
    if len(args) == 0:  
        parser.error("incorrect number of arguments. args: username") 
    print args
    
    # output to file
    outf = open(options.out, 'w')
    for username in args:
        lives = toolkit.live_by_username(username, options.number)
        print >>outf, "===================================="
        print >>outf, "username: %s" % username
        for live in lives:
            print >>outf, live.id
        print >>outf, ""
    outf.close()
    
if __name__ == '__main__':
#    commandui(args=["alice@sioeye.com", "user00001@may.event", "-n", "10", "-o", "data/get_iveids.txt"])
    commandui()
    