# Dog Shelter Management System

## Goal of the Application

The goal of this application is to manage the operations of a dog shelter. It allows users to:

- Add new dogs to the shelter database.
- Register adoptions of dogs.
- View all dogs in the shelter.
- View all adoption records.

This system ensures that each dog and adoption is properly tracked, including information such as breed, age, gender, adoption status, and adopter details.

## Functionalities Built

### 1. **Add a Dog**

- Adds a new dog to the shelter's database.
- Captures details such as:
  - Name, breed, age, gender, arrival date, description, and status.

### 2. **Adopt a Dog**

- Allows users to adopt a dog.
- Once a dog is adopted, the status of the dog is updated to "Geplaatst" (Adopted).
- Tracks adopter details such as name, contact information, and the adoption date.

### 3. **View All Dogs**

- Retrieves and displays a list of all dogs currently in the shelter.

### 4. **View All Adoptions**

- Retrieves and displays a list of all adoption records, including the name of the dog, the adopter's name, and the adoption date.

### 5. **Delete All Dogs and Adoptions**

- Provides functionality to clear all data from the dogs and adoptions tables in the database. Useful for resetting or clearing the database.

## Running the Application

### Requirements

- Python 3.x
- SQLite database
- Required Python packages:
  - `sqlite3` (Included with Python)

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```
