$(function () {

    $('#dialog').dialog({
        autoOpen: false,
        buttons: [
            {
                <!--text: "OK",-->
                <!--click: function() {document.location.href="/basket/add/{{product.id}}"}-->
                <!--},-->
                <!--{-->
                text: "ОТМЕНА",
                click: function () {
                    $(this).dialog("close");
                }
            },
        ],
        draggable: true,
        hide: 'explode',
        show: 'blind',
        modal: true,
        <!--position: ['right', 'center'],-->
        title: 'Добавить в корзину'
    });

    $('#cart').button().click(function () {
        $('#dialog').dialog("open");
    });

    $("#to_cart").on('click', function () {
        $('#cart').val('Товар&nbsp;в&nbsp;корзине');
    });

//      $('#total_quantity').change(function(){
//    $('#bg_popup').css('display', 'block')};

});