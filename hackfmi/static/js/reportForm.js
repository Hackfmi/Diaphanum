$(document).ready(function() {
	$(".report-form").validate({
		rules : {
			reportTo : {
				required : true,
				minlength : 5
			},
			reportFrom : {
				required : true,
				minlength : 5
			},
			reportContent : window.Diaphanum.appConfig.textAreaValidationReq
		}
	});
});