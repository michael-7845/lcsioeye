#!/usr/bin/python
#coding=utf-8
import StringIO
import pycurl
import json

import MyEnv

'''
Created on 2016-4-27
@author: Michael Yu
'''

################# MyCurl Class
'''MyCurl3
Using master key
'''
class MyCurl3(object):
    def __init__(self, url):
        self.url = MyEnv.urlprefix + url;
        
        self.headers = ["Content-Type: application/json; charset=utf-8", 
                        MyEnv.header_appid, 
                        MyEnv.header_masterkey, 
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
    
################# Frequently Used Object Samples
send_message_C = MyCurl3("/1.1/rtm/messages")
#########################################

def demo_send_message():
    send_message_C.showheaders()
    res = send_message_C.post({"from_peer": "5715f727ebcb7d005fab60af", 
                         "message": "the second hello from user00002", 
                         "conv_id": "5722ec5d2e958a0065421a5f", 
                         "transient": False})
    print res
    
if __name__=='__main__':
    demo_send_message()
    