# hudl_tech_test

Written in Python 3 on a x64 Windows 10 machine.

Key 3rd party libraries used: pytest, selenium
Run the following to install dependencies:
	pip install requirements.txt

Execute tests by running runner.py
Test results and log can be found in output/
Tests can be run against Chrome, Firefox and IE.  Note that only the chromedriver is supplied with this project.  See drivers/

NOTE:
I implemented a test for the remember me feature, however i couldn't figure out the logic.  It seemed to exhibit the same behaviour whether it was checked or not.  I have marked the test so it gets skipped
