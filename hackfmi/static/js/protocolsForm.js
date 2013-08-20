$(document).ready(function(){

	var createNewTypeAhead = function() {},
    textAreaValidationReq = window.Diaphanum.appConfig.textAreaValidationReq,
    TypeAheader = window.Diaphanum.TypeAheader,
    typeAheadConfig = {
      template : $("#person-autocomplete-template").html(),
      name : "names" + _.uniqueId()
    };

	var excusedCallback = function(data) {
	 		console.log(data); //selected datum object
	 		$(this)
	 		  .closest(".excused-member-field")
	 		  .find("input.excused-id-container")
	 		  .val(data.id);
	 };

	 var absentCallback = function(data) {
	 	$(this)
	 	  .closest(".absent-member-field")
	 	  .find("input.absent-id-container")
	 	  .val(data.id);
	 };

	 var attendentsCallback = function(data) {
	 	$(this)
	 	  .closest(".attendents-member-field")
	 	  .find("input.attendents-id-container")
	 	  .val(data.id);
	 };

	 $(".protocol-form")
		 .on("click", ".add-excused", function(){
	      var newExcusedFieldHtml = $("#new-excused").html();
	      // use underscore if any placeholders
		  $(newExcusedFieldHtml).insertBefore("#excused-error");

		  TypeAheader.feed(
		  		$("input.autocomplete.excused").not(".tt-query"), 
		  		typeAheadConfig, 
		  		excusedCallback );
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
		  		attendentsCallback );
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

	 	TypeAheader.feed($("input.autocomplete.excused"), typeAheadConfig, excusedCallback );
	 	TypeAheader.feed($("input.autocomplete.absent"), typeAheadConfig, absentCallback );
	 	TypeAheader.feed($("input.autocomplete.attendents"), typeAheadConfig, attendentsCallback );
});