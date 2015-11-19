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
* Functional testing
	* Given input...does it give proper output?
* Non-Functional testing (Parafunctional)
	* While it's generating the correct output
		* how is it performing?
			* usable
			* stable
			* performance/efficient
			* secure
			* etc
* Acceptance testing
	* Is someone going to pay for it?
		* Have terms of contract been met
	* Is there a contract?
	* Implied contract
		* Development vs Marketing
		* R&D vs Product
		* etc
	* Doesn't have to be a written contract
	* Agreement fulfilment
* Why Test?
	* There are always decisions behind testing
		* Need to make a decision and want to make a good decision
		* Testing helps with the decision to use/continue/kill/etc a system/application
	* Gather evidence of quality
	* There are objectives
	* Hard to know how well
	* Hard to know how much information is needed?
	* Every test is a question
		* Did we break something?
		* Chance is > 0
	* Not about absolute knowledge (Probabalistic)
* Oracles
	* Accepted definition of correctnes
	* Mathematics
	* Experts
	* Laws
	* Oracles are incomplete
	* Oracles are heuristic
	* Tests can't be any better than oracles
* Evidence
	* Evidence about quality
	* What are we measuring? What's a good measure and how do we measure it?
* Contexts
	* Prototyping
	* Mass-marked Development
	* Critical Environments
	* Lawsuits
* Testing Mission
	* Blackbox
	* What are we trying to do?
	* What is the success criteria?
	* How much time and resources do you have to meet success criteria?
* Testing Strategy
	* Given Limits
		* Time
		* Resources
	* What will you do?
	* How to maximize benefits?
		* LikelyHood = L 
		* Cost of it happening = C
		* Time = T
		* LC*T
		* In testing can we reduce either of these?
			* Usually in testing you worry about L
				* Can be worried about T too
			* In monitoring you worry about C and T
		* CBA - cost benefit analysis
* Scenario Testing
	* Complex story
		* How is it used in business?
	* Make sure the story works
		* Each element of the story is verified
	* Normal usage works
	* Viewed as important / realistic
* Domain Testing
	* Consider all possibilities
	* Group in to partitions
	* Select from partitions
	* Select from boundaries
	* Unusual tests are viewed as unlikely
		* Tend to find the unusual
	* Two Bad Outcomes
		* Takes lots of time
		* Viewed as unlikely
			* Why did you bother
	* Needs automation, fast, cost effective
* Techniques
	* James Bach
	* Some or all:
		* Analyze the situation
		* Model the test space
		* Select what to cover
		* Determine test oracles
		* Configure the test system
		* Operate the test system
		* Observe the system
* TDD as a Technique
	* Feature is desired
	* Feature gets operated
	* Feature examples
	* Code assertions
	* Unit tests
	* Run the tests
	* Assertion failures

HW: Find bug on site / Send webdriver code

### Wednesday, October 21, 2015
#### Testing Challenges
* Web Sites
	* Exposed applications
	* Accessible to technology
	* Requirements are known
	* Oracles are available
	* BBST methods
* Testing Challenges
	* FOSS Packages - Does it work for a given purpose?
		* Easy to get 
		* Well Understood
		* Testable by usual methods
		* Glass Box testing, perhaps
		* useful to community
* NYPL
	* Is the new version better than the old version?
	* Are the features the same?
	* What should a card catalogue do?
	* How can we tell that it's doing it?
	* How can old catalogue be used as an oracle?
		* Assume it's correct.
	* 10 requirements
		* figure out how to test them, and test them
	* Verify isbn numbers from external sources (AMAZON)
	* Can use other oracles
* Mission
	* Define Value
		* Stakeholders
		* What are the values and how to requirements define them?
	* Define failures
		* What are failure modes?
	* Come up with a plan (1 page long)
	* Non-member activities
* Getting Started
	* How to start?
		* Specific Book
			* How many copies
			* When available
			* Available
			* Where a book is/do they have it
			* How many by keyword
			* pages a book has
			* format / media
			* language
			* Book requests for characters (non-english)
		* What to test?
			* Against oracle
			* How many books with keyword?
			* Funnel based on paper books
		* What to test?
			* Multiple Keywords
		* How to test?
			* Python / Pyunit
			* Webdriver

* Homework A
	* One Week
		* Assess the NYPL new catalog
		* Initial Report
			* A test plan
			* A test methodology
			* A prototype of a test
	* Two weeks
		* A test report
		* At least 10 specific requirements tested
		* Automated tests
	* This is acceptance testing
	* URL spoofing
	* Functional requirements

