$(document).ready(function(){
	 $(".protocol-form")
		 .on("click", ".add-excused", function(){
	      var newTeamMemberHtml = $("#new-excused").html();
	      // use underscore if any placeholders
		  $(newTeamMemberHtml).insertBefore("#excused-control");
		})
		.on("click", ".remove-excused", function(){
		  $(this).parent().remove();
		})
			.on("click", ".add-absent", function(){
		  var newTeamMemberHtml = $("#new-absent").html();
		  // use underscore if any placeholders
		  $(newTeamMemberHtml).insertBefore("#absent-control");
		})
		.on("click", ".remove-absent", function(){
		  $(this).parent().remove();
		})
		.on("click", ".add-attendents", function(){
		  var newTeamMemberHtml = $("#new-attendents").html();
		  // use underscore if any placeholders
		  $(newTeamMemberHtml).insertBefore("#attendents-control");
		})
		.on("click", ".remove-attendents", function(){
		  $(this).parent().remove();
		})
		.on("click", ".add-field", function(){
		  var newTeamMemberHtml = $("#new-field").html();
		  // use underscore if any placeholders
		  $(newTeamMemberHtml).insertBefore($(this));
		  $(this).remove();
		})
});