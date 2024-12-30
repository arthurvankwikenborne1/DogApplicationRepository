import sqlite3

def add_dog(name, breed, age, gender, status, arrival_date, description):
    db_path = "../data/dogshelter.db"
    db_connection = sqlite3.connect(db_path)
    my_cursor = db_connection.cursor()

    add_dog_query = """
    INSERT INTO dogs (name, breed, age, gender, status, arrival_date, description)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    
    my_cursor.execute(add_dog_query, (name, breed, age, gender, status, arrival_date, description))
    
    db_connection.commit()
    db_connection.close()
    print(f"De hond {name} is succesvol toegevoegd aan de database!")

def add_adoption(dog_id, adopter_name, adopter_contact, adopt_date):
    db_path = "../data/dogshelter.db"
    db_connection = sqlite3.connect(db_path)
    my_cursor = db_connection.cursor()

    add_adoption_query = """
    INSERT INTO adoptions (dog_id, adopter_name, adopter_contact, adopt_date)
    VALUES (?, ?, ?, ?)
    """
    
    my_cursor.execute(add_adoption_query, (dog_id, adopter_name, adopter_contact, adopt_date))
    my_cursor.execute("""
    UPDATE dogs
    SET status = 'Geplaatst'
    WHERE id = ?
    """, (dog_id,))
    
    db_connection.commit()
    db_connection.close()
    print(f"Adoptie van hond met ID {dog_id} is succesvol geregistreerd!")

def get_all_dogs():
    db_path = "../data/dogshelter.db"
    db_connection = sqlite3.connect(db_path)
    my_cursor = db_connection.cursor()

    get_all_dogs_query = "SELECT * FROM dogs"
    
    my_cursor.execute(get_all_dogs_query)
    dogs = my_cursor.fetchall()
    
    db_connection.close()
    return dogs

def get_all_adoptions():
    db_path = "../data/dogshelter.db"
    db_connection = sqlite3.connect(db_path)
    my_cursor = db_connection.cursor()

    get_all_adoptions_query = "SELECT * FROM adoptions"
    
    my_cursor.execute(get_all_adoptions_query)
    adoptions = my_cursor.fetchall()
    
    db_connection.close()
    return adoptions

def delete_all_dogs():
    db_path = "../data/dogshelter.db"
    db_connection = sqlite3.connect(db_path)
    my_cursor = db_connection.cursor()

    delete_all_dogs_query = "DELETE FROM dogs"
    
    my_cursor.execute(delete_all_dogs_query)
    db_connection.commit()
    db_connection.close()
    print("Alle honden zijn succesvol verwijderd uit de database.")

def delete_all_adoptions():
    db_path = "../data/dogshelter.db"
    db_connection = sqlite3.connect(db_path)
    my_cursor = db_connection.cursor()

    delete_all_adoptions_query = "DELETE FROM adoptions"
    
    my_cursor.execute(delete_all_adoptions_query)
    db_connection.commit()
    db_connection.close()
    print("Alle adopties zijn succesvol verwijderd uit de database.")