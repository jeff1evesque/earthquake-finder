/**
 * ajax_data.js: store HTML form data into jQuery variables. Then, determine the
 *               strongest earthquake within the provided 'radius', and 'timeframe'
 *               parameters, using server-side logic.
 */

$(function() {
  $('form').on('submit', function(event) {
    event.preventDefault();

  // Local Variables
    var form_data = $('form').serialize();

  // Compute Largest Earthquake
    $.ajax({
      type: 'POST',
      url: '/json_scraper/',
      data: form_data,
      beforeSend: function() {
        var spinner = new ajaxLoader( $(event.currentTarget) );
      }
    }).done(function(data) {
      $('form .ajax_overlay').fadeOut(200, function(){ $(this).remove() });
      console.log( data );
    }).fail(function(jqXHR, textStatus, errorThrown) {
      console.log('Error Thrown: '+errorThrown);
      console.log('Error Status: '+textStatus);
    });

  });
});
