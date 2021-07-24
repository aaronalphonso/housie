"""Constants file for holding constant values declared throughout the app"""

__author__ = 'Aaron Alphonso'
__email__ = 'alphonsoaaron1993@gmail.com'

from typing import List, NamedTuple

# Type Aliases
Number = int

# Board related Types
# List of all valid numbers for Housie
NUMBER_POOL: List[Number] = list(range(1, 91))
RemainingPool = List[Number]
SelectedPool = List[Number]

# Ticket Related Types
Row = List[Number]
TicketRepresentation = List[Row]
ColumnRange = NamedTuple('ColumnRange', [('start', Number), ('end', Number)])

# User Menu Selection Choice Type
Choice = str

# List of Valid ranges for each column of the ticket
COLUMN_RANGES: List[ColumnRange] = \
    [ColumnRange(1, 9)] + [ColumnRange(start, start + 9) for start in range(10, 71, 10)] + [ColumnRange(80, 90)]

# Constants related to data files
DATA_DIR = 'data'
FOLLOWED_TICKETS_FILE = DATA_DIR + '/followed_tickets.json'
FOLLOWED_BOARD_FILE = DATA_DIR + '/followed_board.json'
GENERATED_TICKETS_FILE = DATA_DIR + '/generated_tickets.json'
FOLLOWED_TICKETS_EXAMPLE_FILE = \
    'https://raw.githubusercontent.com/aaronalphonso/housie/master/src/data/followed_tickets.example.json'

# Main menu instructional message
INSTRUCTIONS = f"""Welcome to Housie!

Press 'N' to Host a New Game 
    Displays board, randomly picks numbers

Press 'T' to Generate Tickets 
    Generate tickets for Players to use to play the game

Press 'F' to Follow a Game 
    This mode allows you to follow a game being hosted by someone else, i.e. someone else is calling out the
    numbers as you sit and mark your tickets. This mode automates the marking of your tickets and shows a nice
    visual display of the board and your tickets. You can also quit and continue the game from where you left off 
    later. (Game state is persisted)

    Before using this mode, enter your ticket(s) into '{FOLLOWED_TICKETS_FILE}' file in the current directory. 
    Then start this mode and keep entering the numbers being called out. The status of your ticket(s) are 
    automatically updated on screen. 

    (This mode saves files into the '{DATA_DIR}' folder in order to store the 
    state of the housie board. If you want to start a new game, delete the file named '{FOLLOWED_BOARD_FILE}')

Press 'Q' to Quit
"""

FOLLOW_GAME_TICKETS_NOT_FOUND_MSG = f"""
No tickets found in file '{FOLLOWED_TICKETS_FILE}'!

If you want to follow a game, make sure to first add your tickets into this file. 
If the file doesn't exist, create it. Make sure to create the file inside a folder named '{DATA_DIR}' 
in the current directory in which you are running the game. You can use the file found at 
'{FOLLOWED_TICKETS_EXAMPLE_FILE}' as a reference file.
"""
