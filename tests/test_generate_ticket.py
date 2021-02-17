""" Unit tests for the generate_ticket module """
import collections
import random
from typing import List, Dict, Counter

import pytest
from housie.constants import NUMBER_POOL, COLUMN_RANGES, Number

from housie import generate_ticket, Ticket


@pytest.fixture
def ticket() -> Ticket:
    """ Generate and return a ticket for testing """
    random.seed(10000)  # So that we get reproducible test results
    return generate_ticket()


@pytest.fixture
def number_to_column_mapping() -> Dict[Number, int]:
    """ Returns a mapping which helps determine which column (1-9) a specific number belongs to """
    # Build a mapping of column_number to corresponding numbers allowed in the column
    column_values_mapping: Dict[int, List[Number]] = {}
    for index, column_range in enumerate(COLUMN_RANGES):
        column_values_mapping[index] = list(range(column_range.start, column_range.end + 1))
    print(column_values_mapping)

    # Reverse the mapping to get a mapping of number to column_number
    number_to_column_map: Dict[Number, int] = {}
    for column_number, values in column_values_mapping.items():
        for value in values:
            number_to_column_map[value] = column_number

    # This map has keys has numbers and values as the column_number to which the number belongs
    return number_to_column_map


def test_ticket_contains_15_numbers(ticket: Ticket) -> None:
    """ Test that the generated ticket contains exactly 15 numbers """
    assert len(ticket.numbers) == 15


def test_ticket_contains_unique_numbers(ticket: Ticket) -> None:
    """ Test that all numbers in the ticket are unique """
    assert len(set(ticket.numbers)) == len(ticket.numbers)


def test_ticket_contains_all_valid_numbers(ticket: Ticket) -> None:
    """ Test that all numbers in the ticket are from the NUMBER_POOL """
    ticket_numbers = set(ticket.numbers)
    all_valid_numbers = set(NUMBER_POOL)
    assert ticket_numbers.issubset(all_valid_numbers)


def test_ticket_contains_3_rows(ticket: Ticket) -> None:
    """ Test that a ticket contains exactly 3 rows """
    assert len(ticket.rows) == 3


def test_every_row_contains_5_numbers(ticket: Ticket) -> None:
    """ Test that every row in the ticket contains exactly 5 numbers """
    for row in ticket.rows:
        assert len(row) == 5


def test_every_column_contains_between_1_and_3_numbers(ticket: Ticket,
                                                       number_to_column_mapping: Dict[Number, int]) -> None:
    """ Test that every column in the ticket contains at least one number and at most three numbers """
    columns: Counter[int] = collections.Counter()  # Use a counter to track how many numbers are in each column
    for number in ticket.numbers:
        column_number = number_to_column_mapping[number]
        columns[column_number] += 1

    # If there is at least one number in every column, we should have exactly 9 columns
    # This check implicitly validates that every column has at least one number
    assert len(columns) == 9

    # Check that every column has at most 3 numbers
    for column_number, number_count in columns.items():
        assert number_count <= 3
