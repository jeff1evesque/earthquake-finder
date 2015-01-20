/**
* load_logic.js: stores HTML form data into jQuery variables, then determine strongest
*                earthquake within provided 'radius', and 'timeframe', respectively.
*/

$(function() {
  $('form').submit(function() {
  // Local Variables
    var field = {};
    var $inputs = $('form input');

  // Form Data
    $inputs.each(function() {
        field[this.name] = $(this).val();
    });
  });
});
