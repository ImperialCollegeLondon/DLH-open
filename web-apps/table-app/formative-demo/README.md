# Fill-in-the-blanks table app

These files provide a way to create a fill-in-the-blanks table web application for use in Coursera labs. They are designed so that someone with a basic understanding of `HTML` and a little `CSS` can customise their own version of the application. No prior knowledge of `JavaScript` is required.

This `README` includes details of the files in this repo, instructions for how to customise the app, and instructions for uploading the app to Coursera.

This app is designed to run using `web-app-image` both locally and on Coursera. The web app image can be found in the [DLH github repository](https://github.com/ImperialCollegeLondon/DLH/tree/master/custom-images/web-app-image). In addition, any web app which submits learner answers to Coursera must be used in conjunction with an autograder - you can find instructions and demo graders in the `custom-graders` directory in the [DLH github repository](https://github.com/ImperialCollegeLondon/DLH/tree/master/custom-graders). We recommend that you [get in touch](mailto:dlh.tech@imperial.ac.uk) with the DLH Tech team at dlh.tech@imperial.ac.uk for assistance on this step.

There are multiple folders in this repo. Each is a complete set of files which can be used to create a web app when combined with `web-app-image`.

- `formative-demo` is a shortened version of the table app used in HE.05.04, and is an example of a formative table, with instant feedback, a reset button, and submission to Coursera. It also features blue/grey colouring instead of the default green/red colouring.

- `summative-demo` is a shortened version of the table app used in HE.05.04, as an example of a summative table. There is no instant feedback, and there is no option to reset the app after pressing submit. The learner's answers are submitted to Coursera, and any feedback the learner receives must be given by the grader.

- `he-05-04` is a version of the table app used in HE.05.04. in the GMPH HE course.

## Files in each demo folder

- `index.html` is the main `HTML` file for the app. Most of the customisation is done here. To run the app locally (without submission and file creation enabled), simply open this file in any web browser. Do not change this file's name.

- `package.json` contains the details needed for this package to work using `Web-app-image`. Do not make any changes to this file.

- `js/table.js` is this JavaScript file which enables all the interactivity of the table. To customise the table you need to edit the `tableInfo` object and nothing else.

- `js/jquery-3.5.1.min.js` is a local version of the [jQuery](https://jquery.com/) JavaScript library used by `table.js`. Such dependencies must be included in the files uploaded to `Web-app-image`, because Coursera Labs do not have internet access.

- `css/bootstrap.css` is a local version of the [bootstrap](https://getbootstrap.com/) `CSS` library used for the style of `index.html`. Such dependencies must be included in the files uploaded to `Web-app-image`, because Coursera Labs do not have internet access.

- `images/favicon-196x196.png` is the Imperial College London favicon logo.

# Running the table app

There are three ways to run the table app, each with their own level of complexity and work required.

### Open index.html in your browser

First, try simply opening one of the demo apps and double clicking `index.html`. This is the simplest way to run the app, but you'll notice that you receive errors when you press the submit button. Running the app this way does not allow for creation of a learner submission file, and the app cannot communicate with Coursera's API to submit.

This is a fine way to run the file when you're starting to customise the table app, or if you do not wish to have the learner submit anything to Coursera for grading. However, in general we recommend some kind of submission to Coursera, even for formative assessments, as they allow us to gather data about the learners' progress.

### Use node to run the server locally

When you've finished the first steps and want to start thinking about the learner submission, you can enable the creation of a learner submission file locally by running the table app with `web-app-image` and `Nodejs`. To do this:

- Download the `web-app-image` directory and its contents, and install [Nodejs](https://nodejs.org/en/).

- Copy everything inside the table app's `files` folder and paste it into the `files` folder inside `Web-app-image`. 

- Navigate to the `web-app-image` directory in your terminal, and run

      node server.js

- Then got to `localhost:3000` in your browser to see the web app!

If you have a schemaId in `table.js` (explained later), you should see a file called `learnerSubmission.json` appear in the files folder. This contains all the information the learner submits, and will be useful when creating a grader for your web app.

There is still an error - this is because it's still not possible to submit to Coursera using Coursera's API when running the web app locally.

### Upload and test in Coursera Labs

The final way to run the web app is simply to upload it to Coursera Labs and link it to a programming item. When you have correctly linked it and uploaded an appropriate grader, you will see a successful learner submission instead of an error.

Details for how to upload and link the web app in Coursera labs are given later in this `README`.

# Customising the table app

To customise the table app we must make changes to `index.html` and then fill in some details to tell `table.js` the id attributes of the elements we are using. If you require any degree of interactivity from an element in `index.html`, then you must give it a completely unique id attribute and provide it to `table.js`.

To modify `index.html` it is helpful to have some knowledge of `HTML`. W3schools provides a good [HTML tutorial](https://www.w3schools.com/html/default.asp), which can also act as a useful reference. It is also helpful to know a bit about `CSS`, in particular bootstrap. There is [good documentation for bootstrap](https://getbootstrap.com/docs/4.5/getting-started/introduction/), and each subsection will contain relevant links to the necessary parts.

Before making any changes to the app, have a plan for how your want your app to function. Look at the demo version of the table app first and read this section to get a sense of what options are available for customisation.

## Checklist

The following is a basic checklist of the steps for modifying `index.html`. For more detail on each of the steps, see the subsections below.

- In `<head>...</head>`, change the text inside the `<title>...<\title>` tags to the title of the assignment or app
- Replace the title of the assignment or app in the "card-header".
- Contruct your table with all of the cells filled in with text. If you want to colour or highlight any part of the table upon submit (see "Add instant feedback" subsection), make sure to give those parts id attributes.
- If you wish to show a completed "answer table" as feedback on submit (see "Add instant feedback" subsection), copy the answers table into a [div](https://www.w3schools.com/tags/tag_div.ASP) with the `class="d-none"` and an id attribute. Include any other text you wish to show upon submit here.
- Replace the text in the question table with input cells. Make sure to give each input cell a unique tag.
- If you want to add a cross or tick on submit (see "Add instant feedback" subsection), include an add-on using the classes `"input-group-append"` and `"d-none"` to each input box, and give it a unique tag.
- Repeat for as many tables and exercises as necessary, adding extra formatting for spaces, exercise titles and descriptions.
- After the tables and optionally after horizontal rules `<hr>`, add a submit button with a unique id (necessary).
- If you want the learner to be able to reset the app, add a reset button with the class `d-none` and with a unique id.
- Add a place for score feedback text, but leave it empty, for example `<p id="feedback"></p>`, with a unique id attribute.
- If pressing the submit button will submit a file containing any of the learner's inputs to Coursera, add a place to give a submit status with a unique id.
- Inside `table.js`, fill out the details of your app in the `tableInfo` object.

## Layout and formatting

This table app uses bootstrap for its layout and formatting. Everything inside the *body* is also inside a [container](https://getbootstrap.com/docs/4.5/layout/overview/#containers), the most basic ingredient of bootstrap and required for layout purposes. Inside the container we have a [card](https://getbootstrap.com/docs/4.5/components/card/), another class in bootstrap. This is written in the file as follows:

    <div class="container">
      <div class="card mt-5">
        ...
      </div>
    </div>

In the above snippet, "mt-5" adds some space above the card. For more info about adding spacing, see the [spacing](https://getbootstrap.com/docs/4.5/utilities/spacing/) entry in the bootstrap docs. We add margins to `HTML` elements throughout `index.html` to space the document appropriately.

In the `card-header` we provide the title of the assignment, to be displayed to the learner, for example:

    <div class="card-header">
      <h2>Title of the assignment</h2>
    </div>

Here `<h2></h2>` makes the title a heading type 2. For info on headings see the [headings](https://www.w3schools.com/html/html_headings.asp) entry in w3schools' HTML tutorial.

In the `card-body` we include everything else that will at some point be visible to the learner. Almost all of your added `HTML` will be inside the following div:

    <div class="card-body">
      ...
    </div>

For info about text see the [text](https://getbootstrap.com/docs/4.5/utilities/text/) entry in the bootstrap docs.

We also make use of bootstrap's grid system to place our feedback next to our submit button. See the [grid](https://getbootstrap.com/docs/4.0/layout/grid/) entry in the bootstrap docs.

## Create a table

We use boostrap for our tables ([table docs here](https://getbootstrap.com/docs/4.5/content/tables/)). Each table is contained within a table tag, with the table class:

    <table class="table table-striped">
      ...
    </table>

We use "table-striped", but you can use any table style you like!

## Add input boxes

Input boxes can be added inside a div with class "input-group". Then add an `<input>` tag with the type, class, unique id and aria labels for accessibility. For example:

    <div class="input-group">
      <input type="text" class="form-control col-xs-2" aria-label="a label" aria-describedby="inputGroup-sizing-sm" id="input1">
    </div>

See the [input group docs](https://getbootstrap.com/docs/4.5/components/input-group/) for more details.

## Add instant feedback

Instant feedback is anything that appears to the learner after the learner hits the submit button with information on how they did. There are multiple options for instant feedback in this table, and we recommend using all of them for formative assessments.

### Colour parts of the table on submit

We include the option to colour parts of the table based on their correctness. To enable this option, simply add unique ids to the row or columns of the tables you wish to change on submit. You will make these elements interactive by including the ids in the correct places in `tableInfo` in `table.js`. By default the colours are green for correct and red for incorrect, but you can also change this using `tableInfo`. See "Complete tableInfo object" for more details.

### Add ticks or crosses on submit

We also have the option to add a component that will show a tick or a cross next to the input depending on correctness. To do this we add the following line *inside* the "input-group" div of our input, after "input":

    <div class="input-group-append">
      <span class="input-group-text d-none" id="mark1"></span>
    </div>

Again, it requires a unique id so that we can identify it as the correct place to add the mark. The "d-none" class hides the box - it will display after the submit button is pressed.

For example, any one input group would look like:

    <div class="input-group">
      <input type="text" class="form-control col-xs-2" aria-label="a label" aria-describedby="inputGroup-sizing-sm" id="box1">
      <div class="input-group-append">
        <span class="input-group-text d-none" id="mark1"></span>
      </div>
    </div>

Again, the id will be added to the correct place in `tableInfo` in `table.js`

### Other elements which show after submit

For any other elements which show after submit, such as a paragraph adding additional information, or a correct completed version of the table, wrap the entire section in a div tag with the class "d-none":

    <div class="d-none" id="displayLater1">
      Your hidden info here
    </div>

Include a unique id, which we will add to the correct part of `tableInfo` to tell `table.js` to show it after submit.

You can have multiple divs which display after submit. Remember to give them their own unique ids!

You can choose to colour the text in these elements by choosing the class appropriately. Details for colouring text in bootstrap can be found [here](https://getbootstrap.com/docs/4.0/utilities/colors/#color). For example, to make the text blue you can add the class `"text-primary"`.

### Show score as feedback 

To show the learner's score as feedback on submit, simply include a place for the feedback to appear and give it a unique id attribute, for example:

    <p id="feedback"></p>

Again we will add this id to the correct part of `tableInfo` to tell `table.js` to show it after submit.

## Submit and reset buttons

For the submit and reset buttons, we have two options for what happens when the learner presses submit:

- The learner presses submit and the submit button is replaced with a reset button

or

- The learner presses submit and the submit button is disabled. The learner must exit or refresh the lab to try again

We suggest that the first option is good for formative assessment, while the second is good for summative assessment that is graded by Coursera.

To set up a submit & reset option, place a submit and reset button one after the other in the `HTML`, and make the reset button invisible using the class "d-none".

For example:

    <input class="btn btn-primary align-middle" type="submit" value="Submit" id="submit">
    <input class="btn btn-primary align-middle d-none" type="reset" value="Try again" id="reset">

When you add the submit and reset ids to `tableInfo`, `table.js` will handle the rest for you.

To set up a one-time submit option, you only need to include the submit button, for example:

    <input class="btn btn-primary align-middle" type="submit" value="Submit" id="submit">

Then, when completing `tableInfo`, leave the reset button id as an empty string "". `table.js` will know to set up a one-time submit option.

## Submit to Coursera for grading

Most of the changes to submit to Coursera for grading are in `tableInfo`, in `table.js`. One thing that is important to include is some information to the learner to let them know that they submitted successfully. Like the feedback from before, simply include a place for the submit status to appear and give it a unique id attribute, for example:

    <p id="submitStatus"></p>

You must add this submit status id to `tableInfo`. Submitting to Coursera for grading also requires the `schemaName` to be given in `tableInfo`.

## Complete tableInfo object

`tableInfo` is an object in `table.js` that contains all the information about the `HTML` needed for `table.js` to make the app function. You need to replace the default values of each of the items inside `tableInfo` with the correct ids for your document. The only changes you should make to `table.js` are the values associated with the items in `tableInfo`.

Here we go through each of the items in `tableInfo` with some description.

- `submitId` is the id attribute of your submit button. It is essential to the functioning of the app. Give your submitId as a string between quotes, for example:

      submitId: "submit",

- `schemaName` is the schema name associated with the lab item on Coursera. It will be used to link the submission to the autograder. Choose a unique schema name of lower case letters, dashes and numbers, for example:

      schemaName: "gmph-he-03-02",

  If you do not wish to submit to Coursera for grading, leave the schema name as an empty string:

      schemaName: "",

- `showElements` contains a list of the id tags of elements which are hidden, which will be displayed after the learner presses the submit button. The format is a list (square brackets) of strings (quotation marks), for example:

      showElements: ["displayLater1", "displayLater2"],

  If you do not wish to show any hidden elements after submit, set this to an empty list:

      showElements: [],

- `feedbackId` is the id attribute of the score feedback text location. The format is a string, for example:

      feedbackId: "feedback",

  For no feedback, leave this as an empty string,

      feedbackId: "",
    
- `submitStatus` is the id attribute of the submission status text location. The format is a string, for example:

      submitStatus: "submitStatus",

  If you have no submission status text, leave this as an empty string;

      submitStatus: "",

- `resetId` is the id attribute of the reset button. The format is a string, for example:

      resetId: "reset",

  If you wish to have no reset button, and instead disable the submit button on submission, leave resetId as an empty string,

      resetId: "",

- `correctCol` and `incorrectCol` are the colours that elements of the table will become if they are correct or incorrect on submit. If you leave these as empty strings, the default colours will be green and red:

      correctCol: "",
      incorrectCol: "",
    
  If you wish to change these, you can find the different colour classes in the [bootstrap docs here](https://getbootstrap.com/docs/4.0/content/tables/#contextual-classes). For example, "table-primary" corresponds to blue and "table-warning" corresponds to yellow, so

      correctCol: "table-primary",
      incorrectCol: "table-warning",
  
  would lead to a table with blue for correct entries and yellow for incorrect entries.

- `inputInfo` is an object inside an object, containing all the details of the input boxes and their associated instant feedback. The elements inside inputInfo are also objects, named by a string containing the id attribute of each input box in the table. Make sure you have one of these objects for each input box you wish to use.

  The format of each of these input objects is as follows:

      "inputIdAttribute": {
        submit: true,
        answer: "20",
        colour: "row2",
        mark: "mark2"
      },

  - Set `submit` to `true` or `false`, where `true` submits the input value to Coursera for grading, and `false` does not.

  - Set `answer` to a string containing the correct answer. If there are multiple possible correct answers, use a list of strings of answers, such as:

        answer: ["20", "twenty"],

    Text answers are not case dependent, so the learner could input "Twenty" or "tWenty" and still get a correct mark in the above example. Spaces are trimmed from the start and end of the input, so an input of " twenty" would also be marked correct, but "twen ty" is incorrect.

    For no instant feedback, leave `answer` as an empty string:

        answer: "",

  - Set `colour` to be the id attribute of the area you wish to be coloured green or red depending on if the answer is correct. For no colouring, leave `colour` as an empty string.

  - Set `mark` to be the id attribute of the add-on which will contain a tick or cross depending on if the answer is correct. For no mark, leave `mark` as an empty string.

  By giving each input box its own object and its own `submit`, `answer`, `colour` and `mark` properties, we allow for the option of only some inputs being submitted for marking to Coursera, only some inputs being instantly marked etc.

When completing `tableInfo`, remember that there should be no comma after the last item of each object.

# Uploading to Coursera

Now that you've created your web app and your web app grader, it's time to upload them to Coursera Labs using the DLH's `Web-app-image`. We recommend that you [get in touch](mailto:dlh.tech@imperial.ac.uk) with the DLH Tech team at dlh.tech@imperial.ac.uk for assistance on this step.

## Uploading the web app to Coursera Labs

If your course already have a web app image in Coursera Labs, you can take the following steps to place the image in Coursera Labs:

- Compress your web app files and `package.json` (everything in the files folder) into a `.zip` (or equivalent) archive. Make sure that the visualisation `html` files and `package.json` are at the root of the archive.

- Navigate to the Lab Manager page for your course, and add a new lab to the web app image. Add the following `mount point`:

      /app/files
  
  and upload the `.zip` or equivalent archive you created of your visualisation and `package.json`.

- Add the lab and open it. If it shows the `successful_compilation_image.html` page again, go to `edit lab` and upload the same `.zip` or equivalent archive you created of your visualisation and `package.json`. Try opening it again.

- It currently seems like it always requires two attempts to upload the files like this - we're not yet sure why.

- Once the correct visualisation is showing, select publish lab.

- If this doesn't work after a few attempts of uploading the same archive, go back and check that you have the correct files and that the web app files and `package.json` are at the root of the archive.

## Linking the lab to an item

If the lab does not submit anything to Coursera, create an ungraded lab item and choose the appropriate lab.

For a web app with submission, create a programming assignment item and choose the submission type to be a lab. Add a grader and fill out the following:

- Part Title: Any unique title is fine here

- Points: The total number of points the assignment is worth

- Schema ID: The `schemaId` you provided in `table.js`

- Mount Point: `app/files`

- File Path: `learnerSubmission.json`

- Suggested File: This depends on your grader, but for graders based on the demo web app grader, `learnerSubmission.json` will do.

- Docker Grader: Upload your web app autograder here. For help, get in touch with the DLH Tech team at [dlh.tech@imperial.ac.uk](mailto:dlh.tech@imperial.ac.uk).

