$(document).ready(function(){
    $('.hero-carousel').slick({
        infinite: true,
        draggable: true,
        autoplay: true,
        autoplaySpeed: 4000,
        fade: true,
        responsive: [
            {
                breakpoint: 600,
                settings: {
                    arrows: false,
                    dots:true,
                    adaptiveHeight: true
                }
                }
        ]
    });
    $('.background-image').css({'visibility':'visible'})
});

$(document).ready(function(){
    $('.testimonials').slick({
        centerMode: true,
        centerPadding: '100px',
        autoplay: true,
        autoplaySpeed: 5000,
        infinite: true,
        slidesToShow: 2,
        slidesToScroll: 2,
        arrows: false,
        dots:true,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    adaptiveHeight: true,
                    slidesToShow: 1,
                    slidesToScroll: 1
                },
                },
                {
                    breakpoint: 600,
                    settings: {
                        adaptiveHeight: true,
                        slidesToShow: 1,
                        slidesToScroll: 1,
                        centerMode: false,

                    },
                }
        ]
    });
});

$(document).ready(function(){
    $('.blog').slick({
        centerPadding: '100px',
        autoplay: true,
        autoplaySpeed: 5000,
        infinite: true,
        slidesToShow: 4,
        slidesToScroll: 2,
        arrows: false,
        dots:true,
        responsive: [
                        {
                breakpoint: 1024,
                settings: {
                    adaptiveHeight: true,
                    slidesToShow: 2,
                    slidesToScroll: 2
                },
                },
                {
                breakpoint: 600,
                settings: {
                    adaptiveHeight: true,
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    centerMode: false,
                },
                }
        ]
    });
});

      // cssEase: 'linear',
                // useTransform: false,