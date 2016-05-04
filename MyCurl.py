#!/usr/bin/python
#coding=utf-8
import StringIO
import urllib
import pycurl
import json

import MyEnv

'''
Created on 2016-4-27
@author: Michael Yu
'''

################# MyCurl Class
'''MyCurl
Using session token to maintain the session
'''
class MyCurl(object):
    def __init__(self, url):
        self.url = MyEnv.urlprefix + url;
        
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
        self.setopt_()
        self.myc.setopt(pycurl.POSTFIELDS, json.dumps(jsondata))
        
        buf = StringIO.StringIO()
        self.myc.setopt(pycurl.WRITEFUNCTION, buf.write)
        self.myc.perform()
        response = buf.getvalue()
        buf.close()
        
        return response
    
    def post_2(self, urlpostfix, jsondata):
        self.myc.setopt(pycurl.SSL_VERIFYPEER, False)
        self.myc.setopt(pycurl.HTTPHEADER, self.headers)
        self.myc.setopt(pycurl.URL, str(self.url+urlpostfix))
        self.myc.setopt(pycurl.POSTFIELDS, json.dumps(jsondata))
        
        buf = StringIO.StringIO()
        self.myc.setopt(pycurl.WRITEFUNCTION, buf.write)
        self.myc.perform()
        response = buf.getvalue()
        buf.close()
        
        return response
    
    def postInParams(self, data):
        self.setopt_()
        self.myc.setopt(pycurl.POSTFIELDS, urllib.urlencode(data))
        
        buf = StringIO.StringIO()
        self.myc.setopt(pycurl.WRITEFUNCTION, buf.write)
        self.myc.perform()
        response = buf.getvalue()
        buf.close()
        
        return response
    
    def get(self, urldata):
        self.myc.setopt(pycurl.SSL_VERIFYPEER, False)
        self.myc.setopt(pycurl.HTTPHEADER, self.headers)
        
        self.myc.setopt(pycurl.URL, urldata)
        
        buf = StringIO.StringIO()
        self.myc.setopt(pycurl.WRITEFUNCTION, buf.write)
        self.myc.perform()
        response = buf.getvalue()
        buf.close()
        
        return response
    
################# Frequently Used Object Samples
login_C = MyCurl("/1.1/login")
user_info_C = MyCurl("/1.1/functions/user_info")
users_C = MyCurl("/1.1/users")
#########################################

def demo_login_userinfo():
    res = login_C.post({"username":"user00001@may.event","password":"12345678"})
    resjson = json.loads(res)
    print resjson['sessionToken']
    
    user_info_C.add_sessiontoken_to_headers(resjson['sessionToken'])
    user_info_C.showheaders()
    res = user_info_C.post({"userId":"56c7d005d342d300543379e2"})
    resjson = json.loads(res)
    print resjson
    
    
if __name__=='__main__':
    demo_login_userinfo()
    