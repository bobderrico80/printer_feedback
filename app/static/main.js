$(function() {

  'use strict';

  $('.text-editable').on('click', editCellText);

  function editCellText() {
    var $cell = $(this);
    $('.text-editable').off('click');
    var oldValue = $cell.text().trim();
    var $inputField = $('<input></input>');
    $inputField.attr('type', 'text').val(oldValue);
    $cell.text('').append($inputField);
    $inputField.focus();
    $inputField.on('blur', function() {
      var newValue = $inputField.val();
      $inputField.remove();
      $cell.text(newValue);
      $('.text-editable').on('click', editCellText);
      if (oldValue !== newValue) {
        // logic to update db here;
        console.log('changed!');
      }
    });
  }

});