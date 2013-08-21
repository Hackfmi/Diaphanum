$(document).ready(function() {
	$(".loginForm").validate({
		rules : {
			username : {
				required : true,
				minlength : 2
			},
			password : {
				required : true,
				minlength : 2
			}
		}
	});
});