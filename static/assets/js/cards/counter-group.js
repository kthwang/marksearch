// -----------------------------------------------------------------------------
// Titles: Active Sessions, Add to cart, Newsletter Sign Ups, Total Revenue
// Location: index.html
// -----------------------------------------------------------------------------

(function(window, document, $, undefined) {
  "use strict";
  $(function() {
    $(".progress-active-sessions .progress-bar").animate({
      width: "60%"
    }, 400);
    $(".progress-add-to-cart .progress-bar").animate({
      width: "57%"
    }, 400);
    $(".progress-new-account .progress-bar").animate({
      width: "10%"
    }, 400);
    $(".progress-total-revenue .progress-bar").animate({
      width: "50%"
    }, 400);

  });

})(window, document, window.jQuery);
