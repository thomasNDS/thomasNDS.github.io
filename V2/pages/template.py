#! /usr/bin/python2.7
# -*-coding:Utf-8 -*
#
#
# copyright Thomas Nunes <thomasnds.github.io>
# License MIT
#############################################################
    
###############################################
# Submenu of element
# 
# _elements [(String, String)] value, id
###############################################
class SubMenu:
    _elements = []

    # elts [(String, String)]
    def __init__(self, elts, title,id):
       self._elements = elts
       print elts
       self.title = title
       self.id = id
    
    def addElement(self,name,id):
        _elements.append((name,id))

    def __str__(self):
        res= "<li>"
        res += '<a href="#' + str(self.id) + '">' + self.title + '</a><ul class="nav">'
        for elt in self._elements:
            res += '<li><a href="#' + str(elt[0]) + '">' + str(elt[1]) + '</a></li>'
        
        res += "</ul></li>"
        return res

###############################################
# Create right menu with submenu
#
# _subMenu (SubMenu)
###############################################
class Menu:
    _subMenu = []

    # elts ([String])
    # name (String)
    def addSubMenu(self, title, id, elts):
        self._subMenu.append(SubMenu(elts, title, id))
    
    def __str__(self):
        res= """<div class="container"><div class="row">
        <nav id="affix-nav" class="sidebar col-md-3 sidebar-offcanvas">
            <ul class="nav sidenav" data-spy="affix" data-offset-top="10">"""
            
        for sub in self._subMenu:
            res += str(sub)
        
        res += """    </ul>
                    </nav>
                  </div><!--/row-->
                </div>"""
        return res

        
