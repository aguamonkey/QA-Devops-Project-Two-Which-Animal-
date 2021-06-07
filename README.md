# Which Animal Am I Project

## *Contents*

* [Intro](#Introduction)
    * [Objective](#Objective)
    * [Proposal](#Proposal)
* [Architecture](#Architecture)
    * [Trello Board](#Trello-Board)
    * [Risk Assessment](#Risk-Assessment)
    * [Testing Setup](#Testing-Setup)
* [Infrastructure](#Infrastructure)
    * [Continuous Integration](#continous-integration)  
    * [Entity Diagram](entity-diagram)
    
* [Development](#Development)
    * [Unit Testing](#Unit-Testing)
    * [Front End Design](#Front-End-Design)
* [Footer](#Footer)


## *Introduction*

### *Objective*

For this project our main goal was to create a service-orientated architecture for our own applications. Overall the application had to be composed of at leat 4 services working together. Before I go into how I planned to design each individual server, let's first look at the minimum set of requirements we hoped to achieve.


Specifically we were required to:  

* Create a Trello board with full expansion on tasks needed to complete the project.
* Provide a risk assessment with any issues or risks faced creating the project.
* Create an application that was fully integrated using the feature-branch model in to a version control system, which then would be built through a CI server and deployed to a cloud based virtual machine.
* Implement webhooks when any changes are made and pushed up to github, meaning Jenkins reacts to any new uploads and deploys the application as a result.
* Follow the service-orientated architecture as previously mentioned.
* Deploy the project using containerisation and an orchestration tool.
* Create an Ansible Playbook that will provision the environment our application needs to run.
* Finally use a reverse proxy to make the application accessible to the user.

### *Proposal*

For my project my aim was to create a website that allowed the user to input their date of birth and then as a result find out what there chinese zodiac was. Along with their animal zodiac a random luck number would be generated and based on the number they would be assigned a fortune for the year ahead.

The best way I can show you what my aim was is by detailing the specific services below:

*Service 1:*

* Home Page:
    * Here you would encounter a date form using html5 where you could select your date of birth from a drop down menu.
    * This services main job, was to communicate to the other three services within the application along with persisting the data from said services in to an SQL database.

*Service 2:*
* Get Animal Name
    * Based on the date of birth inputted by the user this service would take the date and through using conditional statements, determine which animal the user was to be assigned.

*Service 3:*
* Random Number Generator
    * This service would generate a random number from 0-100. This was to be the luck number for the year ahead. It would have a direct effect on the fortune of how the users year was going to go.

*Service 4:*
* Fortune
    * For the final service, based on the animal you were assigned and the luck number generated you would be given a fortune for the year ahead. If your luck number was above 75 it would be a prosperous prediction. Between 45 and 75 would mean you may face some hard times but overall it would be a good year. Finaly below 45 meant the year ahead would be a difficult one to face.

## *Architecture*

### *Trello Board*

[Link to my trello](https://trello.com/b/IUMISsfV/which-animal-am-i)

I decided to use Trello because it is simple in it's design, free to use and is a good visual aid to manage your progress. I implemented MOSCOW prioritisation using a color scheme. I then came up with a few user stories to outline the direction my project would go in and then based on these starting to set up my backlogs. Once the backlogs were done, I assigned tasks to the scrums as and when they were necessary. 

![Image of trello board](https://i.imgur.com/zBOZwLu.png)

### *Risk Assessment*

[Link to my risk assessment](https://docs.google.com/spreadsheets/d/1h6sSbGBpRzu-AWcA5ZBxbTg6rulTKAoo/edit#gid=682879054)

For my initial risk assessment I focused more on the risks I came across from my first project, centered around database risks and leaking of credentials. As I grew to understand the virtual machines and how dependent on them my project was, I began to see that there were other specific risks associated with this project. These have been added at a later point and are highlighted in grey in order to establish this fact.

![Image of risk assessment](https://i.imgur.com/unrJw5X.png)


### *Testing Setup*

The first version of my ERD was as follows:

![Jenkins Pipeline Setup](https://i.imgur.com/DiD8R5G.png)

This application mainly focused on unit testing to ensure each server worked in the correct way. The testing was adding as part of the Jenkinsfile to be sure that at the beginning of any build all of the tests passed.

## *Infrastructure*

### *Continous Integration*

Through learning about continous integration and having now experienced it in practice within a couple of my own project, I see how it would fit in well with any business. It allows for a streamlined development process that leads to deploying a product that has a strong foundation. I use Git as my version control system to push my code to and then used a Jenkinsfile within my code to fetch and build the repositiory as well as run docker compose and configure all the different roles through ansible. Once everything was setup the swarm was then deployed.

Here is an image to walk you through what's going on in my CI pipeline.

![Image of CI Pipeline](https://i.imgur.com/O7fy9ub.png)

### *Entity Diagram*

Designing the structure of this database was much simpler as there were no relationships to account for. However it is still important to highlight how everything was set up.

![Image of ED](https://i.imgur.com/9YDYcy6.png)

### *Interactions*

The diagram below outlines the process theat happens as a user connects to our docker swarm through an NGINX load balancer:

![Image of NGINX](https://i.imgur.com/lVLHpEw.png)

## *Development*

### *Front End Design*

Below is a brief outline of how the front end of the website looks.

Home Page:

First you have the home page where you are able to select your date of birth.

![Image of home page](https://i.imgur.com/F7dOEyO.png)

Select a date:

You do this from the drop down menu that is presented.

![Image of select a date](https://i.imgur.com/fETUPQQ.png)

Your fortune:

Then once you've entered your details, you are transported to the fortune.html page where you will see the animal you are, along with your lucj number and your fortune for this year.

![Image of fortune page](https://i.imgur.com/PkFnBCX.png)


### *Unit Testing*

As mentioned unit testing was used to ensure that the functionality of each of my services ran correctly. I attempted to be as in depth as possible with my testing. I wanted to ensure that all elements of the database were covered. I ran pytest in the terminal of my app and ended up with over 90% in most areas coverage as seen below.

![Image of service 1 tests](https://i.imgur.com/3LEdrzX.png)

For service 1 I had to structure the test to take a specified date and then based on that date I instructed the test to gather a certain set of data. If the data was accurate then the test was a success.

![Image of service 2 tests](https://i.imgur.com/FTulHix.png)

For service 2 I again inputted a date and told the test what I expected to be returned in reference to the animal name associated with the test.

![Image of service 3 tests](https://i.imgur.com/BMY9GMM.png)

FOr service 3 I used a for loop to loop through random numbers between 0 and 101 to determine as to whether the luck number generator was working accordingly.

![Image of service 4 tests](https://i.imgur.com/pphKUGR.png)

Finally for service 4 I inputed the animal name and luck number from within my json dictionary and then based on these two factors I inputted what I expected the fortune to be as a result. All tests passed.





## *Footer*

### *Future Improvements*:

There are a number of improvements I would like to make given the time in the future.

* I would implement selenium testing within my tests so that I could ensure that the site was tested in the most thorough way possible.
* I would look at adding sounds and images to the site to give it a better look and feel.
* I would go more in depth to the actual astrology of each animal and what the unique fortunes of them are. 

### *Author*

Joshua Browne


### *Acknowledgements*
* [Harry Volker](https://github.com/htr-volker)
* [Oliver Nichols](https://github.com/OliverNichols)