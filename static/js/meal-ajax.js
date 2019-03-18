$(document).ready(function() {
		// JQuery code to be added in here.
		$('#likes').click(function(){
		var recipeid;
		recipeid = $(this).attr("data-recid");
		$.get(r'^category/(?P<category_name_slug>[\w\-]+)/(?P<recipe_name_slug>[\w\-]+)/$', {recipe_id: recipeid}, function(data){
			$('#like_count').html(data);
			$('#like').hide();
		});
});

