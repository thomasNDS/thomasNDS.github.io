$(document).ready(function() {
    $('#affix-nav').affix({
        offset: {
            top: function() {
                return ($(window).height()*0.30);
            },
            bottom: function() {
                return ($('.footer').outerHeight(true)+ $('#contactForm').outerHeight(true) + 25);
            }
        }
    });
});
