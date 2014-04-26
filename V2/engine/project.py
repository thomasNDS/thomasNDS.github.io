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
# path2page (String) : path to the own page
# page (PageProject) : the page coresponding
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
        self.path2page = "projects/" + self.name + "-orig.html"
        self.page = PageProject(self.path2page, self.name, self.description)
        self.page.close()
    
    def __str__(self):
        res= "  <div id='" + self.id + """' class="col-6 col-sm-6 col-lg-4 element">
                    <div class="thumbnail">
                      <div class="caption text-center">
                        <h3 class="element-title">""" + self.name + """</h3>
                        <p class="element-description">""" + self.description + """ </p>"""
        res += '        <p class="text-right"><a class="btn btn-info" href="' + self.path2page.replace("-orig","") + '" role="button">More »</a></p>'    
        res += """    </div> <!--/caption-->
                    </div><!--/thumbnail-->
                </div><!--/element-->   """
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
        self.fil= FilsAriane([("Projets", "../projects", ""), (self.title, "#", "") ]) 


###############################################
#
###############################################
class ProjectCategory(AbstractCategory):
    def __init__(self, name):
        AbstractCategory.__init__(self, name)
    
    def __str__(self):
        list = self._elements
        res = '<div id="projects-category" class="category grey-back"><div class="container"><h1 class="title-section" id="'+ self.id +'">' + self.name + '</h1>' + """
                   <div class="col-xs-12 col-sm-9">""" 
        listOfYears = self.getListOfYear()
        for date in listOfYears:
            ################         
            res+= '     <h2 id="' + self.id + date.strftime("%Y") + '">' + date.strftime("%Y") + '</h2>'
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

###############################################

projects = ProjectCategory("Projects")

testexp = Project("test","description",True)
testexp.dateStart = datetime.date(2002, 3, 11)
projects.addElement(testexp)

testexp = Project("test2","description",True)
testexp.dateStart = datetime.date(2003, 3, 11)
projects.addElement(testexp)

