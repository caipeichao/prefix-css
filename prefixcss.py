#!/usr/bin/python

import sys
import pprint
import re

USAGE = '''
prefixcss <file> <css-class>
'''

def main(file, wrapclass):
    with open(file, 'rb') as f:
        css = f.read()
        css = css.decode('utf8')
    result = prefixcss(css, wrapclass)
    print result

def prefixcss(css, wrapclass):
    RULE = '[^{}@]*{[^{}]*?}'
    matches = list(re.finditer(RULE, css))
    for e in reversed(matches):
        rule = css[e.start():e.end()]
        rule = stripcomment(rule)
        rule = processrule(rule, wrapclass)
        css = strreplace(css, e.span(), rule)
    return css
    
def processrule(rule, wrapclass):
    rule = rule.strip()
    bracepos = rule.index('{')
    body = rule[bracepos:]
    selector = rule[:bracepos]
    selector = selector.split(',')
    selector = [wrapclass + ' ' + e.strip() for e in selector]
    selector = ','.join(selector)
    return selector + body

def strreplace(s, (start, end), dst):
    return s[:start] + dst + s[end:]
    
def stripcomment(css):
    COMMENT = '/\*.*?\*/'
    return regexreplace(css, COMMENT, ' ')
    
def regexreplace(css, regex, replacement):
    matches = list(re.finditer(regex, css))
    for e in reversed(matches):
        css = strreplace(css, e.span(), replacement)
    return css

def oneline(css):
    SPACE = '\s+'
    return regexreplace(css, SPACE, ' ')

if __name__ == '__main__':
    try:
        main(*sys.argv[1:])
    except TypeError as ex:
        print 'Not enough argument'
        print USAGE
