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

import os
import glob
from BeautifulSoup import BeautifulSoup

from engine import skills
from engine import project
from engine import experience
from engine import formation

class XmlParser:
    
    #
    def createExperiences(self):
        experiences = experience.ExperienceCategory("Experiences")
        path = "engine/experiences/"
        for xmlDoc in glob.glob(os.path.join(path, '*.xml')):
            root = BeautifulSoup(open(xmlDoc,'r').read())
            
            exp = experience.Experience(str(root.experiences.title.string),
            str(root.experiences.description.string),
            True,
            str(root.experiences.image.string))
            
            exp.dateStart = datetime.date(
              int(root.experiences.datestart.y.string), 
              int(root.experiences.datestart.m.string), 
              int(root.experiences.datestart.d.string)
            )
            exp.dateEnd = datetime.date(
              int(root.experiences.dateend.y.string), 
              int(root.experiences.dateend.m.string), 
              int(root.experiences.dateend.d.string)
            )
            experiences.addElement(exp)   
        return experiences
    
    #    
    def createProjects(self):
        projects = project.ProjectCategory("Projects")
        path = "engine/projects/"
        for xmlDoc in glob.glob(os.path.join(path, '*.xml')):
            root = BeautifulSoup(open(xmlDoc,'r').read())
            
            elt = project.Project(str(root.project.title.string),
            str(root.project.description.string),
            True)
            if root.project.image:
                elt.setLogoPath(str(root.project.image.string))
            elt.dateStart = datetime.date(
              int(root.project.datestart.y.string), 
              int(root.project.datestart.m.string), 
              int(root.project.datestart.d.string)
            )
            elt.dateEnd = datetime.date(
              int(root.project.dateend.y.string), 
              int(root.project.dateend.m.string), 
              int(root.project.dateend.d.string)
            )
            projects.addElement(elt)   
        return projects
    
    #    
    def createFormations(self):
        formations = formation.FormationCategory("Formations")
        path = "engine/formations/"
        for xmlDoc in glob.glob(os.path.join(path, '*.xml')):
            root = BeautifulSoup(open(xmlDoc,'r').read())
            
            elt = formation.Formation(str(root.formation.title.string),
            str(root.formation.description.string),
            str(root.formation.image.string),
            True,
            ("http://www.polytech-grenoble.fr/","fr"))
            
            elt.dateStart = datetime.date(
              int(root.formation.datestart.y.string), 
              int(root.formation.datestart.m.string), 
              int(root.formation.datestart.d.string)
            )
            elt.dateEnd = datetime.date(
              int(root.formation.dateend.y.string), 
              int(root.formation.dateend.m.string), 
              int(root.formation.dateend.d.string)
            )
            formations.addElement(elt)   
        return formations
    
    #
    def createSkills(self):
        skillsSection = skills.SkillSection("Skills", "", 
                              [("it-skills", "IT Skills"),
                              ("programming", "Programming")])
                              
        itSkills = skills.SkillContainer("IT skills")
        environement = skills.SubSkillContainer("Tools")
        systemes = skills.SubSkillContainer("Systems")
        design = skills.SubSkillContainer("Design")
        programming = skills.SkillContainer("Programming")
        
        path = "engine/skills/"
        
        for xmlDoc in glob.glob(os.path.join(path, '*.xml')):
            root = BeautifulSoup(open(xmlDoc,'r').read())
            container = (str(root.skill.container.string))
            
            skillElt = skills.SkillElement(str(root.skill.title.string),int(root.skill.level.string))
            #setters
            if(root.skill.content_en):
                skillElt.setContent(root.skill.content_en.contents[0],"en")
            if(root.skill.content_fr):
                skillElt.setContent(root.skill.content_fr.contents[0],"fr")
            if(root.skill.description_en):
                skillElt.setDescription(root.skill.description_en.contents[0],"en")
            if(root.skill.content_fr):
                skillElt.setDescription(root.skill.description_fr.contents[0],"fr")
            skillElt.createPage()
            #set in category
            if str(container) == "itSkills":
                itSkills.addSkill(skillElt)
            elif str(container) == "environnement":
                itSkills.addSkill(skillElt)
            elif str(container) == "systemes":
                systemes.addSkill(skillElt)
            elif str(container) == "design":
                design.addSkill(skillElt)
            elif str(container) == "programming":
                programming.addSkill(skillElt)
            else:
                print("unknow container:", str(container) )
            
        itSkills.addSubSkillContainer(systemes)
        itSkills.addSubSkillContainer(design)
        itSkills.addSubSkillContainer(environement)
        skillsSection.addSkillContainer(itSkills)  
        skillsSection.addSkillContainer(programming)
        return skillsSection  

#itSkills = SkillContainer("IT skills")
#environement = SubSkillContainer("Tools")
#systemes = SubSkillContainer("Systems")
#design = SubSkillContainer("Design")
#
#systemes.addSkill(SkillElement("Linux", 4))
#systemes.addSkill(SkillElement("MacOS", 1))
#systemes.addSkill(SkillElement("Windows", 3))
#design.addSkill(SkillElement("Blender",1))
#design.addSkill(SkillElement("Photoshop",4))
#design.addSkill(SkillElement("Gimp", 2))
#environement.addSkill(SkillElement("Eclipse",4))
#environement.addSkill(SkillElement("Netbeans",4))
#environement.addSkill(SkillElement("Svn",3))
#environement.addSkill(SkillElement("Git",4))
#environement.addSkill(SkillElement("Mercurial",2))
#
#itSkills.addSubSkillContainer(systemes)
#itSkills.addSubSkillContainer(design)
#itSkills.addSubSkillContainer(environement)
#skills.addSkillContainer(itSkills)
#############################################################
#
#programming = SkillContainer("Programming")
#programming.addSkill(SkillElement("Java/JEE", 4))
#programming.addSkill(SkillElement("OcamL", 1))
#programming.addSkill(SkillElement("C/C++", 4))
#programming.addSkill(SkillElement("ADA", 1))
#programming.addSkill(SkillElement("Perl", 2))
#programming.addSkill(SkillElement("Python", 4))
#programming.addSkill(SkillElement("C#", 1))
#programming.addSkill(SkillElement("Android", 3))
#programming.addSkill(SkillElement("Ruby", 1))
#programming.addSkill(SkillElement("HTML5", 3))
#programming.addSkill(SkillElement("ASP", 1))
#programming.addSkill(SkillElement("CSS3", 2))
#programming.addSkill(SkillElement("MatLab/Octave", 1))
#programming.addSkill(SkillElement("SQL", 4))
#programming.addSkill(SkillElement("NoSQL", 2))
#programming.addSkill(SkillElement("IOT", 3))
#programming.addSkill(SkillElement("PHP", 1))
#programming.addSkill(SkillElement("Javascript", 4))
#skills.addSkillContainer(programming)
############################################################
    
#
#####
#exp = Experience("Orange","""Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum""",
#True,
#"./public/img/exps/obs.jpg")
#exp.dateStart = datetime.date(2002, 3, 11)
#exp.dateEnd = datetime.date(2005, 3, 11)
#experiences.addElement(exp)
###
#exp2 = Experience("Emisys","""Lorem ipsunisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum""",
#True,
#"./public/img/exps/emisys.jpeg")
#exp2.dateStart = datetime.date(2001, 3, 11)
#experiences.addElement(exp2)
###
#exp3 = Experience("Joseph Fourier","""Lorem ipsum dolincididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum""",
#True,
#"./public/img/exps/ujf.gif")
#exp3.dateStart = datetime.date(2001, 3, 11)
#experiences.addElement(exp3)