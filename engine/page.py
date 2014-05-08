#! /usr/bin/python3.4
# -*-coding:Utf-8 -*
#
# The core page engine
#
# copyright Thomas Nunes <thomasnds.github.io>
# License MIT
############################################################

import string
import datetime

#########################################################################
# Page object
#
# -path : (String) path of the new page
# -title : (String) the tile of the page <title>
# -description : (String) the description of the page <meta> 
# -file : (File) 
#########################################################################
class Page:
    # Files imported
    doctype = (open("templates/doctype.html", "r")).read()
    importJSHtml = (open("templates/importsJS.html", "r")).read()
    importCSSHtml = (open("templates/importsCSS.html", "r")).read()
    
    # path : (String) path of the new page
    # title : (String) the tile of the page <title>
    # @option header : the text enter <head></head> balise
    # @option startHeaderHtml: personnaliled code after <body> balise
    def __init__(self, path, title, descr, header = "", startHeaderHtml=""):
        self.path = path.replace(" ", "-")
        self.file = open(self.path, "w")
        self.description = descr
        self.title = title
        self.setHeader(header,startHeaderHtml)
    
    # header : the text enter <head></head> balise
    # startHeaderHtml: personnaliled code after <body> balise
    def setHeader(self, header, startHeaderHtml):
        self.write (self.doctype)
        self.write( self.description + '">')
        self.write("<title>"+ self.title + "</title>")
        if header == "":
            self.write(self.importJSHtml + self.importCSSHtml + "</head><body data-spy='scroll' data-target='#affix-nav'>")
            if startHeaderHtml != "":
                self.addSectionHtml(startHeaderHtml)
            self.write('''<div id='wrap'><div id="main" class=""><p class="pull-right visible-xs">''')
            #<button type="button" class="btn btn-primary btn-xs" data-toggle="offcanvas">Toggle nav</button></p>
        else:
            self.write(header)

    #addContent    
    def write(self,content):
        self.file.write(content)
        
    # Add html file to the content
    # pathSection (String) path of a html file
    def addSectionHtml (self, pathSection):
        component = PageSectionHtml(pathSection)
        self.write(component.getHtml())
    
    def close(self):
        self.file.close()
   
#########################################################################
# # Independant page
#
# -path : (String) path of the new page
# -title : (String) the tile of the page <title>
# -description : (String) the description of the page <meta> 
# -file : (File) 
#
# -_filArianne : (FilAriane) the fil ariane of the page
#########################################################################
class AbstractPageStandAlone(Page):
    def __init__(self, path, title, descr):
        header = '''<link rel="stylesheet" type="text/css" href="../public/gen/min.css" media="all" />
        <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js"></script>
        <script type="text/javascript" src="../public/gen/min.js"></script></head>
        <body data-spy='scroll' data-target='#affix-nav'><div id='wrap'>'''
        Page.__init__(self, path, title, descr, header)
        self.setFilArianne()
        self.setTitle()
        self.setContent(self.description)
    
    #write the start of the page : title + fil ariane    
    def setTitle(self):
        self.write("<h1 id='title-subpage'>" + self.title + '''</h1><div class="container">
        <div class="row"><div class="col-md-12">''')
        self.write(str(self._filArianne))
    
    def setFilArianne(self):
        self._filArianne= FilsAriane([("Others", "../projects", ""), (self.title, "#", "") ]) 

    def setContent(self, content):
        self.write('</div>' + content + '</div></div></div>')

#########################################################################
# Page section object like a header, footer or contact form (html)
#
# -path : (string) the path of the html file 
# -_file : (File) file source of section
# -content (String) html content
#########################################################################
class PageSectionHtml:
    def __init__(self,path):
        self.path = path
        self._file = open(path, "r")
        self.content = (self._file).read()
        self._file.close()
        
    def getHtml(self):
        return self.content

###############################################
# A location (GPS)
#
# lattitude (string)
# longitude(string)
# name (string)
###############################################
class Place:
    def __init__(self, name, lattitude, longitude):
        self.name = name
        self.lattitude= lattitude
        self.longitude= longitude

