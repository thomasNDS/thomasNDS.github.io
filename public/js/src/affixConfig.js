$(document).ready(function() {
    $("#affix-nav").affix({offset: {top: function() {
                return $(window).height() * .7
            }, bottom: function() {
                return $(".footer").outerHeight(true) + $("#contactForm").outerHeight(true) + 32
            }}})
});