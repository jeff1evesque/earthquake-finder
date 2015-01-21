/**
* load_logic.js: stores HTML form data into jQuery variables, then determine strongest
*                earthquake within provided 'radius', and 'timeframe', respectively.
*/

$(function() {
  $('form').on('submit', function(event) {
    event.preventDefault();

  // Local Variables
    var field = {};
    var earthquakes = [];
    var $inputs = $('form input');

  // Form Data
    $inputs.each(function() {
      field[this.name] = $(this).val();
    });

  // Dataset
    var dataset = dataset_parser( field['gps_dataset'] );

  // Earthquakes within 'radius', and 'timeframe'

  // Strongest Earthquake

  });
});