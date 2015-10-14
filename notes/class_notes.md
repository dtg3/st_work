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

* Homework 2
	* Get systems running so CH2 can be done
	* Convince if cone and circle volume area supports
	* Write something with webdriver that does something interesting:
		* Verify that Amazon sells coffee cups

### Wednesday, September 23, 2015

* Functional Story

### Wednesday, September 30, 2015

* Example

### Wednesday, October 7, 2015

* In class coding

### Wednesday, October 14, 2015

* BBST - Black Box Software Testing
	* Cem Kaner 
	* Jim Bach
	* Rebecca Fielder
* Test on external behavior and evidence
* What is suitable? What is quality?
* Software testing is:
	* an empirical, technical, investigation, conducted to provide stakeholders with information about the quality of the product or service under test.
	* brief: Evidence of quality
	* empirical - based on evidence (reasoning about facts + basic facts)
	* technical - technology will be used
	* investigation - active plan to collect facts. specfic activity designed to take specific input
	* stakeholders - people who have a vested interest in the software
	* quality - different stakeholders have different ideas of quality. Value is based on stakeholder.
		* Network, Security, Accounting, Business, etc.
* Quality - Value of usefulness to someone....subjective
* Information is probabilistic...cause to believe
	* How much probability is required?
* Definitions
	* are not absolute
	* are meaningful
	* need to know what is meant here (in the domain of application)
* Black Box
	* Can't see internals
	* Testing external expectations
	* Tested by those that know the domain
	* They verify that the thing is behaving properly
		* NOT THAT INTERALLY IT IS CORRECT
	* aka "Behavioral Testing"
	* Oracle
		* External reference of correctness
* Glass Box
	* Used to be called White Box 
	* Test against internal expectation
	* Does what programmer expects
	* Easier to do
	* Less valuable to customer
	* aka "Structural Testing"
* Levels of testing
	* Unit
		* Testing of parts
	* Integration
		* Testing of parts together
			* 1-1
			* Star
				* Test one thing....and everything connected to it
			* All parts
		* Do parts work together
	* System
		* Testing of the business system in its environment
		* Are the needs of the stakeholders met
	* Orthogonal to BB/GB testing
	* For instance, we can unit test sorted([])