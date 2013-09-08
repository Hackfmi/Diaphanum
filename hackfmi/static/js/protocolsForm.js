$(document).ready(function(){
	//TODO: Look this for refactoring
	var peopleList = {
		".excused-member-field": [],
		".absent-member-field": [],
		".attendents-member-field": []
	};

	var
		TypeAheader = window.Diaphanum.TypeAheader,
		typeAheadConfig = {
			template : $("#person-autocomplete-template").html(),
			name : "names" + _.uniqueId()
		};

	var typeAheadCallbackCreator = function(closestFieldContainerClass, idContainerClass) {
		return function(data) {
			var canBeAdd = true;
			//Check if the person is already added.	
			_.each(peopleList, function(item, index) {
				if(_.indexOf(item, data.id) != -1) {
					canBeAdd  = false;
					return;
				}
			});

			if(!canBeAdd) {
				$(this)
					.popover('show')
					.parent().addClass("has-error");
				return;
			}
			$(this)
				.closest(closestFieldContainerClass)
				.find("input" + idContainerClass)
				.val(data.id);

			$(this)
				.attr("disabled", "disabled")
				.css("background-color", "") /* typeahead adds transperant background*/
				.popover('hide')
				.parent().removeClass("has-error");

			peopleList[closestFieldContainerClass].push(data.id);
		};
	};

	var excusedCallback = typeAheadCallbackCreator(".excused-member-field", ".excused-id-container");
	var absentCallback = typeAheadCallbackCreator(".absent-member-field", ".absent-id-container");
	var attendentsCallback = typeAheadCallbackCreator(".attendents-member-field", ".attendents-id-container");
	
	var topicsCount = 1; //TODO: Check if it is posible to have protocol with no topics
	var utils = window.Diaphanum.utils;

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
		.on("click", ".add-absent", function(){
			var newAbsentFieldHtml = $("#new-absent").html();
			// use underscore if any placeholders
			$(newAbsentFieldHtml).insertBefore("#absent-error");

			TypeAheader.feed(
				$("input.autocomplete.absent").not(".tt-query"),
				typeAheadConfig,
				absentCallback );
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
		.on("click", ".remove-person", function(){
			var
				$parent = $(this).parent(),
				fieldName = "." + $parent.attr("class"),
				idToRemove = parseInt($parent.find("input[type=hidden]").val(), 10);


			peopleList[fieldName] = _.without(peopleList[fieldName], idToRemove);
			$parent.remove();
		})
		.on("click", ".add-field", function(){
			var newAddMoreFieldHtml = $("#new-field").html();
			// use underscore if any placeholders
			$(newAddMoreFieldHtml).insertBefore($(this));
			$(this).remove();
		})
		.submit(function(){
			var
				topicIndex = 0,
				voteSections = 0;

			/*
				Backend name formats:
				topics-0-name
				topics-1-name
				...
				topics-n-name
			*/
			$(".topic").each(function() {
				$(this).attr("name", "topics-" + topicIndex + "-name");
				topicIndex += 1;
			});

			/*
				Backend name formats:
				topics-0-voted_for
				topics-0-voted_against
				topics-0-voted_abstain
				topics-0-statement
				...
				topics-n-voted_for
				topics-n-voted_against
				etc.
			*/
			$(".vote-section").each(function() {
				$(this).find(".topics-voted-for").attr("name", "topics-" + voteSections + "-voted_for");
				$(this).find(".topics-voted-against").attr("name", "topics-" + voteSections + "-voted_against");
				$(this).find(".topics-voted_abstain").attr("name", "topics-" + voteSections + "-voted_abstain");
				$(this).find(".topic-statement").attr("name", "topics-" + voteSections + "-statement");
				voteSections += 1;
			});

			$("input[name='topics-TOTAL_FORMS']").val(voteSections);
		})
		.validate({
			// TODO: Fix the bug here
			errorElement : "div",
			errorPlacement: function(error, element){
				error.addClass("alert");
				var elementClasses = element.attr("class").split(" ");

				if(_.contains(elementClasses , "project-team")){
					console.log(error, element);
					$("#members-error")
					.html("")
					.append(error);
				} else {
					error.insertAfter(element);
				}
			}
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
			topicsCount++;
		};

		var removeTopicFromVote = function(topicIndex) {
			var
				selectorTemplate = ".topic-vote-container > .controls > ol > li:nth-child(<%= topicIndex %>)",
				compiledSelector = _.template(selectorTemplate, {
				topicIndex : topicIndex + 1 // n-th child starts from index 1
			});

			$(compiledSelector).remove();
			topicsCount--;
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
				var index = $(this).parent().topicIndexex();
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