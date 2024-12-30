class Adoptor:
	def __init__(self,name,contact):
		self.name = name
		self.contact = contact

	def __str__(self):
		return f"Name: {self.name}, Address : {self.contact}"