casper.test.begin('Testing Login Form', 2, function suite(test) {

	casper.start(host + '/members/login/', function() {
		this.fill('form.loginForm', {
			'username':    'adshads',
			'password':    'dsasskdkdkdk',
		}, true);
	});


	casper.then(function() {
		test.assert(this.visible('.alert-danger'), 'Test login incorrect password'); 
	});

	casper.then(function() {
		this.fill('form.loginForm', {
	        'username':    adminUsername,
	        'password':    adminPassword,
	    }, true);
	});

	casper.then(function() {
		this.test.assertEquals(this.getCurrentUrl(), host + '/', 'Test login correct password');
	});

	casper.run(function() {
	    test.done();
	});

});