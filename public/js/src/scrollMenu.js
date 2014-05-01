//animation when scrolling
$(document).ready(function() {
    $("footer a, .sidebar a").click(function(event) {
        var dest = 0;
        if ($(this.hash) && $(this.hash) !== "undefined" && $(this.hash).offset() && $(this.hash).offset() !== "undefined") {
            event.preventDefault();
            if ($(this.hash).offset().top > $(document).height() - $(window).height()) {
                dest = $(document).height() - $(window).height();
            } else {
                if ($(this.hash) && $(this.hash) !== "undefined" && $(this.hash).offset() && $(this.hash).offset() !== "undefined")
                    dest = $(this.hash).offset().top;
            }
            $('html,body').animate({scrollTop: dest}, 200, 'swing');
        }
    });
});