$(document).ready(function(){
  jQuery.extend(jQuery.validator.messages, {
    required : "Това поле е задължително",
    minlength : jQuery.validator.format("Моля въведете поне {0} символа")
  });

  var
    attachmentsCount = 0,
    maxAttachments = 10,
    setAddMoreFilesButtonState;

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

  var textAreaValidationReq = {
    required: true,
    minlength: 140
  };

  $(".projectForm").validate({
    // TODO: Fix the bug here
    errorPlacement: function(error, element){
      var elementClasses = element.attr("class").split(" ");

      if(_.contains(elementClasses , "projectTeam")){
        console.log(error, element);
        $("#membersError")
          .html("")
          .append(error);
      }
      else{
        error.insertAfter(element);
      }
    },
    rules: {
      projectName: {
        required: true,
        minlength: 2
      },
      projectTeam: {
        required: true,
        minlength: 2
      },
      mol:{
        required: true,
        minlength: 5
      },
      projectDescription: textAreaValidationReq,

      projectMission:textAreaValidationReq,
      projectTasks: textAreaValidationReq,
      projectTargetAudience: textAreaValidationReq,
      projectSchedule: textAreaValidationReq,
      projectResources: textAreaValidationReq,
      projectFinance: textAreaValidationReq
    }
  });

  $(".projectTeam").rules("add", {
    required: true,
    minlength: 2
  });
});