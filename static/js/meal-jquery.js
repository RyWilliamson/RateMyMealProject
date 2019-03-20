$(document).ready(function() {
	$('#likes').click(function(){
	var recipeid;
	recipeid = $(this).attr("data-recid");
	$.get('meal/like/', {recipe_id: recipeid}, function(data){
		$('#like_count').html(data);
		$('#likes').hide();
	});
	location.reload();
});
