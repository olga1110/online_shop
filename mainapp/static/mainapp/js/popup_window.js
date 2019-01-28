$(document).ready(function(){
    var pp = $("#pp"),
        bg = $("#pp-bg");

    function pp_hide(pp, bg){
        pp.animate({top: "-550px"}, 1000, function(){bg.fadeOut(1000);});
    }

    function pp_show(pp, bg){
        pp.animate({top: "150px"}, 2000);
        bg.fadeIn(1000).click(function(){pp_hide(pp, bg)});
    }

    if ( $.cookie('visit') == undefined ){
        $.cookie('visit', true);
        pp_show(pp, bg);
    }

    $('.btn-blob').click(function() {
    $(this).toggleClass('blob');
    $('#pp').css('display', 'none');
    });

});