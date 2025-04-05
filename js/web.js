$(function(){
    $.ajaxSetup({
        headers: {
            'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
        }
    });
    $("#contactUs").submit(function(event) {
        $('.err').text('');
        $('.form-control').css('border-color','green');
        event.preventDefault();
        formdata = new FormData($(this)[0]);
        $.ajax({
            url: $(this).attr('action'),
            contentType: false,
            processData: false,
            cache:false,
            data: formdata,
            type: $(this).attr('method'),
            beforeSend: function() {
                $("#overlay").fadeIn(300);
            },complete: function() {
                $("#overlay").fadeOut(300);
                
            },
            success: function(response){
            if(response.status){
                $('#contactUs')[0].reset();
                $(".submitted_success").css('color','green').text(response.message);
                setTimeout(function() {
                    $(".submitted_success").fadeOut(3000);
                }, 5000);
                
            }else{
                $.each(response.errors, function(key,val) {
                    var fieldElement = $('.err_' + key);
                    fieldElement.css('color','red').text(val[0]);
                    if(key!='message'){
                       $('input[name="'+key+'"], select[name="' + key + '"]').css('border-color','red');
                    }else{
                        $('#message').css('border-color','red').text(val[0]);
                    }
                });
            }
            },

        });
    });
    $('input, textarea').keyup(function(){
        if($(this).val()!=''){
          $(this).siblings('.err').text('');
        }
      })


});