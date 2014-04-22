#! /usr/bin/python
# -*-coding:Utf-8 -*
#
#
# copyright Thomas Nunes <thomasnds.github.io>
# License MIT
############################################################
from pages.page import *

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
    
#######################################
# get the css class associated
#######################################
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
###################################################
class SkillElement:
    levelSkill = None
    
    def __init__(self, name, level = 1):
        self.type = type
        self.name = name
        self.levelSkill = LevelSkill(level)

    def __str__(self):
        return """<div id="content-skills"  class='skill-element
               """+ self.levelSkill.getClass() + """'>
               """ + str(self.name) + """</div><!--/span-->"""
 
###################################################
# A skill subgroup
#
# _skillsElements ([SkillElement]) list of skills
###################################################              
class SubSkillSection(AbstractElement):
    _skillsElements = []
   
    def __init__(self, name):
        AbstractElement.__init__(self, name, "")
        self._skillsElements = []
 
    # skill (SkillElement)
    def addSkill(self, skill):
        self._skillsElements.append(skill)
    
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
# _subSkillSection ([SubSkillSection]) list of subgroup of skills
###################################################       
class SkillSection(AbstractElement):
    _subSkillSection = []
    _skillsElements = []
    
    def __init__(self, name):
        AbstractElement.__init__(self, name, "")
        self._subSkillSection = []
        self._skillsElements = []
     
    # skill (SubSkillSection)
    def addSkillSection(self, skill):
        self._subSkillSection.append(skill)

    # skill (SkillElement)
    def addSkill(self, skill):
        self._skillsElements.append(skill)
        
    def __str__(self):
        res= """
        <div class="col-4 col-sm-6 col-lg-6">
            <h3 id='""" + self.id + """' class="skill-title">""" + self.name + "</h3>" 
        for skill in self._subSkillSection:
            res += str(skill)
        for skill in self._skillsElements:
            res += str(skill)
        res += "</div><!--/span-->"
        return res


skills = Section("Skills", "", [("it-skills", "IT Skills"),
                                ("programming", "Programming")])
skillSections = []

itSkills = SkillSection("IT skills")
environement = SubSkillSection("Tools")
systemes = SubSkillSection("Systemes")
design = SubSkillSection("Design")

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

itSkills.addSkillSection(systemes)
itSkills.addSkillSection(design)
itSkills.addSkillSection(environement)
skillSections.append(itSkills)
############################################################

programming = SkillSection("Programming")
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
skillSections.append(programming)
############################################################


skills.description = """
        <h1 id="skills" class="title-section">""" + skills.name + """</h1>
            <div class="container"><div class="">
                    <div class="col-xs-12 col-sm-9 skills-container">
                        <div class="row">"""
for section in skillSections:
    skills.description += str(section)
skills.description += """
                        </div><!--/span-->
                    </div><!--/span-->
                </div><!--/row-->
            </div>
        """
