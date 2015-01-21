/**
 * retriever_dataset.js: parses dataset from given url.
 */

/**
 * dataset_parser: parses the source code for the given url.
 */
  var dataset_parser = function(url) {
    var form_data = $('form').serialize();

    $.ajax({
      type: 'POST',
      url: '/json_scraper/',
      data: form_data,
      beforeSend: function() {

      }
    }).done(function(data) {
      console.log( JSON.stringify( data ) );
    }).fail(function(jqXHR, textStatus, errorThrown) {
      console.log('Error Thrown: '+errorThrown);
      console.log('Error Status: '+textStatus);
    });
  }
