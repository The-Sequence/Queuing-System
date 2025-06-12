from sys import excepthook

from patient_node import *
from patient_linkedlist import *

from os import system, name

def clear_screen():     # Just in case we figure out where to put this function :D
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def validate_name():
    """Validate a patient's name."""
    while True:
        try:
            """Get a patient name."""
            name = input("Enter patient name: ").strip()

            if name == '' or name.isspace():
                raise ValueError("Name cannot be empty")

            if not all(c.isalpha() or c.isspace() for c in name):
                raise ValueError("Name must contain only alphabetic characters and spaces")

            if len(name) < 2:
                raise ValueError("Name must be at least 2 characters long")
            else:
                return str(name).title()
        except ValueError as e:
            print(f"Invalid input for name: {e}. Please try again.")

    return str(name).title()

def validate_age():
    """Validate a patient's age."""
    while True:
        try:
            age = input("Enter patient age: ").strip()

            if age == '' or age.isspace():
                raise ValueError("Age cannot be empty")

            if not age.isdigit():
                raise ValueError("Age must be a number")

            age = int(age)

            if age < 0:
                raise ValueError("Age cannot be a negative number")
            elif age > 120:
                raise ValueError("Age must be less than or equal to 120")
            else:
                return age
        except ValueError as e:
            print(f"Invalid input for age: {e}. Please try again.")

def validate_sickness():
    """Get a patient sickness."""
    while True:
        try:
            # Input function just takes whatever the user inputs
            sickness = input(f"\nEnter Patient's sickness: ")

            # First Condition: Checks whether the input is empty or just spaces,
            # If so, raises a ValueError :D
            if sickness == '' or sickness.isspace():
                raise ValueError("Sickness cannot be empty")

            if not all(c.isalpha() or c.isspace() for c in sickness):
                clear_screen()
                raise ValueError(f"Error: {sickness} contains a numerical character")

            sickness = str(sickness).title()

            if len(sickness) < 2:
                clear_screen()
                raise ValueError("Sickness must be at least 2 characters long")
            else:
                return sickness

        except ValueError as e:
            print(f"Invalid input for sickness: {e}. Please try again")

def validate_urgency_level():
    """Validate a patient's urgency level."""
    while True:
        try:
            urgency_level = input(f"\nEnter Patient's urgency level: ")

            if urgency_level == '' or urgency_level.isspace():
                clear_screen()
                raise ValueError("Urgency level cannot be empty")

            if not urgency_level.isdigit():
                clear_screen()
                raise ValueError("Urgency level must be a number")

            urgency_level = int(urgency_level)

            if urgency_level < 1 or urgency_level > 3:
                clear_screen()
                raise ValueError("Urgency level must be between 1 and 3")
            else:
                return urgency_level

        except ValueError as e:
            print(f"Invalid input for urgency level: {e}. Please try again.")

def combine_to_dict(name, age, sickness, urgency_level):
    """Combine validated inputs into a dictionary!"""
    return {
        'name': name,
        'age': age,
        'sickness': sickness,
        'urgency_level': urgency_level
    }


