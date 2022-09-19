$(document).ready(function(){
    $("#toggle_header").on({
        click: function(){
            const clase = ($('header').attr('class'));
            console.log(clase);
            if(clase === 'green'){
                $('header').removeClass("green");
                $('header').addClass("red");
            }else{
                $('header').removeClass("red");
                $('header').addClass("green");
            }
        }
      });
});
