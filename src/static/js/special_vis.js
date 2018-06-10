function setCookie(name, value, daysToDel) {
    var cookie = name + "=" + encodeURIComponent(value);
    if (typeof daysToDel === "number") {
        cookie += "; max-age=" + (daysToDel*60*60*24);
    }
    cookie += "; path=/";
    document.cookie = cookie;
}

function get_cookie(name) {
    //Извлечение куков по имени
    var matches = document.cookie.match(new RegExp(
        "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : null;
}

function deleteCookie(name) {
    setCookie(name, "", {
        expires: -1
    })
}

function dmuGostSettings() {
    setCookie("uGostSettings", "enable");
    setCookie("uGostfontfordk", "fontsize2");
    setCookie("uGostcolorfordk", "color1");
    location.reload();
}
var dmchecksettings = get_cookie("uGostSettings");

if (dmchecksettings == '' || dmchecksettings == null) {
    $('#infobardm').css({
        display: 'none'
    });
} else {
    $('#infobardm').css({
        display: 'block'
    });
    $('#enableuGost').css({
        display: 'none'
    });
}
if (dmchecksettings == null) {
    $('#infobardm').css({
        display: 'none'
    });
    $('#enableuGost').css({
        display: 'block'
    })
}

var dmcookiesimg = get_cookie ("uGostimgfordk");
if (dmcookiesimg=='imgnone') {
    $(document).ready(function(){
        $("img").addClass("none");
        $("a.dmdisableimage").addClass("dmimageActive");
        $("a.dmenableimage").removeClass("dmimageActive");
        $('div').css({
            background: 'none'
        });
        $('span').css({
            background: 'none'
        });
        $('body').css({
            background: 'none'
        });
        $('table').css({
            background: 'none'
        });
        $('td').css({
            background: 'none'
        });
        $('tr').css({
            background: 'none'
        });
        $('a').css({
            background: 'none'
        });
        $('li').css({
            background: 'none'
        });
        $('ul').css({
            background: 'none'
        });
    });

} else {
    $(document).ready(function(){
        $("img").addClass("");
        $("a.dmenableimage").addClass("dmimageActive");
        $("a.dmdisableimage").removeClass("dmimageActive");
    });
}
function dmfunctsizeone(){
    $('#allEntries').css({
        fontSize:'14px',
        fontWeight: 'normal'
    });
    $('.eTitle a ').css({
        fontSize:'14px',
        fontWeight: 'normal'
    });
    $('.eTitle').css({
        fontSize:'14px',
        fontWeight: 'normal'
    });
    $('.eBlock').css({
        fontSize:'14px',
        fontWeight: 'normal'
    });
    $('.dmchangea1').css({
        color:'#ffffff',
        fontSize:'14px',
        background:'#000000'
    });

    $('.dmchangea3').css({
        color:'',
        fontSize:'23px',
        background:'normal'
    });

    $('.dmchangea2').css({
        color:'',
        fontSize:'18px',
        background:'normal'
    });
    $(document).ready(function(){
        $("a.dmchangea1").addClass("dmchangeaActive");
        $("a.dmchangea2").removeClass("dmchangeaActive");
        $("a.dmchangea3").removeClass("dmchangeaActive");
    });
    setCookie("uGostfontfordk", "fontsize1");
    location.reload();
}
function dmfunctsizetwo(){
    $('#allEntries').css({
        fontSize:'18px',
        fontWeight: 'bold'
    });
    $('.eTitle a ').css({
        fontSize:'18px',
        fontWeight: 'bold'
    });
    $('.eTitle').css({
        fontSize:'18px',
        fontWeight: 'bold'
    });
    $('.eBlock').css({
        fontSize:'18px',
        fontWeight: 'bold'
    });
    $('.dmchangea3').css({
        color:'',
        fontSize:'23px',
        background:''
    });
    $('.dmchangea1').css({
        color:'',
        fontSize:'14px',
        background:''
    });
    $('.dmchangea2').css({
        color:'#ffffff',
        fontSize:'18px',
        background:'#000000'
    });
    $(document).ready(function(){
        $("a.dmchangea2").addClass("dmchangeaActive");
        $("a.dmchangea1").removeClass("dmchangeaActive");
        $("a.dmchangea3").removeClass("dmchangeaActive");
    });
    setCookie("uGostfontfordk", "fontsize2");
    location.reload();
}
function dmfunctsizethree(){
    $('#allEntries').css({
        fontSize:'23px',
        fontWeight: 'bold'
    });
    $('.eTitle a ').css({
        fontSize:'23px',
        fontWeight: 'bold'
    });
    $('.eTitle').css({
        fontSize:'23px',
        fontWeight: 'bold'
    });
    $('.eBlock').css({
        fontSize:'23px',
        fontWeight: 'bold'
    });
    $('.dmchangea3').css({
        color:'#ffffff',
        fontSize:'23px',
        background:'#000000'
    });
    $('.dmchangea2').css({
        color:'',
        fontSize:'18px',
        background:''
    });
    $('.dmchangea1').css({
        color:'',
        fontSize:'14px',
        background:''
    });
    $(document).ready(function(){
        $("a.dmchangea3").addClass("dmchangeaActive");
        $("a.dmchangea1").removeClass("dmchangeaActive");
        $("a.dmchangea2").removeClass("dmchangeaActive");
    });
    setCookie("uGostfontfordk", "fontsize3");
    location.reload();
}

function dmdisableimage(){
    $('img').css({
        display: 'none'
    });
    $('div').css({
        background: 'none'
    });
    $('span').css({
        background: 'none'
    });
    $('body').css({
        background: 'none'
    });
    setCookie("uGostimgfordk", "imgnone");
    location.reload();
}

function dmenableimage(){
    $('img').css({
        display: 'inherit'
    });
    $("img").addClass("");
    setCookie("uGostimgfordk", "imgyes");
    location.reload();
}

var dmcookiesfont = get_cookie ("uGostfontfordk");


if(dmcookiesfont=='fontsize1' || dmcookiesfont=='fontsize0') {
//делаем все в 15 пикселях
    $("body, div, p, span, h3, a, table, td, tr, tbody, thead, header, footer, section, li, ul").css("font-size", "15px");
    $("h1").css("font-size", "17px");
    $("h2").css("font-size", "16px");
    $("#infobardm, .dmchangea1, .dmchangea2, .dmchangea3, .dmdisableimage, .dmenableimage, .dmcolor1, .dmcolor2, .dmcolor3, .dmcolor4").css("font-size", "15px");

//делаем отступы в 30px
    $("body, div, p, span, h3, a, table, td, tr, tbody, thead, header, footer, section, li, ul").css("line-height", "30px");
    $("h1").css("line-height", "30px");
    $("h2").css("line-height", "30px");
    $("#infobardm, .dmchangea1, .dmchangea2, .dmchangea3, .dmdisableimage, .dmenableimage, .dmcolor1, .dmcolor2, .dmcolor3, .dmcolor4").css("line-height", "30px");

//выделяем текущий пункт
    $(document).ready(function(){
        $("a.dmchangea2").removeClass("dmchangeaActive");
        $("a.dmchangea1").addClass("dmchangeaActive");
        $("a.dmchangea3").removeClass("dmchangeaActive");
    });
} else {
    if (dmcookiesfont=='fontsize2') {  //fontsize2 имеется в виду 18px
        //делаем все в 19 пикселях

        $("body, div, p, span, h3, a, table, td, tr, tbody, thead, header, footer, section, li, ul").css("font-size", "19px");
        $("h1").css("font-size", "21px");
        $("h2").css("font-size", "20px");
        $("#infobardm, .dmchangea1, .dmchangea2, .dmchangea3, .dmdisableimage, .dmenableimage, .dmcolor1, .dmcolor2, .dmcolor3, .dmcolor4").css("font-size", "19px");

//делаем отступы в 35px
        $("body, div, p, span, h3, a, table, td, tr, tbody, thead, header, footer, section, li, ul").css("line-height", "35px");
        $("h1").css("line-height", "35px");
        $("h2").css("line-height", "35px");
        $("#infobardm, .dmchangea1, .dmchangea2, .dmchangea3, .dmdisableimage, .dmenableimage, .dmcolor1, .dmcolor2, .dmcolor3, .dmcolor4").css("line-height", "35px");

//выделяем текущий пункт
        $(document).ready(function(){
            $("a.dmchangea2").addClass("dmchangeaActive");
            $("a.dmchangea1").removeClass("dmchangeaActive");
            $("a.dmchangea3").removeClass("dmchangeaActive");
        });
    } else {
        if (dmcookiesfont=='fontsize3') { //fontsize3 имеется в виду 24px
            //делаем все в 24 пикселях
            $("body, div, p, span, h3, a, table, td, tr, tbody, thead, header, footer, section, li, ul").css("font-size", "24px");
            $("h1").css("font-size", "26px");
            $("h2").css("font-size", "25px");
            $("#infobardm, .dmchangea1, .dmchangea2, .dmchangea3, .dmdisableimage, .dmenableimage, .dmcolor1, .dmcolor2, .dmcolor3, .dmcolor4").css("font-size", "24px");

//делаем отступы в 40px
            $("body, div, p, span, h3, a, table, td, tr, tbody, thead, header, footer, section, li, ul").css("line-height", "40px");
            $("h1").css("line-height", "40px");
            $("h2").css("line-height", "40px");
            $("#infobardm, .dmchangea1, .dmchangea2, .dmchangea3, .dmdisableimage, .dmenableimage, .dmcolor1, .dmcolor2, .dmcolor3, .dmcolor4").css("line-height", "40px");

//выделяем текущий пункт
            $(document).ready(function(){
                $("a.dmchangea2").removeClass("dmchangeaActive");
                $("a.dmchangea1").removeClass("dmchangeaActive");
                $("a.dmchangea3").addClass("dmchangeaActive");
            });
        }
    }
}


function dmcolor1(){
    setCookie("uGostcolorfordk", "color1");
    location.reload();
}
function dmcolor2(){
    setCookie("uGostcolorfordk", "color2");
    location.reload();
}
function dmcolor3(){
    setCookie("uGostcolorfordk", "color3");
    location.reload();

}
var dmcookiescolor = get_cookie ("uGostcolorfordk");

if(dmcookiescolor=='color1') {
    document.write('<link type="text/css" rel="Stylesheet" href="/static/css/style2.css" />');

}
if(dmcookiescolor=='color2') {
    document.write('<link type="text/css" rel="Stylesheet" href="/static/css/style1.css" />');
}
if(dmcookiescolor=='color3') {
    document.write('<link type="text/css" rel="Stylesheet" href="/static/css/style3.css" />');
}
function dmreset(){
    deleteCookie("uGostcolorfordk");
    deleteCookie("uGostfontfordk");
    deleteCookie("uGostimgfordk");
    deleteCookie("uGostSettings");
    location.reload();
}
