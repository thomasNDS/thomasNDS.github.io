!function(a){a.fn.starscroll=function(d,e,f,g,h,i,j,k){var l=a(this),m=c.any(),n=new b(l,m,d,e,f,g,h,i,j,k);return window.addEventListener("scroll",function(){n.parallax()},!1),k&&!m&&setInterval(function(){n.time+=5,n.parallax()},25),this.el};var b=function(b,c,d,e,f,g,h,i,j,k){this.el=b,this.levels=e>10?10:e,this.layers=[],this.dimension=g>20?20:g,this.density=f,this.colour=i?i:[255,255,255],this.hue=j?j:!1,this.bit=d?d:!1,this.time=0,this.anim=k,this.smooth=5;var l,m,n=a(window).width(),o=a(window).width();l=n>700?700:n,m=o>600?650:o,this.w=l,this.h=m,c||this.init()};b.prototype.init=function(){for(var a=0;a<this.levels;a++)this.layers[a]=this.buildlayers(a);this.images=this.createStars(),this.applyImages(this.images)},b.prototype.buildlayers=function(b){var c={},d=document.createElement("canvas"),e=d.getContext("2d");d.width=this.w,d.height=this.h;var f=a('<div id="starchild'+b+'"/>');return this.buildDOMels(f,b),c.canvas=d,c.context=e,c.DOM=f,c},b.prototype.createStars=function(){for(var a=[],b=0;b<this.levels;b++){for(var c=this.layers[b].canvas,d=this.layers[b].context,e=this.hsl(this.colour),f=0;f<this.density;f++)this.drawStar(d,b,e);a[b]=this.convertCanvasToImage(c)}return a},b.prototype.drawStar=function(a,b,c){var d=this.dimension/(.075*b+1),e=Math.random()*d,f=0,g=0,h=Math.random()*.9*e,i=this.hue?this.colstep(c):this.colour;f=this.boundary("x",e),g=this.boundary("y",e);var j=a.createRadialGradient(f,g,h,f,g,e),k=.7+.3*Math.random();j.addColorStop(0,"rgba(255,255,255,.9)"),i&&j.addColorStop(.5,"rgba("+i+",.8)"),j.addColorStop(1,"rgba(255,255,255,0)"),a.beginPath(),8==this.bit?(a.fillRect(f,g,e,e),a.fillStyle="rgba(255,255,255,"+k+")"):(a.arc(f,g,e,0,2*Math.PI,!0),a.globalAlpha=.7+.3*Math.random(),a.fillStyle=j),a.fill()},b.prototype.colstep=function(a){return a[0]=a[0]-~~(4*Math.random())+~~(8*Math.random()),this.rgb(a)},b.prototype.boundary=function(a,b){var c=b,d=0;if("x"==a){var e=Math.random()*this.w;return d=e,c>e?d=e+c+Math.random()*b:e>this.w-c&&(d=e-c-Math.random()*b),d}var e=Math.random()*this.h;return d=e,c>e?d=e+c+Math.random()*b:e>this.h-c&&(d=e-c-Math.random()*b),d},b.prototype.applyImages=function(a){for(var b=0;b<this.levels;b++){var c=this.layers[b].DOM,d=a[b].src;c.css({"background-image":"url("+d+")"})}},b.prototype.parallax=function(){for(var a=window.pageYOffset-this.time,b=0;b<this.levels;b++){var c=this.layers[b].DOM,d=-a*((b+1)/2);c.css({"background-position":"0 "+d+"px"})}},b.prototype.buildDOMels=function(a){this.el.append(a);var b="5s";this.anim&&(b="0s"),this.el.css({position:"fixed","z-index":-1,top:0,width:"100%",height:"100%"}),a.css({transition:"all "+b+" cubic-bezier(0.230, 1.000, 0.320, 1.000)",position:"fixed",width:"100%",height:"100%","background-repeat":"repeat","background-color":"transparent"})},b.prototype.convertCanvasToImage=function(a){var b=new Image;return b.src=a.toDataURL("image/png"),b},b.prototype.hsl=function(a){var b=a[0]/255,c=a[1]/255,d=a[2]/255,e=Math.max(b,c,d),f=Math.min(b,c,d),g=(e+f)/2,h=0,i=0;e!=f&&(h=.5>g?(e-f)/(e+f):(e-f)/(2-e-f),i=b==e?(c-d)/(e-f):c==e?2+(d-b)/(e-f):4+(b-c)/(e-f)),g=100*g,h=100*h,i=60*i,0>i&&(i+=360);var j=[i,h,g];return j},b.prototype.rgb=function(a){var b,c,d,e,f,g,h=a[0],i=a[1],j=a[2];return i/=100,j/=100,0==i?e=f=g=255*j:(c=.5>=j?j*(i+1):j+i-j*i,b=2*j-c,d=h/360,e=this.hue2rgb(b,c,d+1/3),f=this.hue2rgb(b,c,d),g=this.hue2rgb(b,c,d-1/3)),[Math.round(e),Math.round(f),Math.round(g)]},b.prototype.hue2rgb=function(a,b,c){var d;return 0>c?c+=1:c>1&&(c-=1),d=1>6*c?a+6*(b-a)*c:1>2*c?b:2>3*c?a+6*(b-a)*(2/3-c):a,255*d};var c={Android:function(){return navigator.userAgent.match(/Android/i)},BlackBerry:function(){return navigator.userAgent.match(/BlackBerry/i)},iOS:function(){return navigator.userAgent.match(/iPhone|iPod/i)},Opera:function(){return navigator.userAgent.match(/Opera Mini/i)},Windows:function(){return navigator.userAgent.match(/IEMobile/i)},any:function(){return c.Android()||c.BlackBerry()||c.iOS()||c.Opera()||c.Windows()}}}(jQuery);