(function($, window, _, undefined){
	var appConfig = {
		projectName : "Diaphanum",
		textAreaValidationReq : {
			required: true,
			minlength: 140
		}
	};

	var getConfig = function(configString) {
		var
			configParts = configString.split("."),
			len = configParts.length,
			currentPart = "",
			result = appConfig;

		while(len--) {
			currentPart = configParts.shift();
			result = result[currentPart];
			console.log(result);
		}

		return result;
	};

	window.Diaphanum = {};
	window.Diaphanum.getConfig = getConfig;
})($, window, _);