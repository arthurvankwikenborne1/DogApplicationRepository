class Dog:

	def __init__(self, name, breed, age,gender, status, arrival_date, description):
		self.name = name
		self.breed = breed
		self.age = age
		self.gender = gender
		self.status = status
		self.arrival_date = arrival_date
		self.description = description

	def __str__(self):
		return f"name : {self.name}\nbreed : {self.breed}\nAge : {self.age}\nGender : {self.gender}\nStatus: {self.status}\nArrival date : {self.arrival_date}\nDescription : {self.description}"








