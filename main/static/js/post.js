$(document).ready(function(){
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
	
	$("#follow-btn").on('click', function(event){
		var username = $(this).prev().text()
		
		$.ajax({
			 'type': "POST",
			 'url': location.protocol + "//" + location.host + "/" + username + "/follow",
			 'data': {
				'username': username
			 },
			 'dataType': 'json',
			 'success': function (){		
				console.log($('#follow-btn').text());
				
				if ($('#follow-btn').text() == 'Follow'){
					$('#follow-btn').text('Unfollow');
				} else {
					$('#follow-btn').text('Follow');
				}
			}
		});
		
		return false;
	});
});