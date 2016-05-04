#!/usr/bin/python
#coding=utf-8
import os
import time
import json
import toolkit

from MyCurl import users_C
from MyDict import MyDict

from MyCurl2 import MyCurl2 as MyCurl2

'''
Created on 2016-4-28
@author: Michael Yu
'''

################# me_unfollow_many #################
def me_unfollow_many(me, many):
    if me in many:
        many.remove(me)
    
    for followee in many:
        _a_unfollow_b(me, followee)
####################################################
    
############# fans_unfollow_followers ##############
def fans_unfollow_followers(fans_file, follower_file):
    fans = toolkit._read_many(fans_file)
    followers = toolkit._read_many(follower_file)
    
    for (i, fan) in enumerate(fans):
        for (j, follower) in enumerate(followers):
            print "= %03d,%03d = %s is unfollowing %s" % (i, j, fan, follower)
            _a_unfollow_b(fan, follower)
            
####################################################
    
def _a_unfollow_b(a, b):
    print "me: %s, followee: %s" % (a, b)
    followee_add_C = MyCurl2("/1.1/functions/followee_remove", a)
    
    user = toolkit.user_by_username(b)
    userid = ""
    if user is not None:
        userid = user.id
        print userid
    
    # follow
    res = followee_add_C.post({"id": userid})
    print res
    time.sleep(0.2)
    
if __name__ == '__main__':
    #me_unfollow_many(me, many)
    fans_unfollow_followers("unfans.txt", "unfollowers.txt")
    