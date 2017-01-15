
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
	def creat_empty(cls, owner_code):
		""" cls calling ShippingContainer contructor """
		return cls(owner_code, contents=None)

	@classmethod
	def create_with_items(cls, owner_code, items):
		return cls(owner_code, contents=list(items))

	def __init__(self, owner_code, contents):
		self.owner_code = owner_code
		self.contents = contents
		# use self instead of class name ShippingContainer for polymorphism, other wise in code U will be used
		self.code = self._make_code(
			owner_code,
			ShippingContainer._get_next_serial())


class RefrigeratedShippingContainer(ShippingContainer):

	@staticmethod
	def _make_code(owner_code, serial):
		return (owner_code+'R'+str(serial))