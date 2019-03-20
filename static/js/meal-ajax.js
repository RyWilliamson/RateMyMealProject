$(document).ready(function() {
	$('#likes').click(function(){
		var recipeid;
		recipeid = $(this).attr("recid");
		$.get('like/', {recipe_id: recipeid}, function(data){
			$('#like_count').html(data);
		});
		location.reload();
	});
});