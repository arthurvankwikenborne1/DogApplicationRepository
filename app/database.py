import sqlite3
import os

def create_tables():
    db_path = os.path.join("..", "data", "dogshelter.db")  # Verbindt naar de 'data' map boven de huidige directory
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dogs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        breed TEXT,
        age INTEGER,
        gender TEXT,
        status TEXT DEFAULT 'Beschikbaar',
        arrival_date TEXT,
        description TEXT,
        photo_url TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS adoptions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dog_id INTEGER,
        adopter_name TEXT NOT NULL,
        adopter_contact TEXT,
        adopt_date TEXT,
        adopt_fee REAL,
        adopter_feedback TEXT,
        adoption_type TEXT DEFAULT 'Definitief',
        FOREIGN KEY (dog_id) REFERENCES dogs(id)
    )
    """)

    connection.commit()
    connection.close()

def add_dog(name, breed, age, gender, status, arrival_date, description, photo_url):
    db_path = os.path.join("..", "data", "dogshelter.db")
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO dogs (name, breed, age, gender, status, arrival_date, description, photo_url)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (name, breed, age, gender, status, arrival_date, description, photo_url))
    connection.commit()
    connection.close()
    print(f"De hond {name} is succesvol toegevoegd aan de database!")

def add_adoption(dog_id, adopter_name, adopter_contact, adopt_date, adopt_fee, adopter_feedback, adoption_type):
    db_path = os.path.join("..", "data", "dogshelter.db")
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO adoptions (dog_id, adopter_name, adopter_contact, adopt_date, adopt_fee, adopter_feedback, adoption_type)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (dog_id, adopter_name, adopter_contact, adopt_date, adopt_fee, adopter_feedback, adoption_type))
    cursor.execute("""
    UPDATE dogs
    SET status = 'Geplaatst'
    WHERE id = ?
    """, (dog_id,))
    connection.commit()
    connection.close()
    print(f"Adoptie van hond met ID {dog_id} is succesvol geregistreerd!")

create_tables()

#add_dog("Luna", "Siberian Husky", 2, "Female", "Beschikbaar", "2024-12-04", "Energetic, loves running and playing outside.", "http://example.com/photos/luna.jpg")

#add_adoption(1, "Alice Johnson", "alice.johnson@example.com", "2024-12-05", 150.00, "Luna is a perfect companion, very loving!", "Definitief")
