
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
	# adding *args, and **kwargs to support the "temp" attribute in refrigerated sub class
	def creat_empty(cls, owner_code, *args, **kwargs):
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

	MAX_TEMP = 4.0

	@staticmethod
	def _make_code(owner_code, serial):
		return (owner_code+'R'+str(serial))


	def __init__(self,owner_code, contents, temp):
		# with super() we get a reference to the base class instance to extend the base class version
		super().__init__(owner_code,contents)
		if temp > RefrigeratedShippingContainer.MAX_TEMP:
			raise ValueError("Temperature is too Hot!")
		self.temp = temp