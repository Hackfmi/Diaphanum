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
		},
		nameSearchUrl : "http://localhost:8000/search/"
	};

	window.Diaphanum = {};
	window.Diaphanum.appConfig = appConfig;
	window.Diaphanum.validationRequirementsFromAttributes=function(inputNameValue) {
		var inputObject=$("input[name="+inputNameValue+"]");
		var resultObject = {};

		if ( inputObject.is('[maxlength]') ) {
			resultObject.maxlength=inputObject.attr('maxlength');
		}

		if ( inputObject.is('[minlength]') ) {
			resultObject.minlength=inputObject.attr('minlength');
		}

		if ( inputObject.is('[required]') ) {
			resultObject.required=true;
		}

		if ( inputObject.is("input[type=email]") ) {
			resultObject.email=true;
		}

		return resultObject;
	};
})($, window, _);
