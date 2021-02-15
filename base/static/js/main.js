$(document).ready(function () {
    $('menu-toggler').on('click', function () {
        $(this),ToggleClass('open');
        $('.top-nav'),ToggleClass('open');
    });
});