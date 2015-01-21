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
    var dataset = dataset_earthquake();

  // Form Data
    $inputs.each(function() {
      field[this.name] = $(this).val();
    });

  // Earthquakes within 'radius', and 'timeframe'

  // Strongest Earthquake

  });
});
