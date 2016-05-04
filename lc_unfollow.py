#!/usr/bin/python
# -*- coding: utf-8 -*-  

'''
Created on 2016-5-3
@author: Michael Yu
'''

import sys
import os
import optparse
import me_unfollow_many

def commandui(args=sys.argv[1:]):
    parser = optparse.OptionParser(usage="%prog [options]", version="%prog 1.0")
    
    parser.add_option("-f", "--fans",
                      dest="fans",
                      action="store",
                      default="fans.txt",
                      help="file, specifying fans' user name. By default, fans.txt")
    parser.add_option("-t", "--target",
                      dest="target",
                      action="store",
                      default="unfollowers.txt",
                      help="file, specifying user name who will be unfollowed. By default, unfollowers.txt")
    
    (options, args) = parser.parse_args(args)
    
    if not os.path.exists(options.fans):
        parser.error("fans file does not exist!")
    
    if not os.path.exists(options.target):
        parser.error("target file does not exist!")
    
    me_unfollow_many.fans_unfollow_followers(options.fans, options.target)

if __name__ == '__main__':
    commandui()