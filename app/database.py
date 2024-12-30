

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
        description TEXT
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

create_tables()