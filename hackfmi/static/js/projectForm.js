$(document).ready(function(){
  var
    attachmentsCount = 1,
    maxAttachments = $('#MAX_UPLOAD_FILES').val(),
    maxAttachmentsSize = $('#MAX_UPLOAD_SIZE').val() * 1048576, // We need the value in bytes
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
          .val(data.id)
          .end()
        .end()
        .attr("disabled", "disabled")
        .css("background-color", "#eee") // trigger disabled color
        .unbind() // detach all events
        .parent()
        .find(".project-team")
          .popover("destroy"); // remove any left popover
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
      var
        $closestControlsGroup = $(this).closest(".controls"),
        teamInputCount = $closestControlsGroup.find(".team-member-field").length;

      $(this).parent().remove();

      if(teamInputCount <= 1) {
        // we have removed the last team member input, so we add one
        $closestControlsGroup.find("#add-member-button").trigger('click');
      }
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
    })
    .on("change", ".input-file", function(){
      var currentFileSize = this.files[0].size;
      if(currentFileSize > maxAttachmentsSize) {
        //TODO: Нещо по-умно от .parent().parent().parent() и да работи!
        $(this).parent().parent().parent().popover('show');
      } else {
        $(this).parent().parent().parent().popover('destroy'); 
      }

    })
    .on("click", ".fileupload-exists", function() {
      $(this).parent().parent().popover('destroy'); 
    })
    .on("submit", function() {
      //Validate for members
      var hasError = false;
      $(".team-member-id-container").each(function() {
        if($(this).val() == -1) {
          hasError = true;
          $(this).parent().find(".project-team").popover('show');

          event.preventDefault();
        }
      });
      if (hasError) {
          //Scroll to the filed
          $('html, body').animate({
            scrollTop: $(".project-team").offset().top
          }, 1000);
      };

      //Validate file size
      $(".input-file").each(function() {
        if($(this).val()) {
          var currentFileSize = this.files[0].size;
          if(currentFileSize > maxAttachmentsSize) {
            event.preventDefault();
          }
        }
      });
    });


  $(".project-form").validate({
    // TODO: Fix the bug here
    errorElement : "div",
    errorPlacement: function(error, element){
      error.addClass("alert");
      var elementClasses = element.attr("class").split(" ");

      if(_.contains(elementClasses , "project-team")){
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

  $(".errorFieldName").each(function() {
    var labelName = $("input[name=" + $(this).html() + "]")
                      .closest(".control-group")
                      .find("label.control-label")
                      .html();
    $(this).html(labelName);
  });

  // BUG : Check if there is already a field for team members
  // in case of the edit form
  // create the first input field
  $("#add-member-button").trigger('click');
});
