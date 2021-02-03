"""Complex logic for displaying a followed game conveniently in terminal"""

__author__ = 'Aaron Alphonso'
__email__ = 'alphonsoaaron1993@gmail.com'

from itertools import zip_longest
from typing import Dict, List

from housie.models import Board, Ticket


def display_followed_game(board: Board, ticket_data: Dict[str, List[Ticket]]) -> None:
    """Use this to select how you want the game displayed. The complex display looks better, but may not work in all
    sizes of terminals. Use the simple display as a fall back"""
    # Side-by-Side display with minimalistic ticket design
    # _complex_display_followed_game(housie, ticket_data, 'minimalistic_display', 24)

    # Side-by-Side display with traditional/structural ticket design
    _complex_display_followed_game(board, ticket_data, 'structural_display', 36)


# Simplistic vertical scrolling display
# _simple_display_followed_game(housie, ticket_data)


def _simple_display_followed_game(board: Board, ticket_data: Dict[str, List[Ticket]]) -> None:
    """Simple Display method for use in following a game

    Displays the board followed by the tickets
    """
    print(board.display_board())
    for name, tickets in ticket_data.items():
        print(name)
        for ticket in tickets:
            print(ticket.display_ticket())


class DisplayElement:
    """A wrapper object to group together multiple lines of text as a single element"""

    def __init__(self, content: str) -> None:
        self.row_wise_data = content.split('\n')
        self.content = content


def _complex_display_followed_game(
        board: Board, ticket_data: Dict[str, List[Ticket]], display_method: str, line_len: int) -> None:
    """Side-by-Side Display method for use in following a game.
    Tries to fit the tickets besides the board instead of below.

    Not the best implementation though, as it involves a lot of string manipulations.
    Also doesn't consider size of the terminal for now. But it works!

    Allows to display up to 8 tickets in a nice clean manner. After that, the view could get a little messy
    """
    board_element = DisplayElement(board.display_board())
    ticket_elements = []
    for name, tickets in ticket_data.items():
        ticket_str = ''
        for ticket in tickets:
            ticket_str += getattr(ticket, display_method)() + '\n'
        ticket_str = name + (line_len - len(name)) * '-' + '\n' + ticket_str
        ticket_elements.append(DisplayElement(ticket_str))

    if len(ticket_elements) > 1:
        combined_element = fold(ticket_elements)
        further_combined = fold([board_element, combined_element])
        print(further_combined.content)
    else:
        combined_element = fold([board_element, ticket_elements[0]])
        print(combined_element.content)


def fold(display_elements: List[DisplayElement]) -> DisplayElement:
    """Split the incoming list of elements into two side-by-side columns"""
    middle = len(display_elements) // 2
    column1 = display_elements[:middle]
    column2 = display_elements[middle:]

    # Flatten the List of display elements into a list of rows. (each display element contains rows)
    column1_rows = []
    for element in column1:
        for row in element.row_wise_data:
            column1_rows.append(row)

    column2_rows = []
    for element in column2:
        for row in element.row_wise_data:
            column2_rows.append(row)

    combined_str = ''
    space = ' '
    fill_value = len(column1_rows[0]) * ' ' if len(column2_rows) > len(column1_rows) else len(column2_rows[0]) * ' '
    for col1, col2 in zip_longest(column1_rows, column2_rows, fillvalue=fill_value):
        combined_str += col1 + 5 * space + col2 + '\n'
    return DisplayElement(combined_str)
