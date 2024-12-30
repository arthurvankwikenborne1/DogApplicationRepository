import sys
import os

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if repo_root not in sys.path:
    sys.path.append(repo_root)

from app.adoptions.dog.dog import Dog
from app.adoptions.adoptor.adoptor import Adoptor
from datetime import datetime

class Adoptions:
	def __init__(self, Dog, Adoptor):
		self.Dog = Dog
		self.Adoptor = Adoptor
		self.date = datetime.today().strftime('%Y-%m-%d')

	def __str__(self):
		return f"ADOPTIONS: \nadopted dog : {self.Dog.name}\nadoptor: {self.Adoptor.name} \nDate : {self.date}"
