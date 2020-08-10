"""Simple Housie Ticket class to store and display a ticket"""
from typing import List, Dict, Optional, Set

from constants import Row, COLUMN_RANGES, Number
from utils import load_json, strike_through, clear_screen


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

	def __repr__(self):
		return "Ticket(numbers={})".format(self.rows)

	def display_ticket(self) -> str:
		"""Display the ticket"""
		return self.structural_display()

	def minimalistic_display(self):
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

	def structural_display(self):
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

	def get_structural_representation(self):
		"""Returns a representation of the ticket in a 3 x 9 grid with blank squares represented by None

		This representation can be used for a graphical display.
		"""
		representation = []
		for row in self.rows:
			new_row = []
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
	"""Reads the followed_tickets.json file and returns a dict of name : tickets"""
	ticket_data = load_json(file_name)
	if not ticket_data:
		return None
	for name, tickets in ticket_data.items():
		tickets = list(map(Ticket, tickets))
		ticket_data[name] = tickets
	return ticket_data


def demo():
	ticket_data = load_tickets('followed_tickets.json')

	for name, tickets in ticket_data.items():
		for ticket in tickets:
			ticket.mark_number(1)
			ticket.mark_number(20)
			ticket.mark_number(59)

	clear_screen()
	for name, tickets in ticket_data.items():
		print(name)
		for ticket in tickets:
			print(ticket.display_ticket())


if __name__ == '__main__':
	demo()
