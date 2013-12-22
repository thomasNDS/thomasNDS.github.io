

$(function() {

    var $container = $('#container');
    // add randomish size classes
    $container.find('.element').each(function() {
        var $this = $(this),
                number = parseInt($this.find('.number').text(), 10);
        if (number % 3 === 0) {
            $this.css('background-color', 'chocolate');
        }
        if (number % 4 === 0) {
            $this.css('background-color', 'lightblue');
        }
        if (number % 5 === 0) {
            $this.css('background-color', 'coral');
        }
        if (number % 6 === 0) {
            $this.css('background-color', 'lightgreen');
        }
        if (number % 7 === 0) {
            $this.css('background-color', 'cyan');
        }
        if (number % 8 === 0) {
            $this.css('background-color', 'pink');
        }
        if (number % 9 === 0) {
            $this.css('background-color', 'teal');
        }
        if (number % 11 === 0) {
            $this.css('background-color', 'crimson');
        }
        if (number % 13 === 0) {
            $this.css('background-color', 'orangered');
        }
        if (number % 17 === 0) {
            $this.css('background-color', 'plum');
        }
        if (number % 19 === 0) {
            $this.css('background-color', 'lightcyan');
        }
        if (number % 19 === 0) {
            $this.css('background-color', 'lightseagreen');
        }
    });
    $container.isotope({
        itemSelector: '.element',
        masonry: {
            columnWidth: 120
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
       { filter: '.filter-class' }
        var options = {},
                key = $optionSet.attr('data-option-key'),
                value = $this.attr('data-option-value');
        // parse 'false' as false boolean
        value = value === 'false' ? false : value;
        options[ key ] = value;
        if (key === 'layoutMode' && typeof changeLayoutMode === 'function') {
            // changes in layout modes need extra logic
            changeLayoutMode($this, options)
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
    
    $("#exps").hide();
    $("#skills").hide();
    $("#expFilter").click(function() {
        $("#exps").hide();
        $("#skills").show();
    });
    $("#skillFilter").click(function() {
        $("#exps").show();
        $("#skills").hide();
    });
        $("#allFilter").click(function() {
        $("#exps").hide();
        $("#skills").hide();
    });
});