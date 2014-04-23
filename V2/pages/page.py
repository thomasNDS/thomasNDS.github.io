#! /usr/bin/python3.4
# -*-coding:Utf-8 -*
#
#
# copyright Thomas Nunes <thomasnds.github.io>
# License MIT
############################################################

import string
import datetime


#########################################################################
# Page object
#
# -path : (string) path of the new page
# -title : the tile of the page <title>
# -descr : the description of the page <meta> 
#########################################################################
class Page:
    # Files imported
    doctype = (open("templates/doctype.html", "r")).read()
    importJSHtml = (open("templates/importsJS.html", "r")).read()
    importCSSHtml = (open("templates/importsCSS.html", "r")).read()

    def __init__(self, path, title, descr, header = ""):
        self.file = open(path, "w")
        self.description = descr
        self.path = path
        self.title = title
        self.setHeader(header)
    
    def setHeader(self, header):
        self.write (self.doctype)
        self.write( self.description + '">')
        self.write("<title>"+ self.title + "</title>")
        if header == "":
            self.write(self.importJSHtml + self.importCSSHtml + "</head><body data-spy='scroll' data-target='#affix-nav'><div id='wrap'>")
            self.write('''<div id="main" class=""><p class="pull-right visible-xs">
        <button type="button" class="btn btn-primary btn-xs" data-toggle="offcanvas">Toggle nav</button></p>''')
        else:
            self.write(header)
        
    def write(self,content):
        self.file.write(content)
        
    # Add html file to the content
    # pathSection (String) path of a html file
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
###############################################
class AbstractElement:

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
        print "createOwnPage not yet defined"
    
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
class Category(AbstractElement):
    _elements= []
    
    def __init__(self, name):
         AbstractElement.__init__(self, name, "")
    
    #elt (AbstractElement)
    def addElement(self,elt):
        self._elements.append(elt)
        
    # @return [AbstractElement]
    def getElementsWithOwnPage(self):
        res = []
        for elt in self._elements:
            if elt.ownPage:
                res.append(elt.path2page)
        return res
        
    def __str__(self, list= _elements):
        res = '<h1 class="title-section" id="'+ self.id +'">' + self.name + '</h1>' + """<div class="container">
                  <div class="">
                   <div class="col-xs-12 col-sm-9">""" 
        listOfYears = self.getListOfYear()
        for date in listOfYears:
            ################         
            res+= '     <h2>' + date.strftime("%Y") + '</h2>'
            res+= '     <div class="row">'
            for elt in list:
                if elt.dateStart.year == date.year:
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
        return (self.name, self.id, res)
    
    def getListOfYear(self):
        res = set()
        for elt in self._elements:
            if elt.dateStart:
                res.add(elt.dateStart)
        return sorted(res)

    
###############################################
# An experience Object
#
# name (string)
# description (string)
# dateStart (Date): the start date of experience
# dateEnd (Date) :  the end date of experience
# location ([Object Places]) :  Where is the experience
# _entreprise (Object Entreprise) :  the entreprise
###############################################
class Project(AbstractElement):
    name = None
    description = None
    dateStart = None
    dateEnd = None
    id = None

    def __init__(self, name, description, ownPage = False):
        AbstractElement.__init__(self, name, description, ownPage)
    
    def createOwnPage(self):
        self.path2page = "projects/" + self.name + ".html"
        self.page = PageProject(self.path2page, self.name, self.description)
        self.page.close()
    
    def __str__(self):
        res= "<div id='" + self.id + """' class="col-6 col-sm-6 col-lg-4 element">
            <h3 class="element-title">""" + self.name + """</h3>
              <p class="element-description">""" + self.description + """ </p>"""
        
        if self.dateStart and self.dateEnd:
            res+= """<p class="element-date"><span class="start-date">
            """ + self.dateStart + """</span> - <span class="end-date">""" + self.dateEnd +"""</span></p>"""
        else: 
            if self.dateStart:
                res+= """<p class="element-date"><span class="start-date">
                """ + self.dateStart.strftime("%m/%Y") + """</span></p>"""
            res += '<p><a class="btn btn-default" href="' + self.path2page + '" role="button">More »</a></p>'
            
        res += """</div><!--/span-->"""
        return res
 
class PageProject(Page):
    def __init__(self, path, title, descr):
        header = '''<link rel="stylesheet" type="text/css" href="../public/gen/min.css" media="all" />
        <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js"></script>
        <script type="text/javascript" src="../public/gen/min.js"></script></head>
        <body data-spy='scroll' data-target='#affix-nav'><div id='wrap'>'''
        Page.__init__(self, path, title, descr, header)
        self.write("<h1 id='title-subpage'>" + self.title + '</h1><div class="container">')
        self.write(self.description + '</div>')
        self.fil= FilsAriane([("Projects", "../projects", ""), (self.title, "#", "") ]) 
        self.write(str(self.fil))

###############################################
#
#
###############################################
class FilsAriane:
    
    def __init__(self, sections):
        self._sections = sections
    
    def __str__(self):
        res = '''<ol class="breadcrumb breadcrumb-arrow">
                  <li><a href="#"><i class="glyphicon glyphicon-home"></i> Home</a></li>'''
        for section in self._sections :
            res += '<li><a href="' + section[1] + '"><i class="glyphicon '+ section[2] +'"></i>' + section[0] + '</a></li>'
        res += '</ol>'
        return res
    
###############################################
# A section (part of page) class
#
# name (string)
# description (string)
# menu ([String]) list of subtitles to include in a menu
###############################################
class Section(AbstractElement):
    def __init__(self, name, description, menu):
        AbstractElement.__init__(self, name, description)
        self.menu = menu
    
    def getMenu(self):
        return self.menu
