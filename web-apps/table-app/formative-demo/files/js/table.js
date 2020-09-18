// -----------------------------------------------------------
// --- Fill-in-the-blanks table app for DLH webserver labs ---
// -----------------------------------------------------------
//
// This table-code is designed to require minimal editing in order to get a functioning table app working
// All you need to do is fill in the tableInfo object as detailed in the comments

// ------------------------------------------------------------------------------
// --- Edit this: an object with all the details needed for the table to work ---
// ------------------------------------------------------------------------------

// Please complete the tableInfo object

const tableInfo = {
  // The id of the submit button. *Required for operation of app*
  submitId: "submit",
  //
  // The schema name for the grading submission. If not submitting to Coursera for grading, leave as ""
  schemaName: "he-05-04-formative",
  //
  // Elements which are hidden, which should be showed after submit. For no elements leave as []
  showElements: ["a1", "a2"],
  //
  // The id of the feedback text location. If you don't want to give instant feedback, leave this as ""
  feedbackId: "feedback",
  //
  // The id of the submission status text location
  submitStatus: "submitStatus",
  //
  // The id of a reset button. For no reset button, leave as ""
  resetId: "reset",
  //
  // Correct and incorrect colours. Choose what colour the table elements become upon submit by picking a table class
  // for a correct or incorrect answer. See https://getbootstrap.com/docs/4.0/content/tables/#contextual-classes
  // Eg "table-success" for green, "table-warning" for red, "table-info" for light blue
  // For default green and red you can leave these as empty strings ""
  correctCol: "table-info",
  incorrectCol: "table-secondary",
  // Information about the learner input. Include the id of all learner inputs, and add their details inside {}
  // Include submit: true for any element which should be submitted to Coursera for grading (requires schemaName to be set)
  // For no submit, set submit: false.
  // If you don't want instant feedback for any element, leave 'answer' as ""
  // For multiple possible correct answers, include an array of strings of answers, ["answer1", "answer2", "answer3"]
  // The 'colour' and 'mark' items are optional - set these to "" if you don't wish to colour or mark elements
  // Set colour to the id of the part of the table you want to be coloured based on the correctness of the answer
  // Set mark to the id of the appended tick/ cross box
  inputInfo: {
    "ex1bx1": {
      submit: true,
      answer: "20",
      colour: "ex1row2",
      mark: "ex1mk1"
    },
    "ex1bx2": {
      submit: true,
      answer: "25",
      colour: "ex1row3",
      mark: "ex1mk2"
    },
    "ex1bx3": {
      submit: true,
      answer: "40",
      colour: "ex1row4",
      mark: "ex1mk3"
    },
    "ex2bx1": {
      submit: true,
      answer: "20",
      colour: "ex2row2",
      mark: "ex2mk1",
    },
    "ex2bx2": {
      submit: true,
      answer: "dom",
      colour: "ex2row3",
      mark: "ex2mk2"
    },
    "ex2bx3": {
      submit: true,
      answer: "25",
      colour: "ex2row4",
      mark: "ex2mk3"
    },
    "ex2bx4": {
      submit: true,
      answer: "40",
      colour: "ex2row5",
      mark: "ex2mk4"
    }
  }
};

// --------------------------------------
// --- Don't make any changes to this ---
// --------------------------------------

