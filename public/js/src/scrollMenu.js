$(document).ready(function() {
    $("footer a, .sidebar a, .scroll-link, .anchor").click(function(h) {
        var t = 0;
        if ($(this.hash) && $(this.hash) !== "undefined" && $(this.hash).offset() && $(this.hash).offset() !== "undefined") {
            h.preventDefault();
            if ($(this.hash).offset().top > $(document).height() - $(window).height()) {
                t = $(document).height() - $(window).height()
            } else {
                if ($(this.hash) && $(this.hash) !== "undefined" && $(this.hash).offset() && $(this.hash).offset() !== "undefined")
                    t = $(this.hash).offset().top
            }
            $("html,body").animate({scrollTop: t}, 200, "swing")
        }
    })
});