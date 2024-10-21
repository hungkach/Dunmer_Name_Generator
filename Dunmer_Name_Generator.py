import os
import sys

# Set the working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("Current working directory:", os.getcwd())
print("Files in the current directory:", os.listdir(os.getcwd()))

import random  # Importing random for name generation

# Function to load names from a file
def load_names_from_file(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return []
    with open(file_path, 'r') as file:
        names = [line.strip() for line in file.readlines()]  # Read each line, strip whitespace, and return as a list
    return names

# Function to generate a random name
def generate_dunmer_name(first_names, last_names):
    first_name = random.choice(first_names)  # Randomly select from first names
    last_name = random.choice(last_names)    # Randomly select from last names
    return f"{first_name} {last_name}"       # Return full name

if __name__ == "__main__":
    print("Welcome to the Dunmer name generator!")

    # Ask if the user wants a settled Dunmer name or an Ashlander name
    while True:
        name_type = input("Do you want a settled Dunmer name or an Ashlander name? (enter 's' for Settled, 'a' for Ashlander): ").strip().lower()
        if name_type in ['s', 'a']:
            break
        else:
            print("Invalid input, please enter 's' for Settled or 'a' for Ashlander.")

    # Load last names based on the name type
    if name_type == 's':
        last_names = load_names_from_file("dunmer_last_names.txt")
    else:
        last_names = load_names_from_file("ashlander_dunmer_last_names.txt")

    # Prompt the user to select a gender and load the corresponding first names
    while True:
        gender = input("Are you male or female? (enter 'm' for male, 'f' for female): ").strip().lower()
        if gender == 'm':
            if name_type == 's':
                first_names = load_names_from_file("dunmer_male_first_names.txt")
            else:
                first_names = load_names_from_file("ashlander_dunmer_male_first_names.txt")
            break
        elif gender == 'f':
            if name_type == 's':
                first_names = load_names_from_file("dunmer_female_first_names.txt")
            else:
                first_names = load_names_from_file("ashlander_dunmer_female_first_names.txt")
            break
        else:
            print("Invalid input, please enter 'm' for male or 'f' for female.")

    # Generate and display the Dunmer or Ashlander name using the loaded first and last names
    generated_name = generate_dunmer_name(first_names, last_names)
    print(f"Your {'Ashlander' if name_type == 'a' else 'Settled Dunmer'} name is {generated_name}.")
