import sys
import os
from datetime import datetime

today = datetime.today().strftime("%Y-%m-%d")

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(repo_root)

from app.database import create_tables
from app.operations import add_dog, add_adoption, get_all_dogs, get_all_adoptions, delete_all_dogs, delete_all_adoptions


create_tables()

delete_all_dogs()
delete_all_adoptions()


continue_loop = True
while continue_loop:
    answer = input("Would you like to add a dog? : <yes> <no>")
    if(answer.lower()=="no"):
        continue_loop = False
    elif(answer.lower()=="yes"):
        dogName = input("What is the name of your dog? : ")
        dogBreed = input("What breed is the dog? : ")
        dogAge = int(input("How old is the dog? (in years) :"))
        dogGender = input("What gender is the dog? : ")
        dogStatus = input("What is the status of the dog? : ")
        dogArrivalDate = input("When did the dog arrive? : ")
        dogDescription = input("Describe the dog: ")
        add_dog(dogName, dogBreed,dogAge,dogGender,dogStatus,dogArrivalDate, dogDescription)


print("All dogs in the database")
dogs = get_all_dogs()
for dog in dogs:
    print(dog)

continue_loop_adoption = True
while continue_loop_adoption:
        answer = input("Would you like to adopt a dog? : <yes> <no>")
        if(answer.lower()=="yes"):
            name_dog = input("What is the name of the dog?")
            dog_id = None
            for dog in dogs:
                if(dog[1].lower()==name_dog.lower()):
                    dog_id=dog[0]
            adoptorName = input("What is your name? : ")
            adoptorMail = input("What is your mail address? : ")
            adoptDate = today
            add_adoption(dog_id,adoptorName,adoptorMail,adoptDate)
        elif(answer.lower()=="no"):
            continue_loop_adoption = False

print("\nAlle adopties in de database:")
adoptions = get_all_adoptions()
for adoption in adoptions:
    print(adoption)
