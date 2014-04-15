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
################################################
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
################################################
class Entreprise:
    self.website = None 
    self.location = None
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def getShortDescription(self):
        res = self.name + " - " + self.description
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
################################################
class Experience:
    self.dateStart = None
    self.dateEnd = None
    self.location = None
    self._entreprise = None

    def __init__(self, name, description):
        self.name = title
        self.description = description

    # entreprise: (Object Entreprise)
    def setEntreprise(self,entreprise):
        self._entreprise = entreprise
    
    def toString(self):
        res= """<div class="col-6 col-sm-6 col-lg-4 element">
            <h2 class="element-title">""" + self. + """</h2>
              <p class="element-description">""" + self.description + """ </p>"""
        
        if self._entreprise:
            res+="""<p class="entreprise">""" + self.entreprise.getShortDescription() + """</p>"""
        
        if self.dateStart and self.dateEnd:
            res+= """<p class="element-date"><span class="start-date">
            """ + self.dateStart + """</span> - <span class="end-date">""" + self.dateEnd +"""</span></p>"""
        else: if self.dateStart:
            res+= """<p class="element-date"><span class="start-date">
            """ + self.dateStart + """</span></p>"""
        
        res += """<p><a class="btn btn-default" href="#" role="button">More »</a></p></div><!--/span-->"""
        return res
        
def getMenu():
    return """<div class="container"><div class="row">
        <nav id="affix-nav" class="sidebar col-md-3 sidebar-offcanvas">
            <ul class="nav sidenav" data-spy="affix" data-offset-top="10">
                <li class="active"><a href="#cupcake">Cupcake Lorem Ipsum</a>
                    <ul class="nav">
                        <li><a href="#sweetjelly">Sweet Jelly</a></li>
                        <li><a href="#tiramisu">Tiramisu</a></li>
                        <li><a href="#pie">Pie</a></li>
                    </ul>
                </li>
                <li><a href="#veggie">Veggie Lorem Ipsum</a>
                    <ul class="nav">   
                        <li><a href="#coriander">Coriander</a></li>
                        <li><a href="#kohlrabi">Kohlrabi</a></li>
                        <li><a href="#amaranth">Amaranth</a></li>
                        <li><a href="#soybean">Soybean</a></li>        
                    </ul>
                </li>
            </ul>
        </nav>
      </div><!--/row-->
    </div>"""

def getAll():
    res = """<div class="container"><div class="">
        <div class="col-xs-12 col-sm-9">
          <div class="row">""" + """<div class="col-6 col-sm-6 col-lg-4">
              <h2>Heading</h2>
              <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>
              <p><a class="btn btn-default" href="#" role="button">View details »</a></p>
            </div><!--/span-->
            <div class="col-6 col-sm-6 col-lg-4">
              <h2>Heading</h2>
              <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>
              <p><a class="btn btn-default" href="#" role="button">View details »</a></p>
            </div><!--/span-->
            <div class="col-6 col-sm-6 col-lg-4">
              <h2>Heading</h2>
              <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>
              <p><a class="btn btn-default" href="#" role="button">View details »</a></p>
            </div><!--/span-->
            <div class="col-6 col-sm-6 col-lg-4">
              <h2>Heading</h2>
              <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>
              <p><a class="btn btn-default" href="#" role="button">View details »</a></p>
            </div><!--/span-->
            <div class="col-6 col-sm-6 col-lg-4">
              <h2>Heading</h2>
              <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>
              <p><a class="btn btn-default" href="#" role="button">View details »</a></p>
            </div><!--/span-->
          </div><!--/row-->
        </div><!--/span-->
      </div><!--/row-->
    </div>"""
    return res
