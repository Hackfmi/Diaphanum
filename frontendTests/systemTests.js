// SystemTests.js
casper.test.begin('System running on' + host, 1, function suite(test) {
    casper.start(host, function() {
        test.assertHttpStatus(200);
    });

    casper.run(function() {
        test.done();
    });
});