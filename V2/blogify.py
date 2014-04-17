#! /usr/bin/python2.7
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
from pages.experiences import experience
from pages.template import *

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


#########################################################################
# Page object
#
# -path : (string) path of the new page
# -title : the tile of the page <title>
# -descr : the description of the page <meta> 
#########################################################################
class Page:
    html =  ""
    def __init__(self, path, title, descr):
        self.file = open(path, "w")
        self.desc = descr
        self.path = path
        self.title = title
        self.write (doctype)
        self.write( self.desc + '">')
        self.write("<title>"+ self.title + "</title>")
        self.write(importJSHtml + importCSSHtml+ "</head><body data-spy='scroll' data-target='#affix-nav'><div id='wrap'>")
        self.write('''<div id="main" class=""><p class="pull-right visible-xs">
            <button type="button" class="btn btn-primary btn-xs" data-toggle="offcanvas">Toggle nav</button></p>''')
        
    def write(self,content):
        self.file.write(content)
        
    def addSectionHtml (self, pathSection):
        component = PageSectionHtml(pathSection)
        self.write(component.getHtml())
    
    def close(self):
        self.file.close()
        print self.path, "page saved !"
        
#########################################################################
# Page section object like a header, footer or contact form (html)
#
# -path : (string) the path of the html file 
#########################################################################
class PageSectionHtml:
    def __init__(self,path):
        self.path = path
        self._file = open(path, "r")
        self.content = (self._file).read()
        self._file.close()
        
    def getHtml(self):
        return self.content

#########################################################################
# Page section object like a header, footer or contact form (html)
#
# -path : (string) the path of the html file 
#########################################################################
class PageSection:
    def __init__(self):
        self.path = path
        self._file = open(path, "r")
        self.content = (self._file).read()
        self._file.close()
        
    def getHtml(self):
        return self.content

############################-Create pages-###############################

#need arguments ?
if len(sys.argv) > 2:
    print sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
    city = sys.argv[1]
    argument = sys.argv[2]

# Files imported
doctype = (open("templates/doctype.html", "r")).read()
importJSHtml = (open("templates/importsJS.html", "r")).read()
importCSSHtml = (open("templates/importsCSS.html", "r")).read()

# Create a start page (index)
indexPage = Page('index-orig.html',"Thomas Nunes website","Personnal website of Thomas Nunes. thomasNDS")

# Create the menu
menu = Menu()
nameSub, idSub, elts = experience.experiences.get4menu()
menu.addSubMenu(nameSub, idSub, elts)

# Build the page
indexPage.addSectionHtml("pages/components/header.html")
indexPage.write(str(menu))
indexPage.write(experience.getAll())
indexPage.addSectionHtml("pages/articles/testArticle.html")
indexPage.addSectionHtml("pages/components/contact.html")
indexPage.addSectionHtml("pages/components/footer.html")

indexPage.close()
minifyFiles()

# Delete file generated