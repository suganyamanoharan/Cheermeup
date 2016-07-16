$(document).ready(function(){
    var edgeFlag = false;
    // On edge hit
    $('.image-container').on('edge', function(event, slick, direction){
      console.log('edge was hit');
    });

    // On before slide change
    $('.image-container').on('beforeChange', function(event, slick, currentSlide, nextSlide){
      if(nextSlide==14) {
        edgeFlag = true;
        console.log("hit end");
      }
    });



    $('.image-container').slick({
        dots: true,
        infinite: false,
        speed: 300,
        slidesToShow: 1,
        centerMode: true,
        variableWidth: true,
        arrows: true,
        centerPadding: '60px',

    });

    $('.slick-next').click(function() {
        console.log("click");
        if (edgeFlag) {
            window.location.href = "../hello";
        }
    });
    
});

