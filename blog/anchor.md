Anchor
-----------------

js: 

    /*
     * Append a anchor to be able to get a link to current section.
     */
    $('h1[id], h2[id], h3[id], h4[id]').each(function() {
      var current = $(this),
          id = current.attr('id');

      if (!current.text()) {
        return;
      }

      current.append(
        '<a class="anchor" href="#' + id + '" title="Link to current section">¶</a>'
      );
    })

css : 


h1 .anchor,
h2 .anchor,
h3 .anchor,
h4 .anchor {
  display: none;
}

h1:hover .anchor,
h2:hover .anchor,
h3:hover .anchor,
h4:hover .anchor {
  display: inline-block;
}
