#! /usr/bin/python2.7
# -*-coding:Utf-8 -*
#
#
# copyright Thomas Nunes <thomasnds.github.io>
# License MIT
#############################################################

###############################################
#
#
#
###############################################
class subMenu:
    _elements = []

    def __init__(self, name, elts):
       self._elements = elts
    
    def addElement(self,elt):
        _elements.append(elt)

    def __str__(self):
        res= ""
        return res

###############################################
#
#
#
###############################################
class Menu:
    _subMenu = []

    def addSubMenu(self, name, elts):
        self._subMenu.append(subMenu(elts))
    
    def __str__(self):
        res= ""
        return res