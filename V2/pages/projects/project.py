#! /usr/bin/python2.7
# -*-coding:Utf-8 -*
#
#
# copyright Thomas Nunes <thomasnds.github.io>
# License MIT
#############################################################

from pages.page import *
from pages.template import *
import datetime
 
 
projects = Category("projects")

testexp = Project("test","description")
testexp.dateStart = datetime.date(2002, 3, 11)
projects.addElement(testexp)

testexp = Project("test2","description")
testexp.dateStart = datetime.date(2003, 3, 11)
projects.addElement(testexp)

