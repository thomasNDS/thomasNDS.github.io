#! /usr/bin/python2.7
# -*-coding:Utf-8 -*
#
#
# copyright Thomas Nunes <thomasnds.github.io>
# License MIT
#############################################################

###############################################
# Convert a name (String) to an valid id (String)
#
# @param (string) name
# @return (String) a valid id
###############################################
def name2id(name):
    id = "no-id"
    if name != "":
        id = name.replace(" ","-")
        id= id.replace("'","-")
        id= id.replace("é","e")
        id= id.replace("è","e")
        id= id.replace("&","-")
        id= id.replace("~","-")
        id= id.replace("ç","c")
        id= id.replace("à","a")
        id= id.replace("ù","u")
        id= id.replace("#","-")
        id= id.replace("?","")
        id= id.replace("!","")
        id= id.replace(",","")
        id= id.replace(";","")
        id= id.replace("/","")
        id= id.replace(":","")
        id= id.replace(".","-")
    return id
    

###############################################
# Submenu of element
# 
# _elements ([String])
###############################################
class SubMenu:
    _elements = []

    # elts ([String])
    # name (String)
    def __init__(self, name, elts):
       self._elements = elts
    
    # elt (String)
    def addElement(self,elt):
        _elements.append(elt)

    def __str__(self):
        res= "<li>"
        res += '<a href="#' + name2id(self.name) + '">' + self.name + '</a><ul class="nav">'
        for elt in self._elements:
            res += '<li><a href="#' + name2id(elt) + '">' + elt + '</a></li>'
        
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
    def addSubMenu(self, name, elts):
        self._subMenu.append(SubMenu(elts))
    
    def __str__(self):
        res= """<div class="container"><div class="row">
        <nav id="affix-nav" class="sidebar col-md-3 sidebar-offcanvas">
            <ul class="nav sidenav" data-spy="affix" data-offset-top="10">"""
            
        for sub in self._subMenu:
            res += sub
        
        res += """    </ul>
                    </nav>
                  </div><!--/row-->
                </div>"""
        return res

        
