#! /usr/bin/python2.7
# -*-coding:Utf-8 -*
#
#
# copyright Thomas Nunes <thomasnds.github.io>
# License MIT
#############################################################

from engine.page import *
from engine.template import *
import datetime
 
 
projects = Category("projects")

testexp = Project("test","description",True)
testexp.dateStart = datetime.date(2002, 3, 11)
projects.addElement(testexp)

testexp = Project("test2","description",True)
testexp.dateStart = datetime.date(2003, 3, 11)
projects.addElement(testexp)