# def option1_add_patient():
#     # Get name
#     while True:
#                                                                         # Fixed
#         try:
#
#             # Input function just takes whatever the user inputs
#             patient_name = input("\nEnter patient name: ")
#
#             # First Condition: Checks whether the input is empty or just spaces,
#             # If so, raises a ValueError :D
#             if patient_name == '' or patient_name.isspace():
#                 clear_screen()
#                 raise ValueError("Name cannot be empty")
#
#             # If passed First Condition, safely converts the input to a string
#             patient_name = str(patient_name).title()
#
#             # Second Condition: Checks if all characters contain no numbers
#             # If so, raises a ValueError, again.
#             if not all(c.isalpha() or c.isspace() for c in patient_name):
#                 clear_screen()
#                 raise ValueError("Name must contain only alphabetic characters and spaces")
#
#             # Third Condition: Checks if the input contains at least one alphabetic character
#             # If so, raises a ValueError, again :P
#             if len(patient_name) < 2:
#                 clear_screen()
#                 raise ValueError("Name must be at least 2 characters long")
#
#             # If all conditions are passed, the name is valid
#             else:
#                 clear_screen()
#                 print(f"Please enter a few more details for patient {patient_name}.")
#                 break
#         # Default ValueError thing if a user inputs something wild that I didn't anticipate xD
#         except ValueError as e:
#             clear_screen()
#             print(f"Invalid input for name: {e}. Please try again.")
#
#     while True:
#         # Get age                                                                                   #Fixed
#         try:
#             print(f"Patient Name: {patient_name}\n")
#
#             # Input function just takes whatever the user inputs
#             print(f"Note: If patient {patient_name}'s age is not known, or is less than a year old, please enter 0.")
#             age = input(f"Enter Patient {patient_name}'s age: ")
#
#             # First Condition: Checks whether the input is empty or just spaces,
#             # If so, raises a ValueError :D
#             if age == '' or age.isspace():
#                 clear_screen()
#                 raise ValueError("Age cannot be empty")
#
#             # Second Condition: Checks whether the input is an integer,
#             # If it isn't, raises a ValueError :D
#             elif not age.isdigit():
#                 clear_screen()
#                 raise ValueError("Age must be a number")
#
#             # If passed both conditions, safely converts the input to an integer
#             age = int(age)
#
#             # Third Condition: Checks if the age is a negative number or greater than 120
#
#             if age < 0:
#                 clear_screen()
#                 raise ValueError("Age cannot be a negative number")
#             elif age > 120:
#                 clear_screen()
#                 raise ValueError("Age must be less than or equal to 120")
#             else:
#                 if age == 0:
#                     print(f"\nNotification: Patient {patient_name}'s age has been set to 0, indicating unknown or less than a year old")
#                     print(f"Patient {patient_name}'s age has been set to {age}")
#                     break
#                 else:
#                     clear_screen()
#                     print(f"Patient {patient_name}'s age has been set to {age}")
#                 break
#
#         except ValueError as e:
#             print(f"Invalid input for age: {e}. Please try again.")
#
#     while True:
#         # Get sickness                                                                                  #To fix
#         try:
#             print(f"Patient Name: {patient_name}\n"
#                   f"Patient Age: {age}\n")
#
#             # Input function just takes whatever the user inputs
#             sickness = input(f"\nEnter Patient {patient_name}'s sickness: ")
#
#             # First Condition: Checks whether the input is empty or just spaces,
#             # If so, raises a ValueError :D
#             if sickness == '' or sickness.isspace():
#                 raise ValueError("Sickness cannot be empty")
#
#             if not all(c.isalpha() or c.isspace() for c in sickness):
#                 clear_screen()
#                 raise ValueError(f"Error: {sickness} contains a numerical character")
#
#             sickness = str(sickness).title()
#
#             if len(sickness) < 2:
#                 clear_screen()
#                 raise ValueError("Sickness must be at least 2 characters long")
#             else:
#                 print(f"DEBUGGING: Sickness: {sickness} is valid.")
#                 break
#
#         except ValueError as e:
#             print(f"Invalid input for sickness: {e}. Please try again")
#
#     while True:
#         try:
#             print(f"Patient Name: {patient_name}\n"
#                   f"Patient Age: {age}\n"
#                   f"Patient Sickness: {sickness}\n")
#             urgency_level = input(f"\nEnter Patient {patient_name}'s {sickness} urgency level: ")
#
#             if urgency_level == '' or urgency_level.isspace():
#                 clear_screen()
#                 raise ValueError("Urgency level cannot be empty")
#
#             if not urgency_level.isdigit():
#                 clear_screen()
#                 raise ValueError("Urgency level must be a number")
#
#             urgency_level = int(urgency_level)
#
#             if urgency_level < 1 or urgency_level > 5:
#                 clear_screen()
#                 raise ValueError("Urgency level must be between 1 and 5")
#             else:
#                 print(f"Urgency Level: {urgency_level} is valid")
#                 break
#
#         except ValueError as e:
#             print(f"Invalid input for urgency level: {e}. Please try again.")
#
#     return {
#         'name': patient_name,
#         'age': age,
#         'sickness': sickness,
#         'urgency_level': urgency_level
#     }