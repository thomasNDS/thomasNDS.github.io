
            var state = "none"; // map - text

            function toggleText() {
                $("#container-extra").animate({
                    height: "toggle",
                    opacity: "toggle",
                    margin: "toggle"
                }, 500);
            }
            function toggleMap() {
                $("#map-container").animate({
                    height: "toggle",
                    opacity: "toggle",
                    margin: "toggle"
                }, 1000);
            }

            $(".company").click(function() {
                switch (state) {
                    case "none":
                        state = "text";
                        toggleText();
                        break;
                    case "map":
                        state = "text";
                        toggleText();
                        toggleMap();
                        break;
                    case "text":
                        state = "none";
                        toggleText();
                        break;
                }
                adaptHeight();
            });

            $(".city").click(function() {
                switch (state) {
                    case "none":
                        state = "map";
                        toggleMap();
                        break;
                    case "map":
                        state = "none";
                        toggleMap();
                        break;
                    case "text":
                        state = "map";
                        toggleText();
                        toggleMap();
                        break;
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
