var upload_s
$(function() {
    upload_s = setInterval('upload_success()', 3000)
});

function form_submit() {
    if (!$('#id_title').val()) {
        return false
    }
    var data   = $('#gallery_form').serialize();
    $('#save_gallery').attr('disabled', true);
    $.ajax({
        type: 'POST',
        url: '/fotogallery/add/',
        data: data,
        success: function(html) {
            $("#step1").html('<h4 class="text-success"><i class="fa fa-thumbs-up"></i> Шаг 1. Введите название фотогалереи, ее описание (не обязательно) и дату</h4>');
            $('#step2').show();
        }
    });
};

function upload_success() {
    if ($('li.qq-upload-success').length>0) {
        $('#step2 h4').addClass('text-success').html('<i class="fa fa-thumbs-up"></i> Шаг 2. Выберите фотографии, которые хотите загрузить');
        $('#finfo').html('<div class="alert alert-success"><strong>Фотографии загружены!</strong> Если Вы хотите добавить' +
            ' еще больше фотографий, нажмите красную кнопку еще раз, или просто перетащите файлы.</div>')
        clearTimeout(upload_s);
    }
}