$(document).ready(function() {
   
  // When the submit button is clicked
  $("#" + tableInfo.submitId).click(function() {

    // ---------------------------------------------------
    // --- Instant feedback & Change appearance of doc ---
    // ---------------------------------------------------

    // Variables to store correctness of answers
    let numCorrect = 0, numQuestions = 0, instantMarks = {}, learnerSubmission = {};

    // Sets correctCol and incorrectCol to green and red if they are empty strings
    if (tableInfo.correctCol === "") {
      tableInfo.correctCol = "table-success";
    }
    if (tableInfo.incorrectCol === "") {
      tableInfo.incorrectCol = "table-danger";
    }

    // Runs through the keys of the inputInfo object
    for(const x of Object.keys(tableInfo.inputInfo)) {

      // Store learner's submitted answers
      if("submit" in tableInfo.inputInfo[x] && tableInfo.inputInfo[x].submit === true) {
        learnerSubmission[x] = $("#" + x).val();
      }

      // If an answer is given in inputInfo and is not an empty string ""
      if("answer" in tableInfo.inputInfo[x] && tableInfo.inputInfo[x].answer !== "") {

        // Count the number of questions with answers
        numQuestions++;

        // If the learner's submitted element $("#" + x).val() is one of the possible answers
        if((typeof tableInfo.inputInfo[x].answer === "object" && tableInfo.inputInfo[x].answer.includes($("#" + x).val().trim().toLowerCase())) ||
        tableInfo.inputInfo[x].answer === ($("#" + x).val().trim().toLowerCase())) {
          numCorrect++;
          instantMarks[x] = true;
        } else {
          instantMarks[x] = false;
        }
            
        // If a colour tag is given, colour appropriately
        if("colour" in tableInfo.inputInfo[x] && tableInfo.inputInfo[x].colour !== "") {
          colourFunc(tableInfo.inputInfo[x].colour, instantMarks[x], tableInfo.correctCol, tableInfo.incorrectCol);
        }

        // If a mark tag is given, mark appropriately
        if("mark" in tableInfo.inputInfo[x] && tableInfo.inputInfo[x].mark !== "") {
          markFunc(tableInfo.inputInfo[x].mark, instantMarks[x]);
        }
      }

      // Make submitted elements readonly
      $("#" + x).prop("readonly", true);
    }

    // Show elements that were previously hidden
    if("showElements" in tableInfo && tableInfo.showElements !== []) {
      for(const x of tableInfo.showElements) {
        $("#" + x).removeClass("d-none");
      }
    }

    // Add a string of feedback to a feedback element
    if("feedbackId" in tableInfo && tableInfo.feedbackId !== "") {
      $("#" + tableInfo.feedbackId).html(numCorrect + " out of " + numQuestions + " correct");
    }

    // Disable submit button
    if("resetId" in tableInfo && tableInfo.resetId !== "") {
      // If there is a reset button, hide the submit button and show the reset button
      $("#" + tableInfo.submitId).addClass("d-none");
      $("#" + tableInfo.resetId).removeClass("d-none");
    } else {
      // If there is no reset button, just disable the submit button
      $("#" + tableInfo.submitId).prop("disabled", true);
    }

    // Scroll to top of page
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera

    // -----------------------------------------------
    // --- Submit learner's submission for marking ---
    // -----------------------------------------------

    // If there is a schemaName and it isn't an empty string
    if("schemaName" in tableInfo && tableInfo.schemaName !== "") {

      // Submit data to server.js to create learner's json file
      $.post("files/learnerSubmission.json", JSON.stringify(learnerSubmission, undefined, 4), function() {
        console.log("Post success");
      })        
      // Handle success or failure of learner file being created
      .done(function() {
        console.log("Learner file successfully created.");
      })
      .fail(function() {
        $("#" + tableInfo.submitStatus).html("Learner file could not be created. ");
      });

      // Get information needed to submit doc to Coursera
      let submissionInfo = getSubmissionInfo(tableInfo.schemaName);

      // Submit data to Coursera
      $.post("https://hub.coursera-apps.org/api/workspaceSubmissions.v1", submissionInfo, function() {
        console.log("Coursera post success");
      })
      // Handle success or failure of Coursera api interaction
      .done(function(data) {
        let submitStatus = "Thank you for your submission. Your answers were submitted successfully.";
        $("#" + tableInfo.submitStatus).html(submitStatus);
      })
      .fail(function() {
        let submitStatus = $("#" + tableInfo.submitStatus).html() + "Submission failed. Please contact the course instructors to report this error.";
        $("#" + tableInfo.submitStatus).html(submitStatus);
      });
    }
  });

  // If a reset button is provided
  if("resetId" in tableInfo && tableInfo.resetId !== "") {

    // When the reset button is pressed...
    $("#" + tableInfo.resetId).click(function() {

      for(const x of Object.keys(tableInfo.inputInfo)) {
                
        // If a colour tag is given, remove colour
        if("colour" in tableInfo.inputInfo[x] && tableInfo.inputInfo[x].colour !== "") {
          resetColour(tableInfo.inputInfo[x].colour, tableInfo.correctCol, tableInfo.incorrectCol);
        }
    
        // If a mark tag is given, remove mark
        if("mark" in tableInfo.inputInfo[x] && tableInfo.inputInfo[x].mark !== "") {
          resetMark(tableInfo.inputInfo[x].mark);
        }
    
        // Remove readonly from submit elements
        $("#" + x).prop("readonly", false);
      }

      // Hide elements again
      if("showElements" in tableInfo && tableInfo.showElements !== []) {
        for(const x of tableInfo.showElements) {
          $("#" + x).addClass("d-none");
        }
      }

      // Remove feedback string
      if("feedbackId" in tableInfo && tableInfo.feedbackId !== "") {
        $("#" + tableInfo.feedbackId).html("");
      }

      // Enable submit button and hide reset button
      $("#" + tableInfo.submitId).removeClass("d-none");
      $("#" + tableInfo.resetId).addClass("d-none");

      // Scroll to top of page
      document.body.scrollTop = 0; // For Safari
      document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera

      if("schemaName" in tableInfo && tableInfo.schemaName !== "") {
        $("#" + tableInfo.submitStatus).html("");
      }
    });
  }
});

// ------------------------
// --- Useful functions ---
// ------------------------

// This function creates a JSON in the correct format to interact with Coursera's API
function getSubmissionInfo(schemaName) {
  // Get coursera submit cookie
  let submissionToken = document.cookie.replace("COURSERA_SUBMISSION_TOKEN=","");
  // Create submission JSON code for API    
  let submissionInfo = JSON.stringify({
    "token": submissionToken,
    "schemaName": schemaName       
  });
  return submissionInfo;
}

// Colour elements of table based on correctness of answer
function colourFunc(identity, correct, correctCol, incorrectCol) {
  // Colours green if correct = true and red if correct = false
  correct ? $("#" + identity).addClass(correctCol) : $("#" + identity).addClass(incorrectCol);
}

// Remove colouring of table elements
function resetColour(identity, correctCol, incorrectCol) {
  $("#" + identity).removeClass(correctCol);
  $("#" + identity).removeClass(incorrectCol);
}

// Mark answer by making the add-on visible and adding a tick or cross emoji
function markFunc(identity, correct) {
  $("#" + identity).removeClass("d-none");
  // Adds tick if correct = true and cross if correct = false
  correct ? $("#" + identity).html("&#9989;") : $("#" + identity).html("&#10060;");
}

// Hide mark again
function resetMark(identity) {
  $("#" + identity).addClass("d-none");
  // Remove cross or tick
  $("#" + identity).html("");
}
