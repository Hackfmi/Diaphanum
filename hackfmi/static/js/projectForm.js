$(document).ready(function(){
  var
    attachmentsCount = 0,
    maxAttachments = 10,
    createNewTypeAhead = function() {},
    textAreaValidationReq = window.Diaphanum.appConfig.textAreaValidationReq,
    TypeAheader = window.Diaphanum.TypeAheader,
    typeAheadConfig = {
      template : $("#team-member-autocomplete-template").html(),
      name : "names" + _.uniqueId()
    },
    typeAheadSelectCallback = function(data){
      $(this)
        .closest(".team-member-field")
        .find("input.team-member-id-container")
        .val(data.id);
    },
    utils = window.Diaphanum.utils,
    setAddMoreFilesButtonState = function(numberOfFiles){
      var
        $oneMoreFileButton = $("#add-one-more-file");

      if(numberOfFiles >= maxAttachments){
        $oneMoreFileButton
          .attr("disabled", "disabled")
          .html($("#max-files-reached-template").html());
      } else {
        $oneMoreFileButton
          .removeAttr("disabled")
          .html($("#add-one-more-file-template").html());
      }
  };

  $(".project-form")
    .on("click", "#add-member-button", function(){
      var newTeamMemberHtml = $("#new-team-member-template").html();
      // use underscore if any placeholders
      $(newTeamMemberHtml).insertBefore("#members-error");
      // .not("tt-query") to select all that are not yet typeaheads
      TypeAheader.feed($("input.autocomplete").not(".tt-query"),
                        typeAheadConfig,
                        typeAheadSelectCallback);
    })
    .on("click", ".remove-team-member", function(){
      $(this).parent().remove();
    })
    .on("click", "#add-one-more-file", function(){
      var newAttachmentHtml = $("#new-attachment-template").html();
      // use underscore if any placeholders
      $(newAttachmentHtml).insertBefore("#add-one-more-button-container");
      attachmentsCount += 1;
      setAddMoreFilesButtonState(attachmentsCount);
    })
    .on("click", ".remove-attachment", function(){
      $(this).parent().remove();
      attachmentsCount -= 1;
      setAddMoreFilesButtonState(attachmentsCount);
    });

  $(".project-form").validate({
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
      }
      else{
        error.insertAfter(element);
      }
    },
    rules: {
      name: utils.validationRequirementsFromAttributes("name"),
      mol: utils.validationRequirementsFromAttributes("mol"),
      description: utils.validationRequirementsFromAttributes("description"),
      targets : utils.validationRequirementsFromAttributes("targets"),
      tasks : utils.validationRequirementsFromAttributes("tasks"),
      target_group : utils.validationRequirementsFromAttributes("target_group"),
      schedule : utils.validationRequirementsFromAttributes("schedule"),
      resources : utils.validationRequirementsFromAttributes("resources"),
      finance_description : utils.validationRequirementsFromAttributes("finance_description")
    }
  });
  
  TypeAheader.feed($("input.autocomplete"), typeAheadConfig , typeAheadSelectCallback);

  $(".autocomplete").rules("add", {
    required: true,
    minlength: 2
  });
});
