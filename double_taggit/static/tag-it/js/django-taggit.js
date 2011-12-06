(function($) {
    $.djTagit = {};
    $.get('/double-taggit/json', function(data) {
      $.djTagit.data = data;
         $(".taggit").tagit({
            availableTags: $.djTagit.data
         });
    });
})(jQuery);