###############################################
# An Abstract Element
#
# name (string)
# description (string)
# ownPage (Page)
# id (String)
###############################################
class AbstractElement:
    
    # name (string)
    # description (string)
    # @option ownPage (Page)
    def __init__(self, name, description, ownPage = False):
        self.ownPage = ownPage
        self.name = name
        self.description = description
        self.id = self.name2id(name)
        if ownPage:
            self.createOwnPage()

    # Convert a name (String) to an valid id (String)
    #
    # @param (string) name
    # @return (String) a valid id
    def name2id(self, name):
        id = "no-id"
        if name != "":
            id = name.replace(" ","-")
            id= id.replace("'","-")
            id= id.replace("é","e")
            id= id.replace("è","e")
            id= id.replace("&","-")
            id= id.replace("~","-")
            id= id.replace("ç","c")
            id= id.replace("à","a")
            id= id.replace("ù","u")
            id= id.replace("#","-")
            id= id.replace("?","")
            id= id.replace("!","")
            id= id.replace(",","")
            id= id.replace(";","")
            id= id.replace("/","")
            id= id.replace(":","")
            id= id.replace(".","-")
        return id.lower()
    
    # create a personalised page for this element
    def createOwnPage(self):
        print ("createOwnPage not yet defined")
    
    def __str__(self):
        res= """<div class="col-6 col-sm-6 col-lg-4 element">
            <h2 class="element-title">""" + self.name + """</h2>
              <p class="element-description">""" + self.description + """ </p>"""
        res += """<p><a class="btn btn-default" href="#" role="button">More »</a></p></div><!--/span-->"""
        return res

###############################################
# An category of Abstract Element
#
# name (string)
# _elements ([AbstractElement])
###############################################
class AbstractCategory(AbstractElement):
    _elements= []
    
    def __init__(self, name):
         AbstractElement.__init__(self, name, "")
         self._elements= []
    
    #elt (AbstractElement)
    def addElement(self,elt):
        self._elements.append(elt)
        
    # @return [AbstractElement]
    def getElementsWithOwnPage(self):
        res = []
        for elt in self._elements:
            if elt.ownPage:
                res.append(elt.page.path)
        return res
        
    def __str__(self):
        list = self._elements
        res = '''<div class="category grey-back"><div class="container">
                    <h1 class="title-section" id="''' + self.id +'">' + self.name + '</h1>' + """
                     <div class="col-xs-12 col-sm-9">""" 
        list.sort(key=lambda x: x.dateStart, reverse=True)
        for elt in list:
                res += str(elt)
        res += """  </div><!--/row-->"""
            ################
        res += """</div><!--/span-->
               </div><!--/row-->
             </div>"""
        return res
         
#  get the list of names
#    
#  @return (String, [String]) : name of category and list of elements names
    def getMenu(self):
        res = []
        for elt in self._elements:
            res.append((elt.name,elt.id))    
        return (self.name, self.id, self.getListOfYearsId())
    
    # get the list of years sorted of elements in the category
    #
    # @option sortedReverse : if reverse sorting [True]
    # @return [datetime] : date list
    def getListOfYear(self, sortedReverse= True):
        res = set()
        for elt in self._elements:
            if elt.dateStart:
                res.add(elt.dateStart)
        return sorted(res, reverse=sortedReverse)
    
    def getListOfYearsId(self):
        res = []
        for elt in self.getListOfYear():
            res.append((self.id + elt.strftime("%Y"),(elt.strftime("%Y"))))
        return res


###############################################
# Fils Ariane 
#
# sections ([(String,String,String)]) list of (name, class, link)
###############################################
class FilsAriane:
    
    # sections ([(String,String,String)]) list of (name, class, link)
    def __init__(self, sections):
        self._sections = sections
    
    def __str__(self):
        res = '''<ol class="breadcrumb breadcrumb-arrow"> <!--
            --> <li><a href="#">Home</a></li><!--
            -->'''
        for i in range(0,len(self._sections)-1):
            section = self._sections[i]
            res += '\n <li><a class="elt-arianne" href="' + section[1] + '">' + section[0] + '''</a></li><!--
            -->'''
        section = self._sections[-1]
        res += '<li class="elt-arianne active"><span>' + section[0] + '</span></li> \n'
        res += '</ol>'
        return res
    
###############################################
# A section (part of page) class
#
# name (string)
# description (string)
# menu ([String]) list of subtitles to include in a menu
# _content (String)
###############################################
class Section(AbstractElement):
    _content = ""
    
    # name (string)
    # description (string)
    # menu ([String]) list of subtitles to include in a menu
    def __init__(self, name, description, menu):
        AbstractElement.__init__(self, name, description)
        self.menu = menu
        self._content = ""
    
    def getMenu(self):
        return self.menu
    
    def setContent(self, content):
        self._content = content

    def getContent(self):
        return self._content
    
    def __str__(self):
        return self._content
