#!/usr/bin/python
#coding=utf-8

import os
import toolkit

'''
Created on 2016-4-28

@author: admin
'''

datadir = "data"
if not os.path.exists(datadir):
    os.mkdir(datadir)
    
# output file: <datadir>/get_users_output.txt
outfile = os.path.join(datadir, "get_users_output.txt")
# exclude the users in <datadir>/excluding_users.txt
#excluding_users = toolkit._read_many(os.path.join(datadir, "excluding_users.txt"))

def latest_users(many, out=outfile, ex=[]):
    # users(from leancloud) - excluding_users(from followees.txt)
    users = toolkit.many_users(many)
    ex_users = []
    for e in ex:
        for u in users:
            if u.get("username") == e:
                ex_users.append(u)
    for u in ex_users:
        users.remove(u)
    
    # prepare used datum
    uname_uid_list = [(user.get('username'),user.id) for user in users]
    
    # output to file
    outf = open(out, 'w')
    for (username, userid) in uname_uid_list:
        #print >>outf, "%-30s, %s" % (username, userid)
        print >>outf, username
    outf.close()
    
if __name__ == '__main__':
    latest_users(10)
    