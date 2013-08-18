(function($, window, _, undefined){
	
	$(function() {
		jQuery.extend(jQuery.validator.messages, {
			required : "Това поле е задължително",
			minlength : jQuery.validator.format("Моля въведете поне {0} символа")
		});
	});
	
	var appConfig = {
		projectName : "Diaphanum",
		textAreaValidationReq : {
			required: true,
			minlength: 140
		}
	};

	window.Diaphanum = {};
	window.Diaphanum.appConfig = appConfig;
})($, window, _);
