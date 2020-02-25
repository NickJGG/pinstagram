$(document).ready(function(){
	resizeDivs($('.profile-post'));
	resizeDivs($('.profile-pin'));
	
	$('#profile-picture div').css('width', $('#profile-picture div').css('height'));
	
	$(window).resize(function(){
		resizeDivs($('.profile-post'));
		resizeDivs($('.profile-pin'));
		$('#profile-picture div').css('height', $('#profile-picture div').css('width'));
	});
	
	function resizeDivs(div){
		$(div).each(function(){
			$(this).css('height', $(this).css('width'));
		});
	}
	
	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie != '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = jQuery.trim(cookies[i]);
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) == (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}
	function csrfSafeMethod(method) {
		// these HTTP methods do not require CSRF protection
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}
	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
			}
		}
	});
	
	$("form").submit(function(event){
		var username = $(this).parent().prev().text();
		
		$.ajax({
			 'type': "POST",
			 'url': "follow",
			 'data': {
				'username': username
			 },
			 'dataType': 'json',
			 'success': follow()
		});
		
		return false;
	});
	
	function follow(){		
		console.log($('#follow-btn').text());
		
		if ($('#follow-btn').text() == 'Follow'){
			console.log("follow");
			$('#follow-btn').text('Unfollow');
			$('#user-meta').children('p').eq(1).text(parseInt($('#user-meta').children('p').eq(1).text()) + 1);
		} else {
			console.log("unfollow");
			$('#follow-btn').text('Follow');
			$('#user-meta').children('p').eq(1).text(parseInt($('#user-meta').children('p').eq(1).text()) - 1);
		}
	}
});