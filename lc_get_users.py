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
import get_users

def commandui(args=sys.argv[1:]):
    parser = optparse.OptionParser(usage="%prog [options]", version="%prog 1.0")
    
    parser.add_option("-o", "--out",
                      dest="out",
                      action="store",
                      default="get_users_result.txt",
                      help='user name output file. By default, get_users_result.txt')
    parser.add_option("-e", "--exclude",
                      dest="ex",
                      action="store",
                      default=None,
                      help='file, specifying user name who will not be output. By default, no file')
    parser.add_option("-n", "--number",
                      dest="number",
                      action="store",
                      default=10,
                      type="int",
                      help='output user number. By default, 10')
    
    (options, args) = parser.parse_args(args)
    
    ex_list = []
    if options.ex is not None:
        ex_list = toolkit._read_many(options.ex)
    
    if options.out is not None:
        get_users.latest_users(options.number, out=options.out, ex=ex_list)
    
if __name__ == '__main__':
    commandui()
    