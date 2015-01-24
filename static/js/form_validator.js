/**
 * @form_validator.js: call 'validate()' method on defined form elements.
 *
 *     http://jqueryvalidation.org/documentation/
 *     http://jqueryvalidation.org/category/validator/
 *     http://jqueryvalidation.org/jQuery.validator.addMethod/
 *     http://stackoverflow.com/questions/10843399#answer-10843593
 */

/**
 * Custom Method: callback function(s) used from the 'Compound Class Rules',
 *                and the 'Validation' sections (see below).
 */
  jQuery.validator.addMethod(
    'intOnly',
    function(value, element, parameter) {
      if ( Math.round(parseInt(value)) === parseInt(value) ) return true;
      else return false;
  });
  jQuery.validator.addMethod(
    'positiveNumber',
    function(value, element, parameter) {
      if Number(value) > 0 return True;
      else return false;
  });

/**
 * Validation: validates form elements by the 'name' attribute. This validation
 *             may implement the 'Definition(s)', defined from the 'addmethod'
 *             definition.
 */
  $(document).ready(function() {

    $('form').validate({
      rules: {
        gps_longitude: {
          required: true,
          number: true,
          range: [-180, 180]
        },
        gps_latitude: {
          required: true,
          number: true,
          range: [-90, 90]    
        },
        gps_dataset: {
          required: true,
          url: true
        },
        gps_radius: {
          required: true,
          positiveNumber: true
        },
        daysBack: {
          required: true,
          intOnly: true,
          positiveNumber: true
        },
      },
      messages: {
        gps_longitude: 'Not within valid range [-180, 180]',
        gps_latitude: 'Not within valid range [-90, 90]',
        gps_dataset: 'Not valid url',
        gps_radius: 'Not valid position value',
        daysBack: 'Not valid positive integer',
      },
    });
  });
