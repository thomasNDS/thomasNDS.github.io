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
# An experience Object
#
# name (string)
# description (string)
# dateStart (Date): the start date of experience
# dateEnd (Date) :  the end date of experience
# location ([Object Places]) :  Where is the experience
# _entreprise (Object Entreprise) :  the entreprise
# page (PageProject) : the page coresponding
###############################################
class Project(AbstractElement):
    name = None
    description = None
    dateStart = None
    dateEnd = None
    id = None

    def __init__(self, name, description, ownPage = False, image=""):
        AbstractElement.__init__(self, name, description, ownPage)
        self._logoPath = image
    
    def setLogoPath(self,path):
        self._logoPath = path
        
    def createOwnPage(self):
        path = "projects/" + self.name.lower() + ".html"
        self.page = PageProject(path, self.name, self.description)
        self.page.close()
    
    def __str__(self):
        #thumbnail  ---------------------------
        res= '<div id="' + self.id + '''" class="col-6 col-sm-6 col-lg-4 element">
        <div class="thumbnail thumbnail-formations">
           '''
        if self._logoPath != "":
            res += '''<div class="formations-img-content">
                        <img class= "img-rounded exp-img" alt="logo formation" src="''' + self._logoPath + '"></div>'
        res +='''
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
                     <span><a target="_blank" class="btn btn-info" href="''' + self.page.path + '''" role="button">More »</a>
                    </span></div>'''  
        res += """
                </div><!--/caption-->
            </div><!--/tumbnail-->
        </div><!--/element-->"""
        return res

###############################################
# Page of a project
#
# -path : (string) path of the new page
# -title : the tile of the page <title>
# -description : the description of the page <meta> 
# -fil : (FilsAriane) the fil d'ariane
###############################################
class PageProject(AbstractPageStandAlone):
    def __init__(self, path, title, descr):
        AbstractPageStandAlone.__init__(self, path, title, descr)
    
    def setFilArianne(self):
        self._filArianne= FilsAriane([("Projets", "../projects", ""), (self.title, "#", "") ]) 


###############################################
#
###############################################
class ProjectCategory(AbstractCategory):
    def __init__(self, name):
        AbstractCategory.__init__(self, name)
    
    def __str__(self):
        list = self._elements
        res = '''
        <div id="project-container" class="category grey-back">
            <div class="container container-part">
                <h1 class="title-section" id="''' + self.id +'''">
                <a href="#project-container" class="anchor">
                <span class="hidden-xs glyphicon glyphicon-link"></span></a>
                ''' + self.name + '</h1>' + """
                <div class="col-xs-12 col-sm-9">""" 
        listOfYears = self.getListOfYear()
        for date in listOfYears:
            ################         
            res+= '     <h2 id="' + self.id + date.strftime("%Y") + '">' + date.strftime("%Y") + '</h2>'
            res+= '     <div class="row">'
            for elt in list:
                if elt.dateStart.year == date.year:
                    res += str(elt)
            res += """  
                </div><!--/col-->"""
            ################
        res += """
            </div><!--/container-->
        </div><!--/category-->
        </div><!--/???projects-->"""
        return res

###############################################

#projects = ProjectCategory("Projects")

#testexp = Project("test","description",True)
#testexp.dateStart = datetime.date(2002, 3, 11)
#projects.addElement(testexp)
#
#testexp = Project("test2","description",True)
#testexp.dateStart = datetime.date(2003, 3, 11)
#projects.addElement(testexp)

    