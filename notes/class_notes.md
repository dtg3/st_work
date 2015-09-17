### Wednesday, September 16, 2015
#### NOTE: Put word "Testing" in email homework submission

* Quiz:
	* What is the purpose of testing?
		* To get evidence of correct functionality
		* Unless you can bound the universe, you can't prove correctness
		* You can get a lot of evidence, though.
	* What is a challenge to perfect testing?
		* Can't test all possible inputs

* Testing = aquisition of evidence
* Boundry conditions are good for tests
	* Where things tend to break
* Test examples of every kind of thing
	* Testing from each equivalent class

* Advantage of Unit Testing
	* Correct functionality
	* Early detection of issues
	* Comes before all other things (except for req. and analysis)
	* Poor reqs.
		* Did you write the code wrong or is the req wrong?
	* Manual tests don't accumulate
		* Unit tests get re-run over and over
	* Safety when changes are made
* Late stage Advantages
	* Unit tests help in re-engineering
	* Tests help with migration to new platform
	* Porting tests to new environment is step #1
	* "Code Archeology" becomes easier
		* Digging aronud in old code.

* Extending the Calculator
	* Play cool music while python-ing

* Internal vs External
	* Internal
		* Functions and classes
	* External
		* Special library to manipulate library from outside
		* Automated GUI, Webdrivers, etc.

* Simulate GUI
	* Find GUI events and call them manually

* Automate the GUI via OS
	* Use programmed access to browser or OS
	* Create mouse, keyboard, events
	* Application won't know it's automated

* Selenium
	* GUI Automation
	* Manipulates webbrowsers
	* Now uses WebDriver
	* Can program WebDriver directly

* WebDriver
	* Accesses web browers
	* Works on most browsers

* Django....unchained