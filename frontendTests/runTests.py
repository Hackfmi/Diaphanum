import os

os.system("casperjs --includes=config.js test systemTests.js")

os.system("casperjs --includes=config.js test loginTests.js")

os.system("casperjs --includes=config.js test projectsTests.js")