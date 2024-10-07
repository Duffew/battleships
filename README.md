# Battleships

## Features
### Current Features
### Future Features

## Data Model

## Testing
### Manual Testing
The project's features were manually tested for functionality. The screenshots below show a table of the features tested, the function to which they belong and the result.

![table 1](screenshots/test_table_1.png)
![table 2](screenshots/test_table_2.png)
![table 3](screenshots/test_table_3.png)
![table 4](screenshots/test_table_4.png)
![table 5](screenshots/test_table_5.png)
![table 6](screenshots/test_table_6.png)

### Validatior Testing
The project's code was passed through the Code Institute Python Linter validator. The results showed no errors found.

![Python linter test results](screenshots/linter.png)

### Bugs
#### Resolved Bugs
During development I identified a bug where the programme did not seem to generating the correct number of ships based upon the board size - 20% of the board cells should be ships. For a 5 by 5 board, there should be 5 ships, but as the screenshot below shows, sometimes the programme would generate fewer ships than that.

![bug 1 - the problem](screenshots/battle_bugs_1_problem.png)

The problem in the code was an error in the 'for' loop for iterating ship placement. I had made reference to two [x] coordiantes rather than [x][y].

![bug 1 - the code problem](screenshots/battle_bugs_1_code_problem.png)

Adjusting the variable fixed the bug.

![bug 1 - fixed](screenshots/battle_bugs_1_fixed.png)

#### Unresolved Bugs
There are no unresolved bugs.

## Deployment
### GitHub for Version Control
The project was developed using the GitPod Integrated Development Environment (IDE) and pushed to the battleships repo on GitHub. The following git commands were used to communicate between the IDE and the repo:

+ git add . - used to add updates to the staging area ready for committal to the queue
+ git commit -m "comment" - used to commit updates to the repo queue
+ git push - used to send updates in the queue to the repo on GitHub

### Heroku for Deployment
The project was deployed Heroku using the follwoing steps:
+ 'Create new app' from within the Heroku dashboard
    - choose a unique app name
    - select region - Europe
    - select 'create app'
+ Set up the app
    - define Config Vars
    - add buildpacks
        + python
        + nodejs
+ Deploy
    - Select Gitub
    - Search for GitHub repo and connect
    - Choose deployment method - manual
    - Select 'view' to see the link to the deployed version

## Technologies
### Languages
+ Python
### Libraries & Frameworks
+ Import random for generating the game boards and computer turns
### Tools
+ GitHub for code storage and version control
+ GitPod for IDE
+ VSCode for offline coding, experimenting, and practice
+ Heroku for game hosting
+ Node.js for User Interface within Heroku

## Credits

