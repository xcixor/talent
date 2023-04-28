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
                    dots:true
                }
                }
        ]
    });
    $('.background-image').css({'visibility':'visible'})
});

      // cssEase: 'linear',
                // useTransform: false,