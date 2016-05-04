#!/usr/bin/python
#coding=utf-8
import StringIO
import urllib
import pycurl
import json

import toolkit
import MyEnv

'''
Created on 2016-4-27
@author: Michael Yu
'''

################# MyCurl Class
'''MyCurl2
Using user id to convey the session information
'''
class MyCurl2(object):
    def __init__(self, url, username):
        self.url = MyEnv.urlprefix + url;
        self.username = username
        self.user = toolkit.user_by_username(username)
        self.headers = ["Content-Type: application/json; charset=utf-8", 
                        MyEnv.header_appid, 
                        MyEnv.header_appkey, 
                        "X-LC-Prod: 1"]
        self.myc = pycurl.Curl()
        
    def __del__(self):
        pass
     
    def showheaders(self):
        print self.headers
        
    def add_sessiontoken_to_headers(self, sessiontoken):
        self.sessiontoken = sessiontoken;
        self.headers.append(str("X-LC-Session: "+self.sessiontoken));
    
    def setopt_(self):
        self.myc.setopt(pycurl.SSL_VERIFYPEER, False)
        self.myc.setopt(pycurl.HTTPHEADER, self.headers)
        self.myc.setopt(pycurl.URL, self.url)
        #self.myc.setopt(pycurl.VERBOSE, True)
    
    def post(self, jsondata):
        if self.user is None:
            print "error: %s does not exist" % self.username
            return
        jsondata["user"]={"id":self.user.id}
        self.setopt_()
        self.myc.setopt(pycurl.POSTFIELDS, json.dumps(jsondata))
        
        buf = StringIO.StringIO()
        self.myc.setopt(pycurl.WRITEFUNCTION, buf.write)
        self.myc.perform()
        response = buf.getvalue()
        buf.close()
        
        return response
    
################# Frequently Used Object Samples
user_info_C = MyCurl2("/1.1/functions/user_info", "user00001@may.event")
#########################################

def demo_userinfo():
    user_info_C.showheaders()
    res = user_info_C.post({"userId":"56c7d005d342d300543379e2"})
    resjson = json.loads(res)
    print resjson
    
if __name__=='__main__':
    demo_userinfo()
    