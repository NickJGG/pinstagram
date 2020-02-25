$(document).ready(function(){
	var img, rect, ctrl;
	
	$('.image img').on('mousemove', function(e){
		if (ctrl){			
			rect = new rectangle(img.offset().left, img.offset().top, $(this).width(), $(this).height());
			
			var i = $('#img-zoom');
			
			i.css('display', 'block');
			
			i.css({'top': e.pageY - 125 + 'px', 'left': e.pageX - 125 + 'px'});
		}
		
		img = $(this);
		
		var i = $('#img-zoom');
		var posX = img.offset().left;
		var posY = img.offset().top;
		
		i.css('background-image', 'url("' + $(this).prop('src') + '")');
		i.css('background-size', $(this).width() * 2 + 'px ' + $(this).height() * 2 + 'px ');
		i.css('background-position', (-posX * 2) + 'px ' + (-posY * 2) + 'px');
	});
	
	$('.image img').on('mouseleave', function(e){
		if ($(this) == img){
			$('#img-zoom').css({'display': 'none', 'top': '-250px', 'left': '-250px'});
		}
	});
	
	$('#img-zoom').on('mousemove', function(e){
		if (ctrl && rect.contains(e.pageX, e.pageY)){
			var posX = e.pageX - img.offset().left - (125 / 2);
			var posY = e.pageY - img.offset().top - (125 / 2);
			
			$(this).css('background-position', (-posX * 2) + 'px ' + (-posY * 2) + 'px');
			$(this).css({'top': e.pageY - 125 + 'px', 'left': e.pageX - 125 + 'px'});
		} else {
			console.log('exited div');
			
			$(this).css({'display': 'none', 'top': '-250px', 'left': '-250px'});
		}
	});
	
	$(window).keydown(function(e){
		 if (e.which == 17)
			ctrl = true;
	}).keyup(function(e) {
		if (e.which == 17)
			ctrl = false;
	});
	
	$(document).on('mouseover', '.comment-delete img', function(){
		console.log('enter');
		
		$(this).attr('src', $(this).attr('src').replace('delete', 'delete-hover'));
	}).on('mouseleave', '.comment-delete img', function(){
		$(this).attr('src', $(this).attr('src').replace('delete-hover', 'delete'));
	});
	
	$('.comment-delete').on('click', function(){
		var comment_id = $(this).attr('class').replace(' ', '').replace('comment-delete', '');
		console.log(comment_id);
		
		$(this).parent().remove();
		
		$.ajax({
			 'type': "POST",
			 'url': location.protocol + "//" + location.host + "/" + comment_id + "/delete",
			 'dataType': 'json',
			 'success': function(resp){
				 console.log('success');
				 $(this).parent().find(comment_id).remove();
			 }
		});
		
		$(this).parent().find(comment_id).remove();
	});
	
	function rectangle (x, y, w, h) {
		this.x = x;
		this.y = y;
		this.width = w;
		this.height = h;

		this.contains = function (x, y) {
			return this.x <= x && x <= this.x + this.width &&
				   this.y <= y && y <= this.y + this.height;
		}
	}
	
	$('.right').on('click', function(){
		$(this).find('.choose-board').css('display', 'flex');
	});
	
	
	
	
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
	
	$('.comment-form input').on('keypress', function(e){
		if (e.which == 13){
			console.log("enter");
			//$(this).parent().submit();
		}
	});
	
	$(".left form").submit(function(event){
		var post_id = parseInt($(this).attr('class'));
		
		var par = $('.' + post_id);
		var img = $('.' + post_id + " button img");
		var div = $(par).siblings('p')[0];
		var liked = $(img).attr('src').indexOf('like-red') != -1;
		
		console.log($(img).attr('src').indexOf('like-red'));
		
		if (liked){
			$(div).text(parseInt($(div).text()) - 1);
			
			$(img).attr('src', $(img).attr('src').replace('like-red', 'like'));
		} else {
			$(div).text(parseInt($(div).text()) + 1);
			
			$(img).attr('src', $(img).attr('src').replace('like', 'like-red'));
		}
	
		$.ajax({
			 'type': "POST",
			 'url': location.protocol + "//" + location.host + "/" + post_id + "/like",
			 'data': {
				//'post_id': parseInt($(this).attr('id'))
			 },
			 'dataType': 'json',
			 'success': function(resp){
				 like(resp.like == 'true', post_id);
			 }
		});
		
		return false;
	});
	$(".comment-form").submit(function(event){
		var post_id = parseInt($(this).attr('class'));
	
		var par = $('.' + post_id);
		var div = $(par).siblings('p')[0];
		
		var temp = $(this);
	
		$.ajax({
			 'type': "POST",
			 'url': location.protocol + "//" + location.host + "/" + post_id + "/comment",
			 'data': {
				'text': $(this).children('input').eq(1).val()
			 },
			 'dataType': 'json',
			 'success': function(resp){
				 comment(temp, resp.username, $(temp).children('input').eq(1).val(), resp.comment_id);
			 }
		});
		
		return false;
	});
	$('.right').on('click', function(e){
		var post_id = $(this).attr('class').split(' ')[0];
		var pinned = $(this).find('img').attr('src').indexOf('pin-filled') != -1;
		
		console.log($(this).find('img').attr('src'));
		
		if (pinned){
			$(this).find('img').attr('src', $(this).find('img').attr('src').replace('pin-filled', 'pin'));
		} else {
			$(this).find('img').attr('src', $(this).find('img').attr('src').replace('pin', 'pin-filled'));
		}
		
		$.ajax({
			 'type': "POST",
			 'url': location.protocol + "//" + location.host + "/pin/" + post_id,
			 'data': {
				
			 },
			 'dataType': 'json',
			 'success': function(resp){
				
			 }
		});
	});
	
	function comment(div, username, te, commentID){
		var com = createComment();
		$(div).parent().siblings('.comments').append(com);
		console.log($(div).parent().siblings('.comments').children());
		
		var c = $(div).parent().siblings('.comments').children().last();
		
		$(c).find('.username').find('a').text(username);
		$(c).find('.text').html(te);
		$(c).find('.comment-delete').addClass(commentID);
		
		$(div).children('input').eq(1).val('');
	}
	function like(liked, post_id){
		
	}
});