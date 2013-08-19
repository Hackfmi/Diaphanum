$(document).ready(function() {
	$(".protocolForm").validate({
		rules : {
			number : {
				required : true
			},
			institution : {
				required : true
			},
			conducted_at : {
				required : true
			},
			scheduled_time:{
				required : true
			},
			quorum: {
				required : true
			}
			start_time :{
				required : true
			}
			reportContent : window.Diaphanum.appConfig.textAreaValidationReq
		}
	});
});