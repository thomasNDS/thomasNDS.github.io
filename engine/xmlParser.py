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
    
    def createExperiences(self):
        experiences = experience.ExperienceCategory("Experiences")
        path = "engine/experiences/"
        print (os.path.join(path, '*.xml'))
        for xmlDoc in glob.glob(os.path.join(path, '*.xml')):
            print ("filename", xmlDoc)
            root = BeautifulSoup(open(xmlDoc,'r').read())
            
            exp = experience.Experience(str(root.experiences.title.string),
            str(root.experiences.description.string),
            True,
            str(root.experiences.image.string))
            print (exp.description)
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