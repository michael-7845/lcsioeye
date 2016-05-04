#!/usr/bin/python
# -*- coding: utf-8 -*-  

'''
Created on 2016-4-28
@author: Michael Yu
'''

import sys
import os
import optparse
import new_users

def commandui(args=sys.argv[1:]):
    parser = optparse.OptionParser(usage="%prog [options] begin_index end_index", version="%prog 1.0")
    
    parser.add_option("--prefix",
                      dest="user_prefix",
                      action="store",
                      default="user",
                      help='user prefix, e.g. "user00001@cd.test" prefix is user. By default, "user"')
    parser.add_option("--postfix",
                      dest="email_postfix",
                      action="store",
                      default="@cd.test",
                      help='username email postfix, e.g. "user00001@cd.test" postfix is @cd.test. By default, "@cd.text"')
    parser.add_option("--password",
                      dest="user_password",
                      action="store",
                      default="12345678",
                      help='user password, e.g. "12345678". By default, "12345678"')
    
    (options, args) = parser.parse_args(args)
    
    if len(args) != 2:  
        parser.error("incorrect number of arguments")
    begin = int(args[0])
    end = int(args[1])
    print "begin: ", begin, "end: ", end
    
    if (begin >= end):
        parser.error("User range is invalid. Please check begin index and end index.")
    
#    if options.create_new: # update tools
    print options.user_prefix, range(begin, end), options.email_postfix, options.user_password
    new_users.createNewUsers(options.user_prefix, 
                             range(begin, end), 
                             options.email_postfix, 
                             options.user_password)
    
if __name__ == '__main__':
    commandui()
