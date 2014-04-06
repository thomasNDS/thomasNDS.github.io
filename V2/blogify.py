#! /usr/bin/python2.7
# -*-coding:Utf-8 -*
#
# Static blog generator
#
# copyright Thomas Nunes <thomasnds.github.io>
# License MIT

import os
import sys
import package

if len(sys.argv) > 2:
    print sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
    city = sys.argv[1]
    argument = sys.argv[2]

#Files imported
doctype = (open("templates/doctype.html", "r")).read()
headerHtml = (open("templates/header.html", "r")).read()
importJSHtml = (open("templates/importsJS.html", "r")).read()
importCSSHtml = (open("templates/importsCSS.html", "r")).read()
footerHtml = (open("templates/footer.html", "r")).read()

#page object
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
        self.write(importJSHtml + importCSSHtml+ "</head><body><div id='wrap'>")
        self.write(headerHtml)
        
    def write(self,content):
        self.file.write(content)
    
    def close(self):
        self.write(footerHtml)
        self.file.close()
        print self.path, "page saved !"


indexHtml = Page('indexbis.html',"Thomas Nunes website","Personnal website of Thomas Nunes. thomasNDS")
indexHtml.write("hello world ! ")
indexHtml.close()

for file in file2min:
    output = file.replace(".","-min.")
    os.system("./bin/jsmin <" + file + " >" + output)

cssConcat = ""
for css in css2min:
    css = css.replace(".","-min.")
    cssConcat += open(css, "r").read()
# open(css, "r").write


#Delete file generated
os.system("rm indexbis.html")