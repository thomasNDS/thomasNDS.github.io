#! /usr/bin/python3.4
# -*-coding:Utf-8 -*
#
# Static blog generator
#
# copyright Thomas Nunes <thomasnds.github.io>
# License MIT
#########################################################################

import os
import sys
import cssmin
from package import *
from engine import *
from engine.template import *
from engine.page import *
from engine import skills
from engine import xmlParser

############################-Minification-###############################

##
# all files must be closed
def uglifyFiles(minify=True):

    # Merge all css files
    cssConcat = ""
    for css in css2min:
        cssConcat += cssmin.cssmin(open(css, "r").read())
    open(path2cssMin, "w").write(cssConcat)
    if minify:
        os.system("./bin/minify " + path2cssMin )

    # Merge all js files
    jsConcat = ""
    for js in js2min:
        jsConcat += open(js, "r").read()
    open(path2jsMin, "w").write(jsConcat)
    if minify:
        os.system("./bin/minify " + path2jsMin )    
    
    folders2min = ["formations/","skills/","experiences/", "projects/"] + html2min
    if minify: 
        for html in folders2min:
            os.system("./bin/minify " + html )

############################-Manage Args-###############################
import getopt
##
def cleanAll():
    os.system("rm -rf *.pyc engine/*.pyc")
    os.system("rm -rf public/js/src/*-min.js")
    os.system("rm -rf *.html blog/*.html experiences/*.html formations/*.html skills/*.html projects/*.html public/gen/*.html")
##
def cleanMrProper():
    cleanAll();
    os.system("rm -rf __pycache__ engine/__pycache__")

##
minify = False
try:
   opts, args = getopt.getopt(sys.argv[1:],"cpm",["clean","proper", "minify"])
except getopt.GetoptError:
   print (''' -c [--clean] clean option
   -p [--proper] Mr proper option, clean and delete cache
   -m minify all''')
   sys.exit(2)
   
for opt, arg in opts:
   if opt in ("-c", "--clean"):
      print("clean")
      cleanAll()
      sys.exit()
   elif opt in ("-p", "--proper"):
      print("proper")
      cleanMrProper()
      sys.exit()
   elif opt in ("-m", "--minify"):
      minify = True

############################-Create pages-###############################

xmlParser = xmlParser.XmlParser()
experiences = xmlParser.createExperiences()
projects = xmlParser.createProjects()
formations = xmlParser.createFormations()
skills = xmlParser.createSkills()

# Create a start page (index)
indexPage = Page('index.html',
                "Thomas Nunes website","Personnal website of Thomas Nunes. thomasNDS",
                startHeaderHtml="engine/components/header.html" )

# Create the menu ###########################
menu = Menu()
# Skill
menu.addSubMenu(skills.name, skills.id, [])
# Project
nameSub, idSub, elts = projects.getMenu()
menu.addSubMenu(nameSub, idSub, elts)
# Exp
nameSub, idSub, elts = experiences.getMenu()
menu.addSubMenu(nameSub, idSub, [])
# Formations
nameSub, idSub, elts = formations.getMenu()
menu.addSubMenu(nameSub, idSub, [])

# Build the page ###########################
indexPage.write(str(menu))
# Skills
indexPage.write(str(skills))
# Projectexperiences
indexPage.write(str(projects))
# EXP
indexPage.write(str(experiences))
# Formations
indexPage.write(str(formations))
# Contact
indexPage.addSectionHtml("engine/components/contact.html")
# Footer
indexPage.addSectionHtml("engine/components/footer.html")

indexPage.close()
uglifyFiles(minify)
