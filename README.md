# Battleships

## Game Rules

## Features
### Current Features
+ User defined board size
    - The user can choose a board size from between 4 and 8 square
    - Ships are randomly placed on the both the player's and computer's board
    - The number of ships placed is 20% of the total cells on the board
    - The computer's ships are hiden from the player unless sunk
    - The boards feature alphabeticised columns and numeric rows

    ![welcome and game setup](screenshots/feat_welcome.png)

+ Games are played against the computer, and the player always takes the first turn
+ Users are able to input coordinates to make a choice
+ Players can quit the game easily at the beginning of their turn
+ Scores are maintained throughout the game

    ![game play 1](screenshots/feat_gameplay_1.png)
    ![game play 2](screenshots/feat_gameplay_2.png)

+ Turns are tracked and displayed upon game conclusion
+ The player and computer always have the same number of turns to maintain fairness

    ![game play 4](screenshots/feat_gameplay_4.png)

+ Input validation and error checking
    - Duplicate targets prompt player to try again

        ![game play 3](screenshots/feat_gameplay_3.png)

    - Invalid inputs prompt the player to keep trying until a valid target is chosen

        ![invald inputs](screenshots/feat_invalid.png)
    
### Future Features
Possible future features might include:
+ Enable players to input their name for labeling the board
+ Add colour to the game boards for hits and misses
+ Add audio for hits and misses
+ Enable players to place ships themselves
+ Allow for larger ships to be placed

## Data Model
This project employed an Object-Oriented Programming (OOP) approach by making use of a GameBoard class for the player's board and ComputerBoard class for the computer's hidden board. 

The ComputerBoard class inherits the properties of the GameBoard but adds a property to ensure that the player cannot see the computer's ships.

Both classes make use of methods to enable:
+ random ship placement during game setup
+ the boards to be printed to the terminal

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
During development I identified a bug where the programme did not seem to generate the correct number of ships based upon the board size - 20% of the board cells should be ships. For a 5 by 5 board, there should be 5 ships, but as the screenshot below shows, sometimes the programme would generate fewer ships than that.

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

