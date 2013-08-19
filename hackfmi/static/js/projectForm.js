$(document).ready(function(){
  var
    attachmentsCount = 0,
    maxAttachments = 10,
    setAddMoreFilesButtonState = function() {},
    createNewTypeAhead = function() {},
    textAreaValidationReq = window.Diaphanum.appConfig.textAreaValidationReq,
    TypeAheader = window.Diaphanum.TypeAheader,
    typeAheadConfig = {
      template : $("#teamMemberAutocompleteTemplate").html(),
      name : "names" + _.uniqueId()
    },
    typeAheadSelectCallback = function(data){
    console.log(data); //selected datum object
    $(this)
      .closest(".teamMemberField")
      .find("input.teamMemberIdContainer")
      .val(data.id);
    };

  setAddMoreFilesButtonState = function(numberOfFiles){
    var
      $oneMoreFileButton = $("#addOneMoreFile");

    if(numberOfFiles >= maxAttachments){
      $oneMoreFileButton
        .attr("disabled", "disabled")
        .html($("#maxFilesReachedTemplate").html());
    } else {
      $oneMoreFileButton
        .removeAttr("disabled")
        .html($("#addOneMoreFileTemplate").html());
    }
  };

  $(".projectForm")
    .on("click", "#addMemberButton", function(){
      var newTeamMemberHtml = $("#newTeamMemberTemplate").html();
      // use underscore if any placeholders
      $(newTeamMemberHtml).insertBefore("#addMemberControl");
      // hack for now
      TypeAheader.feed($("input.autocomplete").not(".tt-query"),
                        typeAheadConfig,
                        typeAheadSelectCallback);
    })
    .on("click", ".removeTeamMember", function(){
      $(this).parent().remove();
    })
    .on("click", "#addOneMoreFile", function(){
      var newAttachmentHtml = $("#newAttachmentTemplate").html();
      // use underscore if any placeholders
      $(newAttachmentHtml).insertBefore("#addOneMoreButtonContainer");
      attachmentsCount += 1;
      setAddMoreFilesButtonState(attachmentsCount);
    })
    .on("click", ".removeAttachment", function(){
      $(this).parent().remove();
      attachmentsCount -= 1;
      setAddMoreFilesButtonState(attachmentsCount);
    });

  $(".projectForm").validate({
    // TODO: Fix the bug here
    errorElement : "div",
    errorPlacement: function(error, element){
      var elementClasses = element.attr("class").split(" ");

      if(_.contains(elementClasses , "projectTeam")){
        console.log(error, element);
        $("#membersError")
          .html("")
          .append(error);
      }
      else{
        error.addClass("alert");
        error.insertAfter(element);
      }
    },
    rules: {
      name: {
        required: true,
        minlength: 2
      },
      mol:{
        required: true,
        minlength: 5
      },
      description: textAreaValidationReq,

      targets:textAreaValidationReq,
      tasks: textAreaValidationReq,
      target_group: textAreaValidationReq,
      schedule: textAreaValidationReq,
      resources: textAreaValidationReq,
      finance_description: textAreaValidationReq
    }
  });
  
  // createNewTypeAhead($("input.autocomplete"));
  TypeAheader.feed($("input.autocomplete"), typeAheadConfig , typeAheadSelectCallback);


  // waiting for the autocomplete API from the backend
  $(".autocomplete").rules("add", {
    required: true,
    minlength: 2
  });
});