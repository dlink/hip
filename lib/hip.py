#!/usr/bin/env python

from datetime import datetime

from vlib import db

from cli import CLI
from sms import Sms

class HipError(Exception): pass

class Hip(object):

    def __init__(self):
        self.sms = Sms()

    def run(self):
        commands = ['inspire']
        self.cli = CLI(self.process, commands)
        print self.cli.process()

    def process(self, *args):
        args = list(args)

        cmd = args.pop(0)
        if cmd == 'inspire':
            self.inspire()
        else:
            raise HipError('Unrecognized command: %s' % cmd)

    def inspire(self):
        inspiration = Inspiration()
        quote = inspiration.getNext()
        print quote['quote']
        for soul in Folks().getActive():
            phone = soul['phonenumber']
            print phone
            self.sms.send(phone, quote['quote'])
        inspiration.setSentDate(quote['id'], datetime.now())

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
        return self.db.query(sql)[0]
    
    def setSentDate(self, id, date):
        sql = "update inspiration set sent = '%s' where id = %s" % (date, id)
        self.db.execute(sql)

if __name__ == '__main__':
    Hip().run()
