"""Model representing the Housie board"""

__author__ = 'Aaron Alphonso'
__email__ = 'alphonsoaaron1993@gmail.com'

from typing import List, Optional
from random import choice

from housie.constants import SelectedPool, RemainingPool, Number, NUMBER_POOL
from housie.utils import clear_screen


class Board:
    """Represents the Housie board state and logic to run the game and display the state"""

    def __init__(self, already_selected: Optional[SelectedPool] = None) -> None:
        """Initialize the state of the board.
        Either a blank new board, or some pre-selected numbers to represent an already mid-way game"""
        # Variables for holding game state
        self.remaining: RemainingPool = []
        self.selected: SelectedPool = []
        if already_selected:
            self.init_custom_game(already_selected)
        else:
            self.init_new_game()

    def pick_next(self) -> Optional[Number]:
        """Picks a number at random from the remaining pool of numbers.
        The chosen number is removed from the remaining_pool and added to the selected pool"""
        if not self.remaining:
            return None
        number = choice(self.remaining)
        return self.pick_manual(number)

    def pick_many(self, count: int) -> List[Number]:
        """Pick multiple numbers from the remaining pool of numbers
        The chosen numbers are removed from the remaining pool and added to the selected pool"""
        return list(filter(None, [self.pick_next() for i in range(count)]))

    def pick_manual(self, number: Number) -> Number:
        """Manually pick a number from the number pool.
        The chosen number is removed from the remaining pool and added to the selected pool"""
        if number in self.remaining:
            self.remaining.remove(number)
            self.selected.append(number)
        return number

    def init_new_game(self) -> None:
        """Initialize a new game"""
        self.selected = []
        self.remaining = NUMBER_POOL.copy()

    def init_custom_game(self, already_selected: List[Number]) -> None:
        """Initialize a new game with a set of numbers already called out"""
        self.selected = already_selected
        self.remaining = list(set(NUMBER_POOL) - set(already_selected))

    def last_5_selected(self) -> List[Number]:
        """Returns a list of the last 5 numbers called out"""
        return self.selected[-5:]

    def display_board(self) -> str:
        """Display the Housie Board of selected numbers visually in the console"""
        board = ''
        board += '------------------ Housie Board -------------------\n'
        row_size = 10
        num_rows = len(NUMBER_POOL) // row_size
        for row_num in range(num_rows):
            start = row_num * row_size
            end = (row_num * row_size) + row_size
            for num in NUMBER_POOL[start: end]:
                if num in self.selected:
                    board += '|{: 3} '.format(num)
                else:
                    board += '|' + ' ' * 4
            board += '|'
            board += '\n---------------------------------------------------\n'

        last_5_numbers_str = ", ".join(map(str, reversed(self.last_5_selected())))
        board += 'Last 5 Numbers called: {}\n'.format(last_5_numbers_str)
        board += 'Left in the bag: {}\n'.format(len(self.remaining))
        return board


def demo_board() -> None:
    """Test function to print out how the board would look with a few numbers filled"""
    housie_board = Board()
    housie_board.pick_many(40)
    clear_screen()
    print(housie_board.display_board())
