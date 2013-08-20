(function($, window, _, undefined){
	
	$(function() {
		jQuery.extend(jQuery.validator.messages, {
			required : "Това поле е задължително",
			minlength : jQuery.validator.format("Моля, въведете поне {0} символа"),
			maxlength : jQuery.validator.format("Моля, въведете по-малко от {0} символа")
		});
	});

	var getHostLocation = function() {
		if (getHostLocation.hostLocation === undefined) {
			var loc = window.location;
			getHostLocation.hostLocation = loc.protocol + "//" + loc.hostname + ((loc.port !== undefined) ? ':' + loc.port : '');
		}
		return getHostLocation.hostLocation;
	};
	
	var appConfig = {
		projectName : "Diaphanum",
		textAreaValidationReq : {
			required: true,
			minlength: 140
		},
		nameSearchUrl : getHostLocation() + "/search/"
	};

	window.Diaphanum = {
		appConfig : appConfig,
		utils : {}
	};

	window.Diaphanum.utils.validationRequirementsFromAttributes = function(inputNameValue) {
		var
			inputObject = $("input[name=" + inputNameValue + "]"),
			resultObject = {},
			NONE_VALUE = "None";

		// if no match is found, return an empty object
		if(inputObject.length === 0) {
			return resultObject;
		}

		if ( inputObject.is('[maxlength]') && inputObject.attr("maxlength") !== NONE_VALUE ) {
			resultObject.maxlength = inputObject.attr('maxlength');
		}

		if ( inputObject.is('[minlength]') && inputObject.attr("minlength") !== NONE_VALUE ) {
			resultObject.minlength = inputObject.attr('minlength');
		}

		if ( inputObject.is('[required]') ) {
			resultObject.required = true;
		}

		if ( inputObject.is("input[type=email]") ) {
			resultObject.email = true;
		}

		return resultObject;
	};
})($, window, _);
