$(document).ready(function(){

	var
		TypeAheader = window.Diaphanum.TypeAheader,
		typeAheadConfig = {
			template : $("#person-autocomplete-template").html(),
			name : "names" + _.uniqueId()
		};

	var typeAheadCallbackCreator = function(closestFieldContainerClass, idContainerClass) {
		return function(data) {
			$(this)
				.closest(closestFieldContainerClass)
				.find("input" + idContainerClass)
				.val(data.id);
		};
	};

	var excusedCallback = typeAheadCallbackCreator(".excused-member-field", ".excused-id-container");
	var absentCallback = typeAheadCallbackCreator(".absent-member-field", ".absent-id-container");
	var attendentsCallback = typeAheadCallbackCreator(".attendents-member-field", ".attendents-id-container");
	
	$(".protocol-form")
		.on("click", ".add-excused", function(){
			var newExcusedFieldHtml = $("#new-excused").html();
			// use underscore if any placeholders
			$(newExcusedFieldHtml).insertBefore("#excused-error");

			TypeAheader.feed(
				$("input.autocomplete.excused").not(".tt-query"),
				typeAheadConfig,
				excusedCallback);
		})
		.on("click", ".remove-excused", function(){
			$(this).parent().remove();
		})
		.on("click", ".add-absent", function(){
			var newAbsentFieldHtml = $("#new-absent").html();
			// use underscore if any placeholders
			$(newAbsentFieldHtml).insertBefore("#absent-error");

			TypeAheader.feed(
				$("input.autocomplete.absent").not(".tt-query"),
				typeAheadConfig,
				absentCallback );
		})
		.on("click", ".remove-absent", function(){
			$(this).parent().remove();
		})
		.on("click", ".add-attendents", function(){
			var newAttendentsFieldHtml = $("#new-attendents").html();
			// use underscore if any placeholders
			$(newAttendentsFieldHtml).insertBefore("#attendents-error");

			TypeAheader.feed(
				$("input.autocomplete.attendents").not(".tt-query"),
				typeAheadConfig,
				attendentsCallback);
		})
		.on("click", ".remove-attendents", function(){
			$(this).parent().remove();
		})
		.on("click", ".add-field", function(){
			var newAddMoreFieldHtml = $("#new-field").html();
			// use underscore if any placeholders
			$(newAddMoreFieldHtml).insertBefore($(this));
			$(this).remove();
		});

		// initialize the fist inputs to be typeaheads
		TypeAheader.feed($("input.autocomplete.excused"), typeAheadConfig, excusedCallback);
		TypeAheader.feed($("input.autocomplete.absent"), typeAheadConfig, absentCallback);
		TypeAheader.feed($("input.autocomplete.attendents"), typeAheadConfig, attendentsCallback);

		TypeAheader.feed($("input.autocomplete#institution"), {
			name : "institutions",
			template : $("#institution-autocomplete-template").html(),
			valueKey : "name",
			remote : {
				url : window.Diaphanum.appConfig.institutionSearchUrl + "%QUERY/",
				filter : function(parsedResponse) {
					return parsedResponse;
				}
			}
		}, function(data, event) {
			console.log(data);
			$(this)
				.closest(".controls")
				.find("#institutionIdContainer")
				.val(data.id);
		});

		// will be merged with the top $(".protocol-form")

		var addNewTopicInVote = function() {
			var newTopicVoteHtml = $("#new-topic-vote-template").html();
			$(newTopicVoteHtml).appendTo($(".topic-vote-container > .controls > ol"));
		};

		var removeTopicFromVote = function(topicIndex) {
			var
				selectorTemplate = ".topic-vote-container > .controls > ol > li:nth-child(<%= topicIndex %>)",
				compiledSelector = _.template(selectorTemplate, {
				topicIndex : topicIndex + 1 // n-th child starts from index 1
			});

			$(compiledSelector).remove();
		};

		var updateTopicNameInVote = function(topicIndex, topicName) {
			console.log(topicIndex, topicName);
			var
				selectorTemplate = ".topic-vote-container > .controls > ol > li:nth-child(<%= topicIndex %>) .voteTopic",
				compiledSelector = _.template(selectorTemplate, {
				topicIndex : topicIndex + 1 // n-th child starts from index 1
			});
			$(compiledSelector).val(topicName);
		};
		
		$(".protocol-form")
			.on("click", "#add-new-topic-button", function() {
				console.log("I am being clicked");
				var newTopicHtml = $("#new-topic-template").html();

				$(newTopicHtml).appendTo($(".topics-container"));
				addNewTopicInVote();
			})
			.on("click", ".remove-topic-button", function() {
				var index = $(this).parent().index();
				$(this)
					.parent()
					.remove();
				// update the votes accordingly
				removeTopicFromVote(index);
			})
			.on("keyup", ".topic", function() {
				updateTopicNameInVote($(this).parent().index(), $(this).val());
			});
});