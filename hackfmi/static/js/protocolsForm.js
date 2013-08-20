$(document).ready(function(){

	var createNewTypeAhead = function() {},
    textAreaValidationReq = window.Diaphanum.appConfig.textAreaValidationReq,
    TypeAheader = window.Diaphanum.TypeAheader,
    typeAheadConfig = {
      template : $("#person-autocomplete-template").html(),
      name : "names" + _.uniqueId()
    },
    typeAheadSelectCallback = function(data){
 //    $(this)
	// 	.closest(".absent")
	// 	.find("input.absent-id-container")
	// 	.val(data.id);
	// $(this)
	// 	.closest(".attendents")
	// 	.find("input.attendents-id-container")
	// 	.val(data.id);
	};

	var excusedCallback = function(data) {
	 		console.log(data); //selected datum object
	 		$(this)
	 		  .closest(".excused-member-field")
	 		  .find("input.excused-id-container")
	 		  .val(data.id);
	 	};

	 $(".protocol-form")
		 .on("click", ".add-excused", function(){
	      var newTeamMemberHtml = $("#new-excused").html();
	      // use underscore if any placeholders
		  $(newTeamMemberHtml).insertBefore("#excused-error");

		  TypeAheader.feed(
		  		$("input.autocomplete.excused").not(".tt-query"), 
		  		typeAheadConfig, 
		  		excusedCallback );
		})
		.on("click", ".remove-excused", function(){
		  $(this).parent().remove();
		})
		.on("click", ".add-absent", function(){
		  var newTeamMemberHtml = $("#new-absent").html();
		  // use underscore if any placeholders
		  $(newTeamMemberHtml).insertBefore("#absent-error");
		})
		.on("click", ".remove-absent", function(){
		  $(this).parent().remove();
		})
		.on("click", ".add-attendents", function(){
		  var newTeamMemberHtml = $("#new-attendents").html();
		  // use underscore if any placeholders
		  $(newTeamMemberHtml).insertBefore("#attendents-error");
		})
		.on("click", ".remove-attendents", function(){
		  $(this).parent().remove();
		})
		.on("click", ".add-field", function(){
		  var newTeamMemberHtml = $("#new-field").html();
		  // use underscore if any placeholders
		  $(newTeamMemberHtml).insertBefore($(this));
		  $(this).remove();
		});

	 	TypeAheader.feed($("input.autocomplete.excused"), typeAheadConfig, excusedCallback );
});