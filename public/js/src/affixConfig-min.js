
$(document).ready(function(){console.log(($(window).height()))
$('#affix-nav').affix({offset:{top:function(){return($(window).height()*0.30)-20;},bottom:function(){return($('.footer').outerHeight(true)+$('#contactForm').outerHeight(true)+32);}}});});