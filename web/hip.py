#!/usr/bin/env python

from vweb.htmlpage import HtmlPage
from vweb.html import *

class Hip(HtmlPage):

    def getHtmlContent(self):
        return \
            self.getHeader() + \
            self.getBody() + \
            self.getFooter()

    def getHeader(self):
        return center(h3('Hip Hop Inspiration'))

    def getBody(self):
        return center(p('Sign up here') + \
                          'Email: ' + input(name='name'))

    def getFooter(self):
        return ''

if __name__ == '__main__':
    Hip().go()
