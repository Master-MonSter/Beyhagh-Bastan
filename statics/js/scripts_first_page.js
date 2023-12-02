    function firstLoad() {
        $(".ml_bg-item").addClass("mgl_vis");
        TweenMax.to(".ml-mask", 1.7, {
            xPercent: 100,
            repeat: 0,
            yoyo: false,
            repeatDelay: 0.5,
            ease: Linear.easeNone,
            onComplete: function () {
                $(".ml_bg-item , .ml-wrap img").addClass("mgl_clos");
                $(".main-loader").delay(500).fadeOut(1300);
            }
        });
    }
    firstLoad();



var bgImage = $(".bg");
    bgImage.each(function(a) {
        if ($(this).attr("data-bg")) $(this).css("background-image", "url(" + $(this).data("bg") + ")");
}); 
$(".lrt").on({
	mouseenter: function () {
		$(".dark-ver").addClass("vis-dark");
	} 
	}); 
$(".drt").on({
	mouseenter: function () {
		$(".dark-ver").removeClass("vis-dark");
	} 
});
$('head').append('<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">');
document.addEventListener('gesturestart', function (e) {
    e.preventDefault();
});