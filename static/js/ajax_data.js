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
      url: '/find-largest-earthquake/',
      data: form_data,
      beforeSend: function() {
        $("form").validate({
          submitHandler: function(form) {
            $(form).ajaxSubmit();
          }
        });

        var spinner = new ajaxLoader( $(event.currentTarget) );
      }
    }).done(function(data) {
    // Remove AJAX Overlay
      $('form .ajax_overlay').fadeOut(200, function(){ $(this).remove() });

    // Remove previous results
      $('.result-container').remove();
      $('.close-result').remove();
      $('.result-error').remove();
      $('.result').remove();

    // Return Data
      var return_data = $.parseJSON(data).data
      if (return_data != null) {
        var id         = return_data.id;
        var location   = return_data.location;
        var magnitude  = return_data.magnitude;
        var longitude  = return_data.coordinates[0];
        var latitude   = return_data.coordinates[1];
        var elevation  = return_data.coordinates[2];
        var time       = return_data.time;
        var error      = return_data.error;
      }

    // Return Object
      var obj_return  = { id: id, location: location, magnitude: magnitude, longitude: longitude, latitude: latitude, elevation: elevation, time: time, error: error };

    // Return HTML
      result = '<table class="result-container">';
      if (return_data != null) {
        result += '<tr><th>Property</th><th>Value</th></tr>';
        if (obj_return.error != 'undefined') {
          $.each( obj_return, function( index, value ) {
            if (index != 'error') {
              result += '<tr><td class="result-index">' + index + '</td><td class="result-value">' + value + '</td></tr>';
            }
          });
        }
        else result += '<tr><td class="result-index">error</td><td class="result-value">' + obj_return['error'] + '</td></tr>';
      }
      else result += '<tr><td class="result-value">No earthquakes found using supplied parameters</td></tr>';
      result += '</table>';
      result += '<button type="button" class="close-result">Close</button>';

    // Append Return HTML
      $('body').append(result);

    }).fail(function(jqXHR, textStatus, errorThrown) {
      $('form .ajax_overlay').fadeOut(200, function(){ $(this).remove() });
      $('.result').remove();
      $('.fieldset_parameters').after( '<p class="result error">Error: Could not submit request. Please review the messages in the browser \'console.log\'</p>' );
      console.log('Error Thrown: '+errorThrown);
      console.log('Error Status: '+textStatus);
    });

  });
});
