#!/usr/bin/python

import io
import sys
from django.core.management import run_command

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<body>'
run_command('test')
print '</body>'
print '</html>'
