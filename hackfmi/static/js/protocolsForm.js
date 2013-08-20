$(document).ready(function() {
	$(".protocolForm").validate({
		rules : {
			number : {
				required : true,
				number: true
			},
			institution : {
				required : true
			},
			conducted_at : {
				date: true,
				required : true
			},
			scheduled_time : {
				required : true
			},
			quorum : {
				required : true,
				digits: true
			},
			start_time : {
				required : true
			},
			reportContent : window.Diaphanum.appConfig.textAreaValidationReq
		}
	});
});