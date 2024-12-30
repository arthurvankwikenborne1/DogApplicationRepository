import sys
import os

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(repo_root)

from app.adoptions.adoptions import Adoptions
from app.adoptions.adoptor.adoptor import Adoptor
from app.adoptions.dog.dog import Dog

def testMakeDog():
	try:
		name = "Roos"
		breed = "American Stafford"
		age= 5
		gender = "female"
		status = "beschikbaar"
		arrival_date = "2021-12-04"
		description = "In het asiel is Roos geduldig en lief naar haar verzorgers."
		dog = Dog(name, breed, age, gender, status,arrival_date, description)
		return dog
	except ValueError as err:
		print("Wrong user input: {err}")
	finally:
		print("----MAKING DOG----")

def testMakeAdoptor():
	try:
		name="Arthur Van Kwikenborne"
		address ="Anzegemseweg 20 8790 Waregem"
		adoptor = Adoptor(name,address)
		return adoptor
	except ValueError as err:
		print("Wrong user input: {err}")
	finally:
		print("----MAKING ADOPTOR----")

def testMakeAdoption():
	try:
		dog = testMakeDog()
		adoptor = testMakeAdoptor()
		adoption = Adoptions(dog,adoptor)
		print(adoption)
	except ValueError as err:
		print("Wrong user input: {err}")
	finally:
		print("----ADOPTION COMPLETE----")


testMakeAdoption()