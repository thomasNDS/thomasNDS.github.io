#! /usr/bin/python
# -*-coding:Utf-8 -*
#
#
# copyright Thomas Nunes <thomasnds.github.io>
# License MIT
#############################################################

from engine.page import *
from engine.template import *
import datetime

###############################################
# Page 
#
# -path : (string) path of the new page
# -title : the tile of the page <title>
# -description : the description of the page <meta> 
# -fil : (FilsAriane) the fil d'ariane
###############################################
class PageFormation(AbstractPageStandAlone):
    def __init__(self, path, title, descr):
        AbstractPageStandAlone.__init__(self, path, title, descr)
    
    def setFilArianne(self):
        self._filArianne = FilsAriane([("Formations", "../formations", ""), (self.title, "#", "") ]) 

###############################################
# Formation object
#
### HERITAGE ###
# name (string)
# description (string)
# ownPage (Page)
# id (String)
### LOCAL ###
# _siteWeb (String)
# _logoPath (String)
# page (Page)
# dateStart (datetime)
# dateEnd (datetime)
###############################################
class  Formation(AbstractElement):
    name = None
    description = None
    dateStart = None
    dateEnd = None
    id = None
    
    # name (string)
    # description (string)
    #@option ownPage (Page) [False]
    # _siteWeb (String)
    def __init__(self, name, description, image ="", ownPage = False, _siteWeb = ("#","fr")):
        AbstractElement.__init__(self, name, description, ownPage)
        self._logoPath = image
        self._siteWeb =  _siteWeb

    # create a page for the formation
    def createOwnPage(self):
        path = "formations/" + self.name.lower() + ".html"
        self.page = PageFormation(path, self.name, self.description)
        self.page.close()
    
    def __str__(self):
        #thumbnail  ---------------------------
        res= '<div id="' + self.id + '''" class="col-6 col-sm-6 col-lg-4 element">
        <div class="thumbnail thumbnail-formations">
           <div class="formations-img-content"><img class= "img-rounded exp-img" alt="logo formation" src="''' + self._logoPath + '''"></div>
           <div class="caption text-center">
            <h3 class="element-title">''' + self.name + '''</h3>
              <p class="element-description">''' + self.description + ''' </p>
              <p class="element-date"><span class="start-date">'''
        #DATE  ---------------------------    
        if self.dateStart and self.dateEnd:
            if self.dateStart.year == self.dateEnd.year:    
                res += self.dateStart.strftime("%Y")
            else:
                res+= self.dateStart.strftime("%Y") + """</span> - <span class="end-date">""" + self.dateEnd.strftime("%Y")
        else: 
            if self.dateStart:
                res += self.dateStart.strftime("%Y") + """- Now"""
        res += '''</span></p>'''
        
        #BUTTON CORNER  ---------------------------
        res += '''<div class="text-corner-right">
                     <span class="button-bar-thumbnail"><a target="_blank" class="btn btn-default" href="''' + self._siteWeb[0] + '''" role="button">website'''
        if self._siteWeb[1] != "en":
            res += "[FR]"
        res+= ''' »</a></span> 
                     <span><a target="_blank" class="btn btn-info" href="''' + self.page.path + '''" role="button">More »</a>
                    </span></div>'''  
        res += """
                </div><!--/caption-->
            </div><!--/tumbnail-->
        </div><!--/element-->"""
        return res
    
    
###############################################
# A formation category
#
# name (string)
# _elements ([AbstractElement])
###############################################
class FormationCategory(AbstractCategory):
    
    # name (string)
    def __init__(self, name):
        AbstractCategory.__init__(self, name)
        
    def __str__(self):
        list = self._elements
        res = '''<div id="formation-container" class="category grey-back">
                    <div class="container container-part">
                        <h1 class="title-section" id="''' + self.id +'''">
                        <a href="#formation-container" class="anchor">
                        <span class="hidden-xs glyphicon glyphicon-link"></span></a>
                        ''' + self.name + '</h1>' + """
                        <div class="col-xs-12 col-sm-9">""" 
        list.sort(key=lambda x: x.dateStart, reverse=True)
        for elt in list:
                res += str(elt)
        res += """      </div><!--/col-->"""
            ################
        res += """  </div><!--/container-->
                </div><!--/category-->
             """
        return res
    
###############################################

formations = FormationCategory("Formation")

#POLYTECH
testexp = Formation("Enginneering diploma",
"school enginneer Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmo",
"./public/img/formations/polytech.png",
True,
("http://www.polytech-grenoble.fr/","fr"))

testexp.dateStart = datetime.date(2011, 1, 1)
testexp.dateEnd = datetime.date(2014, 1, 1)
formations.addElement(testexp)

#IAE
testexp = Formation("M2 management","school enginneer Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmo",
"./public/img/formations/iae-rect.png",True,("http://www.iae-grenoble.fr/business-school-grenoble.html",'en'))
testexp.dateStart = datetime.date(2013, 1, 1)
testexp.dateEnd = datetime.date(2015, 1, 1)
formations.addElement(testexp)

#MIAGE
testexp = Formation("MIAGE","L2 Université Joseph Fourrier Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmo",
"./public/img/exps/ujf.gif",True,("http://dlst.ujf-grenoble.fr/index.php?module=parcours&idParcours=52#parcourstop",'fr'))
testexp.dateStart = datetime.date(2009, 1, 1)
testexp.dateEnd = datetime.date(2011, 1, 1)
formations.addElement(testexp)

