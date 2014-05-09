#! /usr/bin/python
# -*-coding:Utf-8 -*
#
#
# copyright Thomas Nunes <thomasnds.github.io>
# License MIT
############################################################
from engine.page import *

###############################################
# Page of a skill
#
# -path : (string) path of the new page
# -title : the tile of the page <title>
# -description : the description of the page <meta> 
# -fil : (FilsAriane) the fil d'ariane
###############################################
class PageSkill(AbstractPageStandAlone):
    def __init__(self, path, title, descr):
        AbstractPageStandAlone.__init__(self, path, title, descr)
    
    def setFilArianne(self):
        self._filArianne= FilsAriane([("Skills", "../projects", ""), (self.title, "#", "") ]) 



###################################################
# Level of a skill, between 1 and 4 (4 is the best)
# 
# level (int) the current level
# normal, medium, good, expert: (int) differents levels
###################################################
class LevelSkill():
    normal = 1
    medium = 2
    good = 3
    expert = 4
    level = 1

    def __init__(self, level= 1):
        self.level = level
    
    # get the css class associated
    def getClass(self):
        if self.level == self.normal:
            return ""
        elif self.level == self.medium:
            return "skill-medium"
        elif self.level == self.good:
            return "skill-good"
        elif self.level == self.expert:
            return "skill-expert"
        return ""
                
###################################################
# A skill
#
# levelSkill (LevelSkill) the level of the skill
# _page (PageSkill)
# _description (String)
# type
# name (String)
###################################################
class SkillElement:
    levelSkill = None
    _page = None
    
    #
    def __init__(self, name, level = 1, description = ""):
        self.type = type
        self.name = name
        self._description = description
        self.levelSkill = LevelSkill(level)
        self.createPage()
    
    #
    def getPagePath(self):
            return self._page.path
        
    def createPage(self):
        path = "skills/" + self.name.replace("/","-").lower() + ".html"
        self._page = PageSkill(path, self.name, self._description)
        
    def __str__(self):
        return """<a target="_blank" href='""" + self.getPagePath() + """' >
                    <div id="content-skills" class='skill-element
                     """+ self.levelSkill.getClass() + """'>
                     """ + str(self.name) + """
                    </div>
                  </a><!--/-->"""
 
###################################################
# A skill subgroup
#
# _skillsElements ([SkillElement]) list of skills
###################################################              
class SubSkillContainer(AbstractElement):
    _skillsElements = []
   
    def __init__(self, name):
        AbstractElement.__init__(self, name, "")
        self._skillsElements = []
 
    # skill (SkillElement)
    def addSkill(self, skill):
        self._skillsElements.append(skill)
    
    #
    def getAllSkillsPath(self):
        res= []
        for skill in self._skillsElements:
            res.append(skill.getPagePath())
        return res
    
    def __str__(self):
        res= """
        <div class="subtitle-section"><h4 class="subtitle-section-title">
        """+ self.name +"</h4>"
        for skill in self._skillsElements:
            res += str(skill)
        res += "</div><!--/span-->"
        return res

###################################################
# A skills global group
#
# _skillsElements ([SkillElement]) list of skills
# _subSkillContainer ([SubSkillContainer]) list of subgroup of skills
###################################################       
class SkillContainer(AbstractElement):
    _subSkillContainer = []
    _skillsElements = []
    
    def __init__(self, name):
        AbstractElement.__init__(self, name, "")
        self._subSkillContainer = []
        self._skillsElements = []
     
    # skill (SubSkillContainer)
    def addSubSkillContainer(self, skill):
        self._subSkillContainer.append(skill)

    # skill (SkillElement)
    def addSkill(self, skill):
        self._skillsElements.append(skill)
        
    def __str__(self):
        res= """
        <div class="col-4 col-sm-6 col-lg-6">
            <h3 id='""" + self.id + """' class="skill-title">""" + self.name + "</h3>" 
        for skill in self._subSkillContainer:
            res += str(skill)
        for skill in self._skillsElements:
            res += str(skill)
        res += "</div><!--/span-->"
        return res
    
    #
    def getAllSkillsPath(self):
        res= []
        for subContainer in self._subSkillContainer:
            res += subContainer.getAllSkillsPath()
            
        for skill in self._skillsElements:
            res.append(skill.getPagePath())
        return res
    
