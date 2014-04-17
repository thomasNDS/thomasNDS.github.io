#! /usr/bin/python2.7
# -*-coding:Utf-8 -*
#
#
# copyright Thomas Nunes <thomasnds.github.io>
# License MIT
#############################################################

from pages.page import *
from pages.template import *
        
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

experiences = Category("experiences")
testexp = Experience("test","description")

experiences.addElement(testexp)


