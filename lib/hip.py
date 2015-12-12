#!/usr/bin/env python

from vlib import db

from sms import Sms

class Hip(object):

    def __init__(self):
        self.sms = Sms()

    def inspire(self):
        quote = Inspiration().getNext()
        print quote
        for soul in Folks().getActive():
            phone = soul['phonenumber']
            print phone
            #self.sms.send(phone, quote)


class Folks(object):

    def __init__(self):
        self.db = db.getInstance()

    def getActive(self):
        sql = 'select * from folks where active = 1'
        return self.db.query(sql)

class Inspiration(object):
    def __init__(self):
        self.db = db.getInstance()

    def getNext(self):
        sql = 'select * from inspiration where sent is null order by id limit 1'
        return self.db.query(sql)[0]['quote']
    
        
        
if __name__ == '__main__':
    Hip().inspire()
