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