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
        self.fil= FilsAriane([("Experiences", "../experiences", ""), (self.title, "#", "") ]) 


###############################################
#
###############################################
class  Experience(AbstractElement):
    name = None
    description = None
    dateStart = None
    dateEnd = None
    id = None
    def __init__(self, name, description, ownPage = False):
        AbstractElement.__init__(self, name, description, ownPage)
    
    def createOwnPage(self):
        self.path2page = "experiences/" + self.name + "-orig.html"
        self.page = PageExperience(self.path2page, self.name, self.description)
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
            res += '<p><a class="btn btn-default" href="' + self.path2page.replace("-orig","") + '" role="button">More »</a></p>'
            
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
        res = '''<div class="category"><div class="container">
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

###############################################
 
experiences = ExperienceCategory("Experiences")

exp = Experience("exp1","description",True)
exp.dateStart = datetime.date(2002, 3, 11)
experiences.addElement(exp)

exp2 = Experience("exp2","description",True)
exp2.dateStart = datetime.date(2003, 3, 11)
experiences.addElement(exp2)