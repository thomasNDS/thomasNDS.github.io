$(function() {
    $.stellar({
        horizontalScrolling: false,
        verticalOffset: 40,
        responsive: true,
        showElement: function($elem) {
            $elem.addClass("on-show");
        },
        hideElement: function($elem) {
            $elem.removeClass("on-show");
        },
    });
});
$('#contactForm').stellar();
$('#stellar').stellar();
