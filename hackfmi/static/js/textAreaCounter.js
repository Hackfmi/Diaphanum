$(function() {
	var config = {
		htmlTemplateId : "#text-counter-template",
		minTextAreaLength : window.Diaphanum.appConfig.textAreaValidationReq.minlength
	};
	// set up all text areas
	$("textarea[required]").each(function() {
		var counter = $(config.htmlTemplateId).html();
		$(counter)
			.insertAfter($(this))
			.hide();
	});

	$(document).on("keyup", "textarea", function() {
		var
			$spanCounter = $(this).parent().find("p.textCounter"),
			currentCharsLen = $(this).val().length;

		$spanCounter
			.show()
			.find(".currentChars")
				.html(currentCharsLen)
				.end()
			.find(".minChars")
				.html(config.minTextAreaLength);

		if(currentCharsLen >= config.minTextAreaLength) {
			$spanCounter.hide();
		}
	});
});