
$('#affix-nav').affix({offset:{top:100,bottom:function(){return(this.bottom=$('.footer').outerHeight(true))}}})
$(document).ready(function(){$("footer a, .sidebar a").click(function(event){console.log("click")
event.preventDefault();var dest=0;if($(this.hash).offset().top>$(document).height()-$(window).height()){dest=$(document).height()-$(window).height();}else{dest=$(this.hash).offset().top;}
$('html,body').animate({scrollTop:dest},200,'swing');});});$(window).scroll(function(){if($(window).scrollTop()+$(window).height()>$(document).height()-600){$(".sidebar").fadeOut(10);}
else{$(".sidebar").fadeIn();}});