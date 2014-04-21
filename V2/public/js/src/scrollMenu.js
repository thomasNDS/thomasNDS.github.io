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

        //calculate destination place
        var dest = 0;
        if ($(this.hash) && $(this.hash) !== "undefined" && $(this.hash).offset() && $(this.hash).offset() !== "undefined") {
            event.preventDefault();
            if ($(this.hash).offset().top > $(document).height() - $(window).height()) {
                dest = $(document).height() - $(window).height();
            } else {
                if ($(this.hash) && $(this.hash) !== "undefined" && $(this.hash).offset() && $(this.hash).offset() !== "undefined")
                    dest = $(this.hash).offset().top;
            }
            //go to destination
            $('html,body').animate({
                scrollTop: dest
            }, 200, 'swing');
        }
    });

});

//// fade the menu on bottom
$(window).scroll(function() {
    var contact = $("#contactForm");
    if (contact && contact !== "undefined") {
        var offset = contact.offset();
        if ($(window).scrollTop() > offset.top - 250) {
            $(".sidebar").hide();
        }
        else {
            $(".sidebar").show();
        }
    }
});