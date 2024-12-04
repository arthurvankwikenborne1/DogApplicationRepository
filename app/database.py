import sqlite3

def create_tables():
    db_path = "../data/dogshelter.db"
    db_connection = sqlite3.connect(db_path)
    my_cursor = db_connection.cursor()

    create_dogs_table_query = """
    CREATE TABLE IF NOT EXISTS dogs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        breed TEXT,
        age INTEGER,
        gender TEXT,
        status TEXT DEFAULT 'Beschikbaar',
        arrival_date TEXT,
        description TEXT,
    )
    """
    
    create_adoptions_table_query = """
    CREATE TABLE IF NOT EXISTS adoptions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dog_id INTEGER,
        adopter_name TEXT NOT NULL,
        adopter_contact TEXT,
        adopt_date TEXT,
        FOREIGN KEY (dog_id) REFERENCES dogs(id)
    )
    """
    
    my_cursor.execute(create_dogs_table_query)
    my_cursor.execute(create_adoptions_table_query)
    
    db_connection.commit()
    db_connection.close()

def add_dog(name, breed, age, gender, status, arrival_date, description):
    db_path = "../data/dogshelter.db"
    db_connection = sqlite3.connect(db_path)
    my_cursor = db_connection.cursor()

    add_dog_query = """
    INSERT INTO dogs (name, breed, age, gender, status, arrival_date, description)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
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
    VALUES (?, ?, ?, ?, ?, ?, ?)
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

create_tables()

#add_dog("Luna", "Siberian Husky", 2, "Female", "Beschikbaar", "2024-12-04", "Energetic, loves running and playing outside.", "https://example.com/luna.jpg")
#add_adoption(1, "Alice Johnson", "alice.johnson@example.com", "2024-12-05", 150.00, "Luna is a perfect companion, very loving!", "Definitief")
