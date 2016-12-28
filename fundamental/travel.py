""" model for airplanes """

class Flight:

	def __init__(self, number):
		if not number[:2].isalpha():
			raise ValueError("Airline code with value '{}' does not exist".format(number))

		if not number[:2].isupper():
			raise ValueError("Invalid airline code '{}'".format(number))

		if not(number[2:].isdigit() and int(number[2:]) <= 9999):
			raise ValueError("Invalid route number '{}'".format(number))

		self._number = number

	def number(self):
		print(self._number[:2])
		return self._number

	""" Get airline code """
	def airline(number):
		return self._number[:2]

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