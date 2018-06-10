$(document).ready(function() {
    $('table').addClass('table');
    $('a[href*="/media/"]').each(function () {
        var old_text = $(this).text();
        $(this).html(old_text + ' <i class="fa fa-download"></i>');
    });
});