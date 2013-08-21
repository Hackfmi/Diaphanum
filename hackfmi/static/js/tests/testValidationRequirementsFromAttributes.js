var utils = window.Diaphanum.utils;

// By putting it in the #qunit-fixture element, 
// we don’t have to worry about DOM changes from one test affecting other tests, 
// because QUnit will automatically reset the markup after each test.

test("Get empty object from no name input", function() {
	var testedInput = "<input type='text' />";
	$(testedInput).appendTo("#qunit-fixture");

	var expectedResult = {};

	deepEqual(utils.validationRequirementsFromAttributes("someRandomName"), expectedResult);
});

test( "Get empty object from no attributes input", function() {
  var testedInput = "<input type='text' name='name' />";
  $(testedInput).appendTo("#qunit-fixture");

  var expectedResult = {};

  deepEqual(utils.validationRequirementsFromAttributes("name"), expectedResult);
});

test("Get required : true when a required attribute is found", function() {
	var testedInput = "<input type='text' name='name' required />";
	$(testedInput).appendTo("#qunit-fixture");

	var expectedResult = {
		required : true
	};

	deepEqual(utils.validationRequirementsFromAttributes("name"), expectedResult);
});

test("Get email : true when type='email' is in the input", function() {
	var testedInput = "<input type='email' name='name' />";
	$(testedInput).appendTo("#qunit-fixture");

	var expectedResult = {
		email : true
	};

	deepEqual(utils.validationRequirementsFromAttributes("name"), expectedResult);
});

test("Get url : true when type='url' is in the input", function() {
	var testedInput = "<input type='url' name='name' />";
	$(testedInput).appendTo("#qunit-fixture");

	var expectedResult = {
		url : true
	};

	deepEqual(utils.validationRequirementsFromAttributes("name"), expectedResult);
});

test("Get date : true when type='date' is in the input", function() {
	var testedInput = "<input type='date' name='name' />";
	$(testedInput).appendTo("#qunit-fixture");

	var expectedResult = {
		date : true
	};

	deepEqual(utils.validationRequirementsFromAttributes("name"), expectedResult);
});

test("Get number : true when type='number' is in the input", function() {
	var testedInput = "<input type='number' name='pesho' />";
	$(testedInput).appendTo("#qunit-fixture");

	var expectedResult = {
		number : true
	};

	deepEqual(utils.validationRequirementsFromAttributes("pesho"), expectedResult);
});

test("Get required, maxlength and minlength into the resulted object ", function() {
	var testedInput = "<input type='text' name='name' required='true' minlength='150' maxlength='300' />";
	$(testedInput).appendTo("#qunit-fixture");

	var expectedResult = {
		required : true,
		minlength : 150,
		maxlength : 300
	};

	deepEqual(utils.validationRequirementsFromAttributes("name"), expectedResult);
});