#!/usr/bin/env python

import re 

from vlib import db
from vlib.datatable import DataTable

from vweb.htmlpage import HtmlPage
from vweb.html import *

PHONE_NUMBER_REGEX = r'(^[+0-9]{1,3})*([0-9]{10,11}$)'

class Hip(HtmlPage):

    def __init__(self):
        HtmlPage.__init__(self, 'Motiviz')
        self.style_sheets = ['css/styles.css', 'css/user_message.css']
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
        return '''
    <section id="banner">
      <h1>Motivizzle</h1>
      <h2>Get Your Mental Right. Daily.</h2>
    </section>'''

    def getUserMsg(self, error=0):
        user_msg  = div(self.user_msg,       class_='userMsg')
        error_msg = div(self.user_error_msg, class_='userMsg errorMsg')
        return user_msg + error_msg

    def getBody(self):
        return '''
    <section class="info">
      <h2>Start Your Day Right</h2>
      <p>Get inspirational texts from your favorite rappers. Sign up now.</p>

      <div class="sign-up">
        <div class="phone-form">
            <label class="phone-label icon-phone" for="phone"></label>
          <input type="tel" name="phonenumber" class="phone-input">
        </div>
        <input type="submit" class="submit-btn" value="Sign Up">
      </div>
    </section>'''

    def getFooter(self):
        return ''

if __name__ == '__main__':
    Hip().go()