* Homework B
	* Same thing
	* Python Package - tinydb
* Suggested: Tinydb
	* Small database package (small demo forthcoming)
* 10,000 customers
* purchases up to 1,000 items per customer
* customers interests
* one document per customer
* imagine 10 requirements
	* delete remove item from customer list
	* add 
	* do at scale
	* at last item for last customer
	* shouldn't be able to remove customers that exist
* Is this a good idea to use this database?
* 10 million data items
* how many apples, when, etc.
* A document of things, of purchases
* Alternative structures
* VIABILITY
* Slow compared to sqlite?
* Fast implementation for TinyDB?
	* another pip install (native C Json implementation)

### Wednesday, October 28, 2015
* Testing helps to assess value
* Separation of concerns
* Separate tests from app code
* Refactor on the third time you find code
* Project:
	* git checkout chapter_05
	* manage.py migrate
	* manage.py test

### Wednesday, November 4, 2015
* Gather Evidence that a piece of software works in production environment
* Can't always run lots of tests in the presence of customers
* Prepare an environment like production (QA or static site testing)
* Staging Sites
	* Imitate production site
	* Burn down staging server and restage (want to reherse the deployment as well)
* Want to run against static site
* "www.foo.com" -> top level domain
* TO DO:
	* Look at the slides
	* Get a server - digital ocean, linode, etc.
	* Get nginx
	* Send LAN id and point server there (OUTSIDE IP ADDRESS)
		* Also kent id

### Wednesday, November 18, 2015
* Reasons for Failure
	* Wrong requirements
	* Defective code
	* Defective tools
* Problem in execution environment (server / desktop / etc)
	* This probably is the most common reason for outage
	* Really expensive
	* Sophisticated software architectures are making it worse

* Reasons environment fails
	* Missing dependencies
		* Libraries
		* Tools
		* Volumes
		* Ports
		* Connections
		* Credentials
	* Lack of Capacity
		* Memory
		* Disk Space
		* CPU Speed
		* Network Bandwidth
		* Parallel Capacity
	* Changes in the environment
		* Additional activity
		* Cpapcity consumption
		* Connectivity Issues
		* Patches
		* Interference - side effects from other work
		* Malware
		* Credentialing issues
		* Power failure

* How does this relate to testing?
	* Testing the environmental requirements
	* Repeating that test on the target environments
	* Periodically verifying the target environment
	* Environmental assessment in case of failure

* Environment as Software
	* Tools hae been made to _create_ environments.
		* Batch Files
		* Recipies
		* Containers
	* These can be adapted to testing work
		* Test the correct execution of the setup program
		* Compare recipes to current state
		* Evaluate container construction _and_ state
			* Combine the reciepies of states with module data
			* Composible recipe sets

* Recipes
	* Create a tool to describe desired state
	* Put an agent on ta machine, tell it what recipe to follow
	* Agent updates machine to match recipe
	* Recipe conformance is testable

* Puppet
	* puppetlabs.com
	* puppetlabs.com/puppet/what-is-puppet

* Catalogs
	* Puppet configures systems in two main stages:
		* Compile a catalog
		* Apply the catalog
	* What is a Catalog?
		* A catalog is a document that describes the desired system state for one specific compter
		* Lists all the of the resource (...)

* [Example manifest]

* Chef - Alternative to Puppet
	* This is where the "recipe" term comes from
	* Scanning for compliance is a large draw here
	* Learn Chef (Ubuntu)

* Ansible
	* Youtube tut
	* Playbooks

* Programatic Colutions
	* Remote control of machines
		* Write function in, say python
		* Part of the function is executed remotely
	* These allow you to program remote machines
		* Functions to set things up - configuration
		* Functions to return values - testing
	* Paramiko - remote control
	* Fabric - convenient configuration
	* Yarn - alternative for Python 3.x

* Paramiko
	* www.paramiko.org
	* Implements SSH for remote login
	* Very low-level
	* [Paramiko Example]

* Fabric
	* Easy remote command run a series of hosts
	* www.fabfile.org
	* only python 2.7 at this time
	* author not porting, but ports are available

* Yarn
	* Github.com/python-yarn/yarn
	* written in Python3
	* uses paramiko
	* very easy to use
	* array of strings

* Homework
	* get a remote computer running
		* Vagrant or cloud computer
	* execute some yarn commands against it
	* Use python unittest framework to test some setup parameters
	* Is <?> installed?
	* Is <?> directory created?
	* Does this dorectroy have the right permissions?
	*  ...etc
* As always, send me something showing that you did this