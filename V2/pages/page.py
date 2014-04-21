#! /usr/bin/python3.4
# -*-coding:Utf-8 -*
#
#
# copyright Thomas Nunes <thomasnds.github.io>
# License MIT
#############################################################

import string
import datetime

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

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.id = self.name2id(name)

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

    def __init__(self, name, description):
        AbstractElement.__init__(self, name, description)
    
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
            res += '''<p><a class="btn btn-default" href="#" role="button">More »</a></p>'''
            
        res += """</div><!--/span-->"""
        return res
    
class Section(AbstractElement):
    def __init__(self, name, description, menu):
        AbstractElement.__init__(self, name, description)
        self.menu = menu
    
    def getMenu(self):
        return self.menu