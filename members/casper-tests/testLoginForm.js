casper.test.comment('Login test');
var helper = require('./../../djangocasper.js');
helper.scenario('/members/login/',
    function() {
       this.test.assertExists('input[name="username"]', 'Username field exists'); 
       this.test.assertExists('input[name="password"]', 'Password field exists'); 
       this.test.assertExists('button[type="submit"]', 'Login Button exists');
    }
);
helper.run();
