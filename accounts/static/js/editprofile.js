$(document).ready(function(){	
	function resizeDiv(){
		$('.post-img').each(function(){
			$(this).css('height', $(this).css('width'));
		});
	}
	
	resizeDiv();
	
	$(document).resize(function(){
		resizeDiv();
	});

	$("#upload-btn").change(function() {
		$.ajax({
			 'type': "POST",
			 'url': "pic/",
			 'data': {
				'username': username
			 },
			 'dataType': 'json',
			 'success': follow()
		});
	});
	
	$('.post-img').on('click', function(){
		var add = !($(this).hasClass('post-selected'));
		
		$('.post-img').each(function(){
			$(this).removeClass('post-selected');
		});
		
		if (add){
			$(this).addClass('post-selected');
		}
	});
	
	$('#prof-pic-submit').on('click', function(){
		$('#post-select').css('visibility', 'hidden');
		
		$('.post-img').each(function(){
			if ($(this).hasClass('post-selected')){
				var post_id = $(this).attr('class').split(' ')[0];
				
				$.ajax({
					'type': "POST",
					'url': "/accounts/edit/pic/" + post_id,
					'data': {
						
					},
					'dataType': 'json',
					//'success':
				});
			}
		});
		
		location.reload();
	});
	
	$('#upload-btn p').on('click', function(){
		$('#post-select').css('visibility', $('#post-select').css('visibility') == 'hidden' ? 'visible' : 'hidden');
	});
	
	$(document).on('click', function(e){
		var div = $('#post-select');
		
		if (!div.is(e.target) && div.has(e.target).length == 0 && !$('#upload-btn p').is(e.target)){
			$('#post-select').css('visibility', 'hidden');
		} else {
			console.log(!div.is(e.target));
			console.log(!div.is($('#upload-btn p')));
		}
	});
});