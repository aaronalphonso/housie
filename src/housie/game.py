"""Main Logic to drive the Game-Play

Classic Housie Board game

Also known as Bingo
https://en.wikipedia.org/wiki/Bingo_(British_version)
"""

__author__ = 'Aaron Alphonso'
__email__ = 'alphonsoaaron1993@gmail.com'

from typing import Dict, List, Optional

from housie.utils import load_json, save_json, clear_screen, dynamic_doc
from housie.constants import INSTRUCTIONS, Number, FOLLOW_GAME_TICKETS_NOT_FOUND_MSG, FOLLOWED_TICKETS_FILE, \
    FOLLOWED_BOARD_FILE, GENERATED_TICKETS_FILE, TicketRepresentation
from housie.models import Board, Ticket, load_tickets
from housie.display_util import display_followed_game
from housie.generate_ticket import generate_ticket


def print_options() -> str:
    """Prints the options to allow the user to drive the program flow"""
    option = 'default'
    while option not in ['N', 'T', 'F', 'Q']:
        clear_screen()
        print(INSTRUCTIONS)
        if option != 'default':
            print("Sorry that is not a valid input. Please try again")
        option = input("\nSelect an option to get started: ").upper()
    return option


def host_new_game() -> None:
    """Host a Housie Game.
    Starts with a blank board. Randomly picks numbers and updates the board when you ask it to
    """
    options = "Press 'Enter' to pick the next number\nPress 'Q' followed by 'Enter' to quit\n"
    board = Board()
    clear_screen()
    print(board.display_board())
    user_choice = ''
    while user_choice not in ['Q', 'q']:
        user_choice = input(options)
        board.pick_next()
        clear_screen()
        print(board.display_board())


@dynamic_doc
def follow_game() -> None:
    """Allows you to play along/follow a game being hosted by someone else.

    Reads your tickets from '{FOLLOWED_TICKETS_FILE}' and displays them.
    Refer to the '{FOLLOWED_TICKETS_EXAMPLE_FILE}' file as a reference file.

    Reads the board from {FOLLOWED_BOARD_FILE} on startup. Displays the board.
    Allows you to enter the numbers being called out by the host, and updates your tickets and the board.
    The state of the board is persisted even if you exit the program.
    To start a new game, delete the {FOLLOWED_BOARD_FILE} file.

    For this mode, certain files are read from/saved to a folder named '{DATA_DIR}' which
    should be in the current directory from where you are running the game.

    NOTE: This mode doesn't let you generate numbers randomly on the board. This is because the whole purpose of this
    mode is to allow to follow a game being hosted by someone else.

    If you want to host a game and play with friends, use the generate tickets mode to distribute tickets to your
    friends, and then use the host a game mode to play.
    """
    already_selected_numbers = load_json(FOLLOWED_BOARD_FILE)
    board = Board(already_selected_numbers)
    ticket_data: Optional[Dict[str, List[Ticket]]] = load_tickets(FOLLOWED_TICKETS_FILE)
    if not ticket_data:
        print(FOLLOW_GAME_TICKETS_NOT_FOUND_MSG)
        return None
    mark_tickets_full_board(board, ticket_data)
    while True:
        clear_screen()
        display_followed_game(board, ticket_data)
        user_choice = input("Press 'Q' to quit. Enter next number: ")
        if user_choice == 'Q' or user_choice == 'q':
            break
        elif user_choice.isnumeric():
            number = int(user_choice)
            board.pick_manual(number)
            save_json(board.selected, FOLLOWED_BOARD_FILE)
            mark_tickets(number, ticket_data)


def mark_tickets_full_board(board: Board, ticket_data: Dict[str, List[Ticket]]) -> None:
    """Updates the tickets with all numbers from the housie board"""
    for name, tickets in ticket_data.items():
        for ticket in tickets:
            ticket.mark_numbers(board.selected)


def mark_tickets(number: Number, ticket_data: Dict[str, List[Ticket]]) -> None:
    """Updates the tickets with all numbers from the housie board"""
    for name, tickets in ticket_data.items():
        for ticket in tickets:
            ticket.mark_number(number)


@dynamic_doc
def generate_tickets() -> None:
    """Allows you to generate housie tickets for use in a game. Enter the names of the players and numbers of tickets
    per player

    Saves the generated tickets to a file '{GENERATED_TICKETS_FILE}'
    """
    clear_screen()
    names = input("Enter the names of users playing the game. Separate each name with a space: ")
    number = input("Enter the number of tickets to be generated per user: ")
    ticket_data: Dict[str, List[TicketRepresentation]] = {}
    names_list = map(str.strip, names.split())
    for name in names_list:
        tickets = [generate_ticket() for _ in range(int(number))]
        print(name)
        for ticket in tickets:
            print(ticket.display_ticket())
        # Convert from ticket object in a list of rows representing the ticket so we can save and load it from json
        ticket_data[name] = [ticket.rows for ticket in tickets]
    save_json(ticket_data, GENERATED_TICKETS_FILE)
    print(f"The generated tickets can also be found in the '{GENERATED_TICKETS_FILE}' file")


@dynamic_doc
def display_main_menu() -> None:
    """The starting menu presented to the user

    Supported Options are as follows :

    'N' - Host a New Game
        Displays the board, randomly picks numbers

    'T' - Generate Tickets
        Generate tickets for Players to use to play the game. Also stores the tickets to the '{GENERATED_TICKETS_FILE}'

    'F' - Follow a Game
        This mode allows you to follow a game being hosted by someone else, i.e. someone else is calling out the
        numbers as you sit and mark your tickets. This mode automates the marking of your tickets and shows a nice
        visual display of the board and your tickets.

        Before using this mode, enter your ticket(s) into the '{FOLLOWED_TICKETS_FILE}' file. Then start this mode
        and keep entering the numbers being called out. The status of your ticket(s) are automatically updated on
        screen.

    'Q' - Quit

    """
    option = print_options()
    if option == 'N':
        host_new_game()
    elif option == 'F':
        follow_game()
    elif option == 'Q':
        print("Thank you for playing! Bye")
    elif option == 'T':
        generate_tickets()
    else:
        print("Sorry this feature is not available yet!")


if __name__ == '__main__':
    display_main_menu()
# demo_board()
