"""Simple Housie Ticket class to store and display a ticket"""

__author__ = 'Aaron Alphonso'
__email__ = 'alphonsoaaron1993@gmail.com'

from typing import List, Dict, Optional, Set

from housie.constants import Row, COLUMN_RANGES, Number, NUMBER_POOL
from housie.utils import load_json, strike_through, clear_screen


class Ticket:
    """Simple structure to store and display the ticket"""

    def __init__(self, rows: List[Row]):
        # self.rows will hold only the non-None elements
        self.rows: List[Row] = []
        # Storing all the numbers in a flat list
        self.numbers: List[int] = []
        for row in rows:
            new_row = []
            for number in row:
                if number:
                    self.numbers.append(number)
                    new_row.append(number)
            self.rows.append(new_row)
        # All the numbers that are selected
        self.selected: Set[Number] = set()

    def mark_number(self, number: int) -> None:
        """Updates the ticket marking the matching number as selected"""
        if number in self.numbers:
            self.selected.add(number)

    def mark_numbers(self, numbers: List[int]) -> None:
        """Updates the ticket marking the matching numbers as selected"""
        for number in numbers:
            self.mark_number(number)

    def __repr__(self) -> str:
        return "Ticket(numbers={})".format(self.rows)

    def display_ticket(self) -> str:
        """Display the ticket"""
        return self.structural_display()

    def minimalistic_display(self) -> str:
        """Displays the ticket in a minimalistic format"""
        ticket_representation = ''
        for row in self.rows:
            row_elems = []
            for number in row:
                if number:
                    if number in self.selected:
                        row_elems.append(strike_through('{: 3} '.format(number)))
                    else:
                        row_elems.append('{: 3} '.format(number))
            ticket_representation += ','.join(row_elems) + '\n'
        return ticket_representation

    def structural_display(self) -> str:
        """Displays the ticket in a 3 x 9 grid as is seen on traditional tickets"""
        ticket_representation = ''
        for row in self.get_structural_representation():
            for num in row:
                if num:
                    if num in self.selected:
                        ticket_representation += strike_through('{: 3} '.format(num))
                    else:
                        ticket_representation += '{: 3} '.format(num)
                else:
                    ticket_representation += '  - '
            ticket_representation += '\n'
        return ticket_representation

    def get_structural_representation(self) -> List[List[Optional[Number]]]:
        """Returns a representation of the ticket in a 3 x 9 grid with blank squares represented by None

        This representation can be used for a graphical display.
        """
        representation = []
        for row in self.rows:
            new_row: List[Optional[Number]] = []
            row_iter = iter(row)
            num = next(row_iter)
            if num:
                for start, end in COLUMN_RANGES:
                    if num and start <= num <= end:
                        new_row.append(num)
                        try:
                            num = next(row_iter)
                        except StopIteration:
                            # Add 'None' to the remaining elements of the row
                            new_row.extend([None] * (9 - len(new_row)))
                            break
                    else:
                        new_row.append(None)
                representation.append(new_row)
        return representation


def load_tickets(file_name: str) -> Optional[Dict[str, List[Ticket]]]:
    """Reads the input file and tries to parse the data into a dict of name : tickets"""
    ticket_data = load_json(file_name)
    if not ticket_data:
        return None
    for name, tickets in ticket_data.items():
        tickets = list(map(Ticket, tickets))
        ticket_data[name] = tickets
    return ticket_data


def demo_ticket() -> None:
    """Method to demonstrate how tickets would look like with some numbers marked"""
    from housie.generate_ticket import generate_ticket

    # Generate some sample tickets
    names = ['Thor', 'Ironman', 'Spiderman']
    ticket_data = {}
    for name in names:
        ticket = generate_ticket()
        ticket_data[name] = [ticket]

    # Mark some random numbers so we can see the output
    from random import sample
    random_numbers = sample(NUMBER_POOL, 40)
    for name, tickets in ticket_data.items():
        for ticket in tickets:
            for number in random_numbers:
                ticket.mark_number(number)

    # Display the tickets
    clear_screen()
    for name, tickets in ticket_data.items():
        print(name)
        for ticket in tickets:
            print(ticket.display_ticket())
