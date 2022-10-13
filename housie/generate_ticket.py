"""Housie Ticket generation logic"""

__author__ = 'Aaron Alphonso'
__email__ = 'alphonsoaaron1993@gmail.com'

from collections import defaultdict
from random import choice, randint
from typing import List, Set, Dict, DefaultDict

from housie.constants import Number, Row, ColumnRange, COLUMN_RANGES
from housie.models import Ticket


def generate_ticket() -> Ticket:
    """Generates a Housie Ticket containing 15 randomly selected numbers based on the following rules

    * A Housie ticket has 15 numbers.
    * These 15 numbers are placed in a 3 rows x 9 cols grid (27 possible spaces).
    * There has to be exactly 5 numbers in each row.
    * There has to be at least one number in each column.
    * The numbers in each column must belong to that column's allowed range.
        Column 1: 1-9
        Column 2: 10-19
        Column 3: 20-29
        .      .      .
        .      .      .
        .      .      .
        Column 8: 70-79
        Column 9: 80-90

    Based on the rules above we have to select the numbers.
    """
    # The list of ranges for each column. Make a copy as we mutate it during our selection process
    column_ranges: List[ColumnRange] = COLUMN_RANGES.copy()

    # The numbers selected for the ticket
    ticket_numbers: Set[Number] = set()

    # Saving the numbers column-wise to ensure we select at max 3 numbers for each column and also
    # to help in distributing them into the 3 rows later
    column_wise_numbers: DefaultDict[ColumnRange, List[Number]] = defaultdict(list)

    # Select one number from each column range. This will give us 9 numbers
    for column_range in column_ranges:
        selected_number = select_unique_number_from_range(
            column_range=column_range, already_selected=column_wise_numbers[column_range])
        ticket_numbers.add(selected_number)
        column_wise_numbers[column_range].append(selected_number)

    # Select the remaining 6 numbers at random from the columns.
    while len(ticket_numbers) < 15:
        selected_range = choice(column_ranges)
        selected_number = select_unique_number_from_range(
            column_range=selected_range, already_selected=column_wise_numbers[selected_range])

        ticket_numbers.add(selected_number)
        column_wise_numbers[selected_range].append(selected_number)

        # If we have selected 3 numbers for a specific column, remove that column from the further selection process
        if len(column_wise_numbers[selected_range]) == 3:
            column_ranges.remove(selected_range)

    # Convert to a regular dict now as we no longer need the defaultdict properties
    # Now we assign the 15 selected numbers into the 3 rows.
    rows = assign_to_rows(dict(column_wise_numbers))
    return Ticket(rows)


def select_unique_number_from_range(column_range: ColumnRange, already_selected: List[Number]) -> Number:
    """Selects and returns a number randomly from a ColumnRange. If the number has already been selected before, then
    re-select a new number"""
    selected_number: Number = randint(column_range.start, column_range.end)
    # If the selected_number is already_selected, select a new number until we get a unique number
    while selected_number in already_selected:
        selected_number = randint(column_range.start, column_range.end)
    return selected_number


def assign_to_rows(column_wise_numbers: Dict[ColumnRange, List[Number]]) -> List[Row]:
    """Distribute the ticket numbers into the 3 rows such that each row has exactly 5 numbers

    Start with the columns that have 3 numbers, followed by the columns that have two numbers and
    then columns that have 1 number.
    Assign the numbers in a round-robin fashion.
    """
    ticket: List[Row] = [[], [], []]
    row_num = 0
    for col_len in [3, 2, 1]:
        columns = list(filter(lambda x: len(x) == col_len, column_wise_numbers.values()))
        for column in columns:
            row_num = insert_from_columns_to_rows(column, ticket, row_num)
    for row in ticket:
        row.sort()
    return ticket


def insert_from_columns_to_rows(column: List[Number], ticket: List[Row], row_num: int) -> int:
    """Insert numbers from the columns into the rows in a round-robin fashion.
    Returns the row_num, so it can be persisted between calls"""
    numbers = sorted(column)

    # If we have to assign numbers to row 3 and row 1 of the same column, we should always assign the smaller
    # number to the higher row, i.e. row 1. To do this, we have the following logic:
    # Figure out which rows we will be assigning the column numbers to. Assign in round robin logic starting from the
    # smallest row num possible.
    row_nums_to_assign_to = []
    for _ in numbers:
        row_nums_to_assign_to.append(row_num)
        row_num = (row_num + 1) % 3

    # This is the last row position that we are assigning to in the round-robin assignment. Return this for the
    # assignment of the numbers from the next column
    last_row_num = row_num
    row_nums_to_assign_to.sort()
    for number, row_num in zip(numbers, row_nums_to_assign_to):
        ticket[row_num].append(number)
    return last_row_num


def demo_ticket_generation() -> None:
    """Demonstrates ticket generation by generating a ticket and printing it visually"""
    sample_ticket = generate_ticket()
    print("Concise representation")
    print(sample_ticket.minimalistic_display())

    print("Structural representation")
    print(sample_ticket.structural_display())
