/**
* ajax_dataset.js: return parsed dataset from given URL.
*/

/**
 * dataset_earthquake: parse dataset from given url.
 */
  var dataset_earthquake = function(dataset_url) {
    $.ajax({
      url: dataset_url,
      type: 'POST',
      beforeSend: function() {

      }
    }).done(function(data) {

    }).fail(function(jqXHR, textStatus, errorThrown) {
      console.log('Error Thrown: '+errorThrown);
      console.log('Error Status: '+textStatus);
    });
  }
