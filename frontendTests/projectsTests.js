// projectsTests.js
casper.test.begin('System running on localhost:8000', 1, function suite(test) {

	casper.start('http://localhost:8000/projects/add/', function() {
		this.fill('form.loginForm', {
			'username':    'asdasd',
			'password':    'asdasd',
		}, true);
	});


	casper.then(function() {
		test.assert(this.visible('.alert-danger'), 'Wrong Password! Notification is OK'); 
	});

	casper.then(function() {
		this.fill('form.loginForm', {
	        'username':    'admin',
	        'password':    'admin',
	    }, true);
	});

	casper.then(function() {
		this.test.assertEquals(this.getCurrentUrl(), 'http://localhost:8000/projects/add/', 'Logged in with correct password');
	});

	casper.run(function() {
	    this.echo('Login System Works!').exit();
	});

});