function searchSuccess(data, textStatus, jqXHR) {
    $('#search_results').html(data);
}

$(function () {
    $('#search').on('change', function () {
        if ($('#search').val() == '') {
            $('#search_results').empty();
        }
    });
});


