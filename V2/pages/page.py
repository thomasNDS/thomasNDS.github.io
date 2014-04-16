#! /usr/bin/python2.7
# -*-coding:Utf-8 -*
#
#
# copyright Thomas Nunes <thomasnds.github.io>
# License MIT
#############################################################


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
# An experience Object
#
# name (string)
# description (string)
# location ([Object Place]) :  Where is the experience
# website (String)
###############################################
class Entreprise:
    website = None 
    location = None
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def getShortDescription(self):
        res = self.name + " - " + self.description
        return res

###############################################
# An Abstract Element
#
# name (string)
# _elements ([AbstractElement])
###############################################
class Category:
    _elements= []
    
    def __init__(self, name):
         self.name = name
    
    #elt (AbstractElement)
    def addElement(self,elt):
        _elements.append(elt)
        
    def __str__(self):
        res = ""
        for elt in _elements:
            res += elt
        return res

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
    
    def __str__(self):
        res= """<div class="col-6 col-sm-6 col-lg-4 element">
            <h2 class="element-title">""" + self.name + """</h2>
              <p class="element-description">""" + self.description + """ </p>"""
        res += """<p><a class="btn btn-default" href="#" role="button">More »</a></p></div><!--/span-->"""
        return res

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
class Experience(AbstractElement):
    name = None
    description = None
    dateStart = None
    dateEnd = None
    location = None
    _entreprise = None

    def __init__(self, name, description):
        AbstractElement.__init__(self, name, description)

    # entreprise: (Object Entreprise)
    def setEntreprise(self,entreprise):
        self._entreprise = entreprise
    
    def __str__(self):
        res= """<div class="col-6 col-sm-6 col-lg-4 element">
            <h2 class="element-title">""" + self.name + """</h2>
              <p class="element-description">""" + self.description + """ </p>"""
        
        if self._entreprise:
            res+="""<p class="entreprise">""" + self.entreprise.getShortDescription() + """</p>"""
        
        if self.dateStart and self.dateEnd:
            res+= """<p class="element-date"><span class="start-date">
            """ + self.dateStart + """</span> - <span class="end-date">""" + self.dateEnd +"""</span></p>"""
        else: 
            if self.dateStart:
                res+= """<p class="element-date"><span class="start-date">
                """ + self.dateStart + """</span></p>"""
        
        res += """<p><a class="btn btn-default" href="#" role="button">More »</a></p></div><!--/span-->"""
        return res
    
###############################################
# A skill
#
# name (string)
# description (string)
###############################################
class Skill(AbstractElement):

    def __init__(self, name, description):
        AbstractElement.__init__(self, name, description)
    
    def __str__(self):
        res= """<div class="col-6 col-sm-6 col-lg-4 element">
            <h2 class="element-title">""" + self.name + """</h2>
              <p class="element-description">""" + self.description + """ </p>"""
        res += """<p><a class="btn btn-default" href="#" role="button">More »</a></p></div><!--/span-->"""
        return res