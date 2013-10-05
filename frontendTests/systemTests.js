// SystemTests.js
casper.test.begin('System running on localhost:8000', 1, function suite(test) {
    casper.start("http://localhost:8000/", function() {
        test.assertHttpStatus(200);
    });

    casper.run(function() {
        test.done();
    });
});