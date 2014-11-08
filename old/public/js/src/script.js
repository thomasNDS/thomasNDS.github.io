
var state = "none"; // map - text

function toggleText() {
    $("#container-extra").animate({
        height: "show",
        opacity: "show",
        margin: "show"
    }, 500);
}
function toggleMap() {
    $("#map-container").animate({
        height: "show",
        opacity: "show",
        margin: "show"
    }, 1000);
}
function toggleDescr() {
    $("#descr-container").animate({
        height: "show",
        opacity: "show",
        margin: "show"
    }, 1000);
}
function toggleAll() {
    $("#descr-container").hide()
    $("#map-container").hide()
    $("#container-extra").hide()
}
//Company toggle
$(".company").click(function() {
    toggleAll()
    switch (state) {
        case "company":
            state = "none"
            toggleAll()
            break;

        default:
            state = "company"
            toggleText()
    }
    adaptHeight();
});
//city toggle
$(".city").click(function() {
    toggleAll()
    switch (state) {
        case "map":
            state = "none"
            toggleAll()
            break;

        default:
            state = "map"
            toggleMap()
    }
    adaptHeight();
});
//descr toggle
$(".descr").click(function() {
    toggleAll()
    switch (state) {
        case "descr":
            state = "none"
            toggleAll()
            break;

        default:
            state = "descr"
            toggleDescr()
    }
    adaptHeight();
});

if (window.addEventListener) { // Mozilla, Netscape, Firefox
    window.addEventListener('load', WindowLoad, false);
} else if (window.attachEvent) { // IE
    window.attachEvent('onload', WindowLoad);
}

function adaptHeight() {
    var height2set = 300;
    switch (state) {
        case "none":
            height2set = 300;
            break;
        case "map":
            height2set = 600;
            break;
        case "text":
            height2set = 512;
            break;
            default:
            height2set = 600;

    }
    if ($(window).height() <= height2set) {
        height2set = $(window).height();
    }
    $(".bloc").animate({
        height: height2set
    }, 500);
}

function WindowLoad(event) {
    $("#map-container").toggle();
    $('#overlay').fadeToggle();
    if ($(window).height() > 512) {
        titleAnimation();
    }
}

$(document).ready(function() {
    setFirefly();
});
function setFirefly() {
    $(function() {
        $.firefly();
    });
}

function socialAnimation() {
    $("#header-part3").animate({
        "opacity": "1"
    }, {
        duration: 7000,
        easing: "swing"
    });
}

function textAnimation() {
    $("#header-part2").animate({
        "margin-top": "1em",
        "opacity": "1"
    },
                               {
                                   duration: 500,
                                   easing: "swing",
                                   complete: function() {
                                       socialAnimation();
                                   }
                               });
}

function titleAnimation() {
    $("#header-part1").animate({
        "margin": "0px",
        "opacity": "1"
    },
                               {
                                   duration: 500,
                                   easing: "swing",
                                   complete: function() {
                                       textAnimation();
                                   }
                               });
}
