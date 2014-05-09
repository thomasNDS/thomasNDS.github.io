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
class PageExperience(AbstractPageStandAlone):
    def __init__(self, path, title, descr):
        AbstractPageStandAlone.__init__(self, path, title, descr)
    
    def setFilArianne(self):
        self._filArianne= FilsAriane([("Experiences", "../experiences", ""), (self.title, "#", "") ]) 


###############################################
#
###############################################
class  Experience(AbstractElement):
    name = None
    description = None
    dateStart = None
    dateEnd = None
    id = None
    logoPath = None
    
    def __init__(self, name, description, ownPage = False, logo = ""):
        AbstractElement.__init__(self, name, description, ownPage)
        self.logoPath = logo
    
    #
    def createOwnPage(self):
        path = "experiences/" + self.name.lower() + ".html"
        self.page = PageExperience(path, self.name, self.description)
        self.page.close()
    
    def __str__(self):
        res= '<div id="' + self.id + '''" class="col-6 col-sm-6 col-lg-4 element-frame">
               <h3 class="element-title">''' + self.name + '''</h3>
               <div class="exp-img-content">
                    <img class= "img-rounded exp-img" alt="logo company" src="''' + self.logoPath + '''"/>
                </div>
               <p class="element-date"><span class="start-date">'''
              
        if self.dateStart and self.dateEnd:
            if self.dateStart.year == self.dateEnd.year:    
                res += self.dateStart.strftime("%Y")
            else:
                res+= self.dateStart.strftime("%Y") + """</span> - <span class="end-date">""" + self.dateEnd.strftime("%Y")
        else: 
            if self.dateStart:
                res += self.dateStart.strftime("%Y") + """- Now"""
        res += '''</span></p>
                    <p class="text-corner-right"><a class="btn btn-info" target="_blank" href="''' + self.page.path + '" role="button">More »</a></p>'
        res += """</div><!--/span-->"""
        return res

###############################################
#
###############################################
class ExperienceCategory(AbstractCategory):
    def __init__(self, name):
        AbstractCategory.__init__(self, name)

    def __str__(self):
        list = self._elements
        res = '''<div class="category"><div class="container container-part">
                    <h1 class="title-section" id="''' + self.id +'''">
                    <a href="#''' + self.id + '''" class="anchor"><span class="hidden-xs glyphicon glyphicon-link"></span></a>
                    ''' + self.name + '</h1>' + """
                    <div class="col-xs-12 col-sm-9">
                     """ 
        list.sort(key=lambda x: x.dateStart, reverse=True)
        for elt in list:
                res += str(elt)
        res += """  </div><!--/row-->"""
            ################
        res += """</div><!--/span-->
               </div><!--/row-->
             </div>"""
        return res

###############################################
 
