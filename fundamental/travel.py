""" model for airplanes """

class Flight:
	""" Flight with a passenfer airplanes """
	def __init__(self, number, aircraft):
		if not number[:2].isalpha():
			raise ValueError("Airline code with value '{}' does not exist".format(number))

		if not number[:2].isupper():
			raise ValueError("Invalid airline code '{}'".format(number))

		if not(number[2:].isdigit() and int(number[2:]) <= 9999):
			raise ValueError("Invalid route number '{}'".format(number))

		self._number = number
		self._aircraft = aircraft

		#gets the range for rows and number of seats from seating_plan()
		rows, seats = self._aircraft.seating_plan()
		self._seating = [None] + [{letter: None for letter in seats} for _ in rows]
		print (self._seating)

	def number(self):
		print(self._number[:2])
		return self._number

	""" Get airline code """
	def airline(number):
		return self._number[:2]

	def aircraft_model(self):
		return self._aircraft.model()

	def allocate_seat(self, seat, passenger):
		""" Allocate one seat to each passenger 
		
		Arguments:	Seat designator like "12B"
					Passenger: Just a text string name

		Raises:		ValueError if seat number is invalid or unavailable 
		"""
		rows, seat_letter = self._aircraft.seating_plan()

		letter = seat[-1]

		if letter not in seat_letter:
			raise ValueError("Invalid seat letter{}".format(letter))

		row_text = seat[:-1]

		try:
			row = int(row_text)
		except ValueError:
			raise ValueError("Invalid seat row {}".format(row_text))

		if row not in rows:
			raise ValueError("Invalid row number {}".format(row))

		if self._seating[row][letter] is not None:
			raise ValueError("Seat {} is taken".format(seat))

		self._seating[row][letter] = passenger

class Aircraft:
	def __init__(self,registration,model,num_rows,num_seats_per_row):
		self._registration = registration
		self._model = model
		self._num_rows = num_rows
		self._num_seats_per_row = num_seats_per_row

	def registration(self):
		return self._registration

	def model(self):
		return self._model

	def seating_plan(self):
		return (range(1, self._num_rows + 1),
				"ABCDEFGHJK"[:self._num_seats_per_row])
		print(range(1, self._num_rows + 1),
				"ABCDEFGHJK"[:self._num_seats_per_row])