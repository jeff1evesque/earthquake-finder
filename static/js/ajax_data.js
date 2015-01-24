/**
 * ajax_data.js: store HTML form data into jQuery variables. Then, determine the
 *               strongest earthquake within the provided 'radius', and 'timeframe'
 *               parameters, using server-side logic.
 */

$(function() {
  $('form').validate({
    submitHandler: function() {

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
      // Remove AJAX Overlay
        $('form .ajax_overlay').fadeOut(200, function(){ $(this).remove() });
      // Append Results
        $('.result').remove();
        $('.fieldset_parameters').after( '<p class="result">' + data + '</p>' );
      }).fail(function(jqXHR, textStatus, errorThrown) {
        $('.result').remove();
        $('.fieldset_parameters').after( '<p class="result error">Error: Could not submit request. Please review the messages in the browser \'console.log\'</p>' );
        console.log('Error Thrown: '+errorThrown);
        console.log('Error Status: '+textStatus);
      });

    // prevent form redirect
      return false;
    }
  });
});
