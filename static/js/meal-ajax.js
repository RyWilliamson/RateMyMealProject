$('#likes').click(function(){
    var recipeid;
    recipeid = $(this).attr("data-recipeid");
    $.get('/meal/like/', {recipe_id: recipeid}, function(data){
        $('#like_count').html(data);
             $('#likes').hide();
    });
});
