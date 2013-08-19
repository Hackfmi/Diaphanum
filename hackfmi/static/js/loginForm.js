$(document).ready(function() {
	$(".loginForm").validate({
		username : {
			required : true,
			minlength : 30
		},
		password : {
			required : true
		}
	});
});