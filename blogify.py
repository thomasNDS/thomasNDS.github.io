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
from engine import project
from engine import experience
from engine import formation

############################-Minification-###############################
def minifyFiles():
    # Minify all files
    for file in file2min:
        # test if allready minified
        if not (("-min" in file) or (".min" in file)):
            #if minify without "-min"
            if "-orig" in file:
                output = file.replace("-orig.",".")
            else:
                output = file.replace(".","-min.")
            os.system("./bin/jsmin <" + file + " >" + output)

    # Merge all css files
    cssConcat = ""
    for css in css2min:
        cssConcat += cssmin.cssmin(open(css, "r").read())

    open(path2cssMin, "w").write(cssConcat)

    # Merge all js files
    jsConcat = ""
    for js in js2min:
        if (not (("-min" in js) or (".min" in js))) :
            js = js.replace(".","-min.")
        jsConcat += open(js, "r").read()
    open(path2jsMin, "w").write(jsConcat)
    print "all files minified !"


############################-Create pages-###############################

# Need arguments ?
if len(sys.argv) > 2:
    print sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
    city = sys.argv[1]
    argument = sys.argv[2]

# Create a start page (index)
indexPage = Page('index-orig.html',
                "Thomas Nunes website","Personnal website of Thomas Nunes. thomasNDS",
                startHeaderHtml="engine/components/header.html" )

# Create the menu ###########################
menu = Menu()
# Exp
nameSub, idSub, elts = experience.experiences.getMenu()
menu.addSubMenu(nameSub, idSub, [])
# Formations
nameSub, idSub, elts = formation.formations.getMenu()
menu.addSubMenu(nameSub, idSub, [])
# Skill
menu.addSubMenu(skills.skills.name, skills.skills.id, [])
# Project
nameSub, idSub, elts = project.projects.getMenu()
menu.addSubMenu(nameSub, idSub, elts)

# Build the page ###########################
indexPage.write(str(menu))
# EXP
indexPage.write(str(experience.experiences))
# Formations
indexPage.write(str(formation.formations))
# Skills
indexPage.write(str(skills.skills))
# Project
indexPage.write(str(project.projects))
indexPage.write("<div class='separate-margin200'></div>")
# Contact
indexPage.addSectionHtml("engine/components/contact.html")
# Footer
indexPage.addSectionHtml("engine/components/footer.html")

# Minify ###########################
file2min += project.projects.getElementsWithOwnPage()
file2min += experience.experiences.getElementsWithOwnPage()
file2min += formation.formations.getElementsWithOwnPage()

indexPage.close()
minifyFiles()
