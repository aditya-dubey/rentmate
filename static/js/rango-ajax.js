/**
 * Created by admin on 06-11-2016.
 */
$('.likes').click(function(){
    var p_id;
    p_id = $(this).attr("data-catid");
    $.get('/send_mail/', {post_id: p_id}, function(){
        $(this).hide();
        alert("Your request has been sent to the dealer with your details(name,age,email).If intrested he will contact you. ")
    });
});