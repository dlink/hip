#!/usr/bin/env python

import re 

from vlib import db
from vlib.datatable import DataTable

from vweb.htmlpage import HtmlPage
from vweb.html import *

PHONE_NUMBER_REGEX = r'(^[+0-9]{1,3})*([0-9]{10,11}$)'

class Hip(HtmlPage):

    def __init__(self):
        HtmlPage.__init__(self, 'hip')
        self.user_msg = ''
        self.user_error_msg = ''

    def process(self):
        HtmlPage.process(self)

        if 'phonenumber' in self.form:
            phonenumber = self.form['phonenumber'].value
            if not re.match(PHONE_NUMBER_REGEX, phonenumber):
                self.user_error_msg = 'Invalid Phone Number: %s ' % phonenumber
            else:
                folks = DataTable(db.getInstance(), 'folks')
                folks.insertRow({'phonenumber': phonenumber,
                                 'active': 1})
                self.user_msg = "Okay - congrats - you've been added (%s)" \
                    % phonenumber
        
    def getHtmlContent(self):
        return \
            self.getHeader() + \
            self.getUserMsg() + \
            self.getBody() + \
            self.getFooter()

    def getHeader(self):
        return center(h3('Hip Hop Inspiration'))

    def getUserMsg(self, error=0):
        user_msg = center(div(self.user_msg,
                              style='background-color: yellow'))
        error_msg = center(div(self.user_error_msg,
                               style='background-color: red'))
        return user_msg + \
            error_msg
                       
    
    def getBody(self):
        return center(p('Sign up here') + \
                          p('Phone Number: ' + input(name='phonenumber')) + \
                          input(type='submit'))

    def getFooter(self):
        return ''

if __name__ == '__main__':
    Hip().go()
