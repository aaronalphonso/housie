# Housie
All the core logic required to play the classic game 'Housie' (also known as 'Bingo' or 'Tambola'). 
Terminal driven with a simple menu to drive game-play.
 
All the code is well segregated, so should be a breeze if you want to
reuse and build upon any of the components.

## Core Features:
* Generating Housie Tickets to play the game (Ticket format is accurate! Numbers are exactly where they are supposed to be)
* Displaying the Housie board visually in terminal
* Randomly picking numbers on the board, for when you're hosting a game with friends
* Auto-marking the numbers on your tickets, for when you are following a game hosted by someone else


## Installation and Setup

* The only dependency for this project is python3. You can get it [here](https://www.python.org/downloads/).  
* After that, just clone this repository and you can start using it.

## Usage

To run the housie game, we need to make sure we are in the source folder. 

So cd into the project directory i.e. 
`housie`, and then further into `housie` which is the base directory for the source code.
```bash
cd housie/housie
```  
Then run the following command to start the game:

```bash
python game.py
```
This will display a menu in the terminal, allowing you to explore the various features.  

![Main Menu Image](images/main_menu.png)


## Features Explained
This section explains each of the features present in the main menu.

**Host a New Game** 
* This mode displays the housie board on the screen and lets you randomly pick numbers.
* This mode is for when you are playing a game with friends. 
* The board is constantly updated with the selected numbers. 
* Before using this mode, you may want to generate 
and distribute tickets among your friends. 

![New Game Image](images/new_game3.png)

**Generate Tickets**
* As the name suggests, this mode allows you to generate tickets. 
* You specify the names of players and the number of tickets per player, and the program generates and prints 
out the tickets on the screen.
* The generated tickets are also available in `housie/data/generated_tickets.json`.

![Generate Tickets Image](images/generate_tickets.png)

**Follow a Game**
* This mode was built as a convenience mode for when playing games that are hosted by someone else.
* Before starting this mode, you need to enter your tickets into the `housie/data/followed_tickets.json` file. Use the 
`housie/data/followed_tickets.example.json` file as a reference.
* Then start up this mode. You will see the housie board displayed along with your tickets.
* Enter the numbers called out by the host and these numbers will be automatically crossed out in your tickets.
* **Note**: This mode persists game state (i.e. if you shut the program suddenly and start up again, you can continue 
where you left off). If you want to start a new game, just delete the `housie/data/followed_housie.json` file.

![Followed Game Image](images/followed_game_2.png)


## Codebase Structure
This section will describe some of the important files inside the `housie/` source code directory.
* All core logic for representing and manipulating the housie board and housie ticket are present inside 
`models/housie.py` and `models/ticket.py` respectively.
* Ticket-generation logic is present in `generate_ticket.py`
* `display_util.py` contains some custom logic for displaying the board and the tickets side by side during the 
'Follow a Game' mode.
* The `game.py` file contains the core logic that drives game-play and integrates the various modules described above 
to bring about the whole experience of playing the game.  

## Extending and Adding new functionality
The purpose of this package is to provide the core logic required to play the game. 
Keeping this in mind, I have tried to segregate the code as per functionality and reusability. 

Feel free to add upon this base layer.
##

**Author**

  
```

  Aaron Alphonso (https://github.com/aaronalphonso)
  Email: alphonsoaaron1993@gmail.com
  
``` 