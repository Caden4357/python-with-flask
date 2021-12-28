$(document).ready(function() {

    $('#submit').click(function()
    {
        var value = $('#selected').val();
        alert($('#browsers [value="' + value + '"]').data('value'));
    });
});