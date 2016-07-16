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
            window.location.href = "../";
        }
    });

    $('#dislike-btn').click(function() {
        var imgUrl = $('.slick-current img').prop('src');
        var tag = imgUrl.split("/")[5];
        var data = {value:"dislike", tag:tag};
        console.log(tag);
    
        $.ajax("/likes-handler", {
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify(data),
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        })
    });

    $('#like-btn').click(function() {
        var imgUrl = $('.slick-current img').prop('src');
        var tag = imgUrl.split("/")[5];
        console.log(tag);
        var data = {value:"like", tag:tag};
        
        $.ajax("/likes-handler", {
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify(data),
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        })
    });

    $('#personal-btn').click(function() {
        window.location.href = "/personal";
    });

    $('#interests-btn').click(function() {
        window.location.href = "/interests";
    });
    
});

