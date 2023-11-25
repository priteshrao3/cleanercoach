// hero slider
$('.hero-slider').owlCarousel({
    loop: true,
    nav: false,
    dots: true,
    margin: -1,
    autoplay: true,
    autoplayHoverPause: true,
    autoplayTimeout: 5000,
    items: 1,
    navText: [
        "<i class='far fa-long-arrow-left'></i>",
        "<i class='far fa-long-arrow-right'></i>"
    ],
});

$('.hero-slider').on('change.owl.carousel', function (event) {
    new WOW().init();
});



// hero slider 2
$('.hero-slider2').owlCarousel({
    loop: true,
    nav: true,
    dots: false,
    margin: 0,
    autoplay: true,
    autoplayHoverPause: true,
    autoplayTimeout: 5000,
    items: 1,
    navText: [
        "<i class='fal fa-long-arrow-left'></i>",
        "<i class='fal fa-long-arrow-right'></i>"
    ],
});

$('.hero-slider2').on('change.owl.carousel', function (event) {
    new WOW().init();
});


$('.col-md-4').smoove({
    offset:'40%'
});

