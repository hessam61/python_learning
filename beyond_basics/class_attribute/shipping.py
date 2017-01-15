
class ShippingContainer:

	next_serial = 1000

	@staticmethod
	def _make_code(owner_code, serial):
		return (owner_code+'U'+str(serial))

	@classmethod
	def _get_next_serial(cls):
		result = cls.next_serial
		cls.next_serial += 1
		return result

	@classmethod
	# adding *args, and **kwargs to support the "temp_celsius" attribute in refrigerated sub class
	def create_empty(cls, owner_code, *args, **kwargs):
		""" cls calling ShippingContainer contructor """
		return cls(owner_code, contents=None, *args, **kwargs)

	@classmethod
	def create_with_items(cls, owner_code, items, *args, **kwargs):
		return cls(owner_code, contents=list(items), *args, **kwargs)

	def __init__(self, owner_code, contents):
		self.owner_code = owner_code
		self.contents = contents
		# use self instead of class name ShippingContainer for polymorphism, other wise in code U will be used
		self.code = self._make_code(
			owner_code,
			ShippingContainer._get_next_serial())


class RefrigeratedShippingContainer(ShippingContainer):

	MAX_TEMP_CELSIUS = 4.0

	@staticmethod
	def _make_code(owner_code, serial):
		return (owner_code+'R'+str(serial))

	@staticmethod
	def _c_to_f(temp_celsius):
		return temp_celsius * 9/5 + 32
	
	@staticmethod
	def _f_to_c(temp_fahrenheit):
		return (temp_fahrenheit - 32) * 5/9

	def __init__(self,owner_code, contents, temp_celsius):
		# with super() we get a reference to the base class instance to extend the base class version
		super().__init__(owner_code,contents)
		self.temp_celsius = temp_celsius

	@property
	def temp_celsius(self):
		return self._temp_celsius

	@temp_celsius.setter
	def temp_celsius(self, value):
		if value > RefrigeratedShippingContainer.MAX_TEMP_CELSIUS:
			raise ValueError ("Temperature is too Hot!")
		self._temp_celsius = value

	@property
	def temp_fahrenheit(self):
		return RefrigeratedShippingContainer._c_to_f(self.temp_celsius)

	@temp_fahrenheit.setter
	def temp_fahrenheit(self, value):
		self.temp_celsius = RefrigeratedShippingContainer._f_to_c(value)