###################################################
# A section (part of page) class
#
# id (string)
# name (string)
# description (string)
# menu ([String]) list of subtitles to include in a menu
# _content (String)
# _skillContainers [SkillContainer]
#
###################################################
class SkillSection(Section):
    _skillContainers = []
    
    def __init__(self, name, description, menu):
        Section.__init__(self, name, description, menu)
        self._skillContainers = []
        
    def addSkillContainer(self, skillContainer):
        self._skillContainers.append(skillContainer)
        
    # @return [AbstractElement]
    def getElementsWithOwnPage(self):
        res = []
        for elt in self._skillContainers:
            res += (elt.getAllSkillsPath())
        return res
    
    def __str__(self):    
        res='''
            <div class="container container-part">
              <div class="category">
                <h1 id="skills" class="title-section">
                <a href="#''' + self.id + '''" class="anchor"><span class="hidden-xs glyphicon glyphicon-link"></span></a>
                ''' + self.name + """</h1>
                    <div class="col-xs-12 col-sm-9 skills-container">
                        <div class="row">"""
        for container in self._skillContainers:
            res += str(container)
        res += """
                        </div><!--/span-->
                    </div><!--/span-->
                </div><!--/row-->
            </div>
        """
        return res
    
####
skills = SkillSection("Skills", "", [("it-skills", "IT Skills"),
                                ("programming", "Programming")])


itSkills = SkillContainer("IT skills")
environement = SubSkillContainer("Tools")
systemes = SubSkillContainer("Systems")
design = SubSkillContainer("Design")

systemes.addSkill(SkillElement("Linux", 4))
systemes.addSkill(SkillElement("MacOS", 1))
systemes.addSkill(SkillElement("Windows", 3))
design.addSkill(SkillElement("Blender",1))
design.addSkill(SkillElement("Photoshop",4))
design.addSkill(SkillElement("Gimp", 2))
environement.addSkill(SkillElement("Eclipse",4))
environement.addSkill(SkillElement("Netbeans",4))
environement.addSkill(SkillElement("Svn",3))
environement.addSkill(SkillElement("Git",4))
environement.addSkill(SkillElement("Mercurial",2))

itSkills.addSubSkillContainer(systemes)
itSkills.addSubSkillContainer(design)
itSkills.addSubSkillContainer(environement)
skills.addSkillContainer(itSkills)
############################################################

programming = SkillContainer("Programming")
programming.addSkill(SkillElement("Java/JEE", 4))
programming.addSkill(SkillElement("OcamL", 1))
programming.addSkill(SkillElement("C/C++", 4))
programming.addSkill(SkillElement("ADA", 1))
programming.addSkill(SkillElement("Perl", 2))
programming.addSkill(SkillElement("Python", 4))
programming.addSkill(SkillElement("C#", 1))
programming.addSkill(SkillElement("Android", 3))
programming.addSkill(SkillElement("Ruby", 1))
programming.addSkill(SkillElement("HTML5", 3))
programming.addSkill(SkillElement("ASP", 1))
programming.addSkill(SkillElement("CSS3", 2))
programming.addSkill(SkillElement("MatLab/Octave", 1))
programming.addSkill(SkillElement("SQL", 4))
programming.addSkill(SkillElement("NoSQL", 2))
programming.addSkill(SkillElement("IOT", 3))
programming.addSkill(SkillElement("PHP", 1))
programming.addSkill(SkillElement("Javascript", 4))
skills.addSkillContainer(programming)
############################################################

