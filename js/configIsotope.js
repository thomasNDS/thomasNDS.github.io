

$(function() {

    var $container = $('#container');
    // add randomish size classes
    $container.find('.element').each(function() {
        var $this = $(this),
                number = parseInt($this.find('.number').text(), 10);
    });
    $container.isotope({
        itemSelector: '.element',
        masonry: {
            columnWidth: 10
        },
        getSortData: {
            symbol: function($elem) {
                return $elem.attr('data-symbol');
            },
            category: function($elem) {
                return $elem.attr('data-category');
            },
            number: function($elem) {
                return parseInt($elem.find('.number').text(), 10);
            },
            weight: function($elem) {
                return parseFloat($elem.find('.weight').text().replace(/[\(\)]/g, ''));
            },
            name: function($elem) {
                return $elem.find('.name').text();
            }
        }
    });
    var $optionSets = $('#options .option-set'),
            $optionLinks = $optionSets.find('a');
    $optionLinks.click(function() {
        var $this = $(this);
        // don't proceed if already selected
        if ($this.hasClass('selected')) {
            return false;
        }
        var $optionSet = $this.parents('.option-set');
        $optionSet.find('.selected').removeClass('selected');
        $this.addClass('selected');
        // make option object dynamically, i.e. 
        {
            filter: '.filter-class';
        }
        var options = {},
                key = $optionSet.attr('data-option-key'),
                value = $this.attr('data-option-value');
        // parse 'false' as false boolean
        value = value === 'false' ? false : value;
        options[ key ] = value;
        if (key === 'layoutMode' && typeof changeLayoutMode === 'function') {
            // changes in layout modes need extra logic
            changeLayoutMode($this, options);
        } else {
            // otherwise, apply new options
            $container.isotope(options);
        }
        return false;
    });
    // change size of clicked element
    $container.delegate('.element', 'click', function() {
        $(this).toggleClass('large');
        $container.isotope('reLayout');
    });
    var $sortBy = $('#sort-by');
    $('#shuffle a').click(function() {
        $container.isotope('shuffle');
        $sortBy.find('.selected').removeClass('selected');
        $sortBy.find('[data-option-value="random"]').addClass('selected');
        return false;
    });
    previousId = "#menu-1";
    previousMenu = ".menuPart-1";
    $("#exps").hide();
    $("#skills").hide();

    $("#expFilter").click(function() {
        $(previousMenu).removeClass("active");
        previousMenu = ".menuPart-1";
        $(previousMenu).addClass("active");
        $(previousId).removeClass("active");
        $("#menu-3").addClass("active");
        previousId = "#menu-3";
        $("#exps").hide();
        $("#skills").show();
        $('#options').addClass('extended');
    });
    $("#skillFilter").click(function() {
        $(previousMenu).removeClass("active");
        previousMenu = ".menuPart-1";
        $(previousMenu).addClass("active");

        $(previousId).removeClass("active");
        $("#menu-2").addClass("active");
        previousId = "#menu-2";
        $("#exps").show();
        $("#skills").hide();
        $('#options').addClass('extended');
    });
    $("#allFilter").click(function() {
        $(previousId).removeClass("active");
        $("#menu-1").addClass("active");
        previousId = "#menu-1";
        $("#exps").hide();
        $("#skills").hide();
        $('#options').removeClass('extended');
    });
    $("#formationFilter").click(function() {
        $(previousId).removeClass("active");
        $("#menu-4").addClass("active");
        previousId = "#menu-4";
        $("#exps").hide();
        $("#skills").hide();
        $('#options').removeClass('extended');
    });
    $(".menuPart-1>a").click(function() {
        $(previousMenu).removeClass("active");
        $(".menuPart-1").addClass("active");
        previousMenu = ".menuPart-1";
    });
    $(".menuPart-2>a").click(function() {
        $(previousMenu).removeClass("active");
        $(".menuPart-2").addClass("active");
        previousMenu = ".menuPart-2";
    });
    $(".menuPart-3>a").click(function() {
        $(previousMenu).removeClass("active");
        $(".menuPart-3").addClass("active");
        previousMenu = ".menuPart-3";
    });
});
