"""Constants file for holding constant values declared throughout the app"""

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
ColumnRange = NamedTuple('ColumnRange', [('start', Number), ('end', Number)])

# User Menu Selection Choice Type
Choice = str

# List of Valid ranges for each column of the ticket
COLUMN_RANGES = \
		[ColumnRange(1, 9)] + [ColumnRange(start, start + 9) for start in range(10, 71, 10)] + [ColumnRange(80, 90)]

# Main menu instructional message
INSTRUCTIONS = """Welcome to Housie!

Press 'N' to Host a New Game 
	Displays board, randomly picks numbers

Press 'T' to Generate Tickets 
	Generate out tickets for Players to use to play the game

Press 'F' to Follow a Game 
	This mode allows you to follow a game being hosted by someone else, i.e. someone else is calling out the
	numbers as you sit and mark your tickets. This mode automates the marking of your tickets and shows a nice
	visual display of the board and your tickets.
	
	Before using this mode, enter your ticket(s) into the 'data/followed_tickets.json' file. Then start this mode
	and keep entering the numbers being called out. The status of your ticket(s) are automatically updated on
	screen.

Press 'Q' to Quit
"""


FOLLOW_GAME_TICKETS_NOT_FOUND_MSG = """
No tickets found in file 'data/followed_tickets.json'!

If you want to follow a game, make sure to first add your tickets into this file. 
If the file doesn't exist, create it. Use the 'data/followed_tickets.example.json' file as a reference. 
"""
