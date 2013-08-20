(function($, window, _, undefined){
	var TypeAheader = {};

	var defaultOptions = {
		name : "dataset" + _.uniqueId(),
		valueKey : "value",
		remote: {
			url : window.Diaphanum.appConfig.nameSearchUrl + "%QUERY/",
			filter : function(parsedResponse) {
				_.map(parsedResponse, function(item) {
					item.value = item.full_name + " " + item.faculty_number;
				});
				return parsedResponse;
			}
		},
		engine : {
		// using underscore as a templating engine
		compile : function(template) {
				var compiled = _.template(template);
				return {
					render : function(context) {
						return compiled(context);
					}
				};
			}
		}
	};

	TypeAheader.feed = function($elements, options, selectCallback) {
		_.extend(defaultOptions, options);
		$elements
			.typeahead(defaultOptions)
			.on("typeahead:selected", function(evt, data) {
				selectCallback.call(this, data, evt);
			});
	};

	if(typeof window.Diaphanum === "undefined") {
		throw new Error("Please, include after appConfig.js");
	}
	// should be included after appConfig.js
	window.Diaphanum.TypeAheader = TypeAheader;
})($, window, _);