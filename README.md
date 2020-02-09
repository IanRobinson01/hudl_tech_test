# hudl_tech_test

Written in Python 3 on a x64 Windows 10 machine.

Key 3rd party libraries used: pytest, selenium

Recommend setting up a virtualenv for the project and activating it

Run the following to install dependencies:

	pip3 install -r requirements.txt


Execute tests by running runner.py

Test results and log can be found in output/

Tests can be run against Chrome, Firefox and IE.  Note that only the chromedriver is supplied with this project.  See drivers/


NOTE:
The test for the remember me function fails.
I made an assumption that, if remember me is checked when the user logs in, if they close the browser, open a new browser and navigate to the login page, then it would display the home page.
However this doesn't seem to be the case.  It seemed to exhibit the same behaviour whether it was checked or not.
