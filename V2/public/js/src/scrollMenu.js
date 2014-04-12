//Affix plugin
$('#affix-nav').affix({
    offset: {
        top: 100
        , bottom: function() {
            return (this.bottom = $('.footer').outerHeight(true))
        }
    }
})
//animate transition
$(document).ready(function() {
    $("footer a, .sidebar a").click(function(event) {
        console.log("click")
        event.preventDefault();
        //calculate destination place
        var dest = 0;
        if ($(this.hash).offset().top > $(document).height() - $(window).height()) {
            dest = $(document).height() - $(window).height();
        } else {
            dest = $(this.hash).offset().top;
        }
        //go to destination
        $('html,body').animate({
            scrollTop: dest
        }, 200, 'swing');
    });
});

//            fade the menu on bottom
$(window).scroll(function() {
    if ($(window).scrollTop() + $(window).height() > $(document).height() - 600) {
        $(".sidebar").fadeOut(10);
    }
    else {
        $(".sidebar").fadeIn();
    }
});