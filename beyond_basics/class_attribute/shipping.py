
class ShippingContainer:

	HEIGHT_FT = 8.5
	WIDTH_FT = 8.0

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
	def create_empty(cls, owner_code, length_ft, *args, **kwargs):
		""" cls calling ShippingContainer contructor """
		return cls(owner_code, length_ft, contents=None, *args, **kwargs)

	@classmethod
	def create_with_items(cls, owner_code, items, length_ft, *args, **kwargs):
		return cls(owner_code, length_ft, contents=list(items), *args, **kwargs)

	def __init__(self, owner_code, length_ft, contents):
		self.contents = contents
		self.length_ft = length_ft
		# use self instead of class name ShippingContainer for polymorphism, other wise in code U will be used
		self.code = self._make_code(
			owner_code,
			ShippingContainer._get_next_serial())

	@property
	def volume_ft3(self):
		return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft

class RefrigeratedShippingContainer(ShippingContainer):

	MAX_TEMP_CELSIUS = 4.0

	FRIDGE_VOLUME_FT3 = 100

	@staticmethod
	def _make_code(owner_code, serial):
		return (owner_code+'R'+str(serial))

	@staticmethod
	def _c_to_f(temp_celsius):
		return temp_celsius * 9/5 + 32
	
	@staticmethod
	def _f_to_c(temp_fahrenheit):
		return (temp_fahrenheit - 32) * 5/9

	def __init__(self,owner_code, length_ft, contents, temp_celsius):
		# with super() we get a reference to the base class instance to extend the base class version
		super().__init__(owner_code, length_ft, contents)
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

	@property
	def volume_ft3(self):
		return (super.volume_ft3 - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT3)


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):

	MIN_TEMP_CELSIUS = -20.0

	@RefrigeratedShippingContainer.temp_celsius.setter
	def temp_celsius(self, value):
		if not(HeatedRefrigeratedShippingContainer.MIN_TEMP_CELSIUS
				<= value
				<= RefrigeratedShippingContainer.MAX_TEMP_CELSIUS):
			raise ValueError ("Temperature out of range!")
		self._temp_celsius = value

