//////////////////////////////
/// javascripts for Posts page
//////////////////////////////

$(function() {
    // Executed when js-menu-icon js clicked
    $('.js-menu-icon').click(function() {
        ////$ (this) : Self element, namely div. js-menu-icon
        // next     
        $(this).next().toggle();
    })
})
