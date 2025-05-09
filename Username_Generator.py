import random
import string

adjectives = ["Mighty", "Swift", "Gentle", "Fiery", "Jolly", "Sneaky", "Bold", "Glorious", "Daring", "Vibrant"]
nouns = ["Falcon", "Shadow", "Rogue", "Wizard", "Lion", "Sphinx", "Gladiator", "Cyclone", "Crusader", "Vortex"]

def generate_username(add_numbers=True, add_special_chars=False, length=12):
    """Generate a random username based on user preferences."""
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adjective + noun
    
    if add_numbers:
        username += str(random.randint(100, 999))  
    
    if add_special_chars:
        username += random.choice("!@#$%^&*") 
    
    return username[:length] 

def save_to_file(username):
    """Save generated username to a file."""
    with open("usernames.txt", "a") as file:
        file.write(username + "\n")

def main():
    print("Welcome to the Unique Username Generator!")
    
    add_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
    add_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"
    length = input("Enter desired length (or press Enter for default): ").strip()
    
    length = int(length) if length.isdigit() else 12  
    
    username = generate_username(add_numbers, add_special_chars, length)
    
    print(f"Generated Username: {username}")
    
    save_to_file(username)
    print("Your username has been saved to usernames.txt.")

if _name_ == "_main_":
    main()
