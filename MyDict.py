#!/usr/bin/python
#coding=utf-8

'''
Created on 2016-4-27
@author: Michael Yu
'''

class MyDict(dict):
    def __getattr__(self,name):
        if name in self:
            return self[name]
        n=MyDict()
        super(MyDict, self).__setitem__(name, n)
        return n
    def __getitem__(self,name):
        if name not in self:
            super(MyDict, self).__setitem__(name,nicedict())
        return super(MyDict, self).__getitem__(name)
    def __setattr__(self,name,value):
        super(MyDict, self).__setitem__(name,value)

def demo():
    d= MyDict()
    print d
    d.name = "kemin_yu"
    d.my.family = ["lan_zhang, wanyi_yu, douchun_yu, rongfeng_pan, yinglan_wang, youbin_zhang"]
    print d
    d.china.sichuan= 'a'
    print d
    print d['china']
    d['china'].celerity = 7
    print d
    
    print dir(dict)
    print dir(MyDict)
    print dir(MyDict.__dict__)
        
if __name__=="__main__":
   demo()
    