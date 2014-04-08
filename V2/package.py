#! /usr/bin/python2.7
# -*-coding:Utf-8 -*
#
# Static blog generator
#
# copyright Thomas Nunes <thomasnds.github.io>
# License MIT

css2min = [
            "public/css/libs/bootstrap.css",
            "public/css/libs/bootflat.css",
            "public/css/src/general.css",
            ]
js2min = [
            "public/js/libs/bootstrap.min.js",
            "public/js/libs/stellar.js",
            "public/js/libs/respond.min.js",
            "public/js/libs/icheck.min.js",
            "public/js/src/stellarConfig.js",
            "public/js/src/scrollButton.js",
            ]
html2min = [
            "indexbis.html",
            ]
            
file2min = js2min + html2min

#Where generated files will be set
path2cssMin = "public/gen/min.css"
path2jsMin = "public/gen/min.js"