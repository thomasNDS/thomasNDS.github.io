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
from pages import *
#from project import *
#from skill import *
from pages.template import *
from pages.page import *
from pages import skills
from pages import project

############################-Minification-###############################
def minifyFiles():
    # Minify all files
    for file in file2min:
        if file != "index-orig.html":
            output = file.replace(".","-min.")
        else:
            output = "index.html"
        os.system("./bin/jsmin <" + file + " >" + output)

    # Merge all css files
    cssConcat = ""
    for css in css2min:
        cssConcat += cssmin.cssmin(open(css, "r").read())

    open(path2cssMin, "w").write(cssConcat)

    # Merge all js files
    jsConcat = ""
    for js in js2min:
        js = js.replace(".","-min.")
        jsConcat += open(js, "r").read()
    open(path2jsMin, "w").write(jsConcat)
    print "all files minified !"


############################-Create pages-###############################

#need arguments ?
if len(sys.argv) > 2:
    print sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
    city = sys.argv[1]
    argument = sys.argv[2]

# Create a start page (index)
indexPage = Page('index-orig.html',"Thomas Nunes website","Personnal website of Thomas Nunes. thomasNDS")

# Create the menu
menu = Menu()

menu.addSubMenu(skills.skills.name, skills.skills.id, skills.skills.getMenu())

nameSub, idSub, elts = project.projects.getMenu()
menu.addSubMenu(nameSub, idSub, elts)

# Build the page
indexPage.addSectionHtml("pages/components/header.html")
indexPage.write(str(menu))
indexPage.write(str(skills.skills.description))
indexPage.write(str(project.projects))
indexPage.addSectionHtml("pages/articles/testArticle.html")
indexPage.addSectionHtml("pages/components/contact.html")
indexPage.addSectionHtml("pages/components/footer.html")

indexPage.close()
minifyFiles()
