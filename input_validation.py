from patient_node import *
from patient_linkedlist import *

from os import system, name
from title import *


def clear_screen():  # Just in case we figure out where to put this function :D
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def validate_name():
    """Validate a patient's name."""
    while True:
        try:
            patient_name = input("Enter patient name: ").strip()

            if patient_name == 'q' or patient_name == 'Q':
                return None

            if patient_name == '' or patient_name.isspace():
                raise ValueError("\nName cannot be empty")

            if not all(c.isalpha() or c.isspace() for c in patient_name):
                raise ValueError("\nName must contain only alphabetic characters and spaces")

            if len(patient_name) < 2 :
                raise ValueError("\nName must be at least 2 characters long")
            else:
                if patient_name.title() == 'Quit':
                    raise ValueError("\nPatient name cannot be 'quit' or 'Quit'")
                else:
                    return str(patient_name).title()

        except ValueError as e:
            print(f"\nInvalid input for patient name!"
                  f"\n{e}. Please try again")

def validate_age():
    """Validate a patient's age."""
    while True:
        try:
            print("Note: Enter '0' if the patient's age is unknown, \nor if the patient is less than a year old.\n")
            age = input("Enter patient age: ").strip()

            if age == 'q' or age == 'Q':
                return None

            if age == '' or age.isspace():
                raise ValueError("\nAge cannot be empty")

            if not age.isdigit():
                raise ValueError("\nAge must be a number")

            age = int(age)

            if age == 0:
                print("\nNotification: Patient age is either unknown, or the patient is an infant.")
                return age
            elif age < 0:
                raise ValueError("\nAge cannot be a negative number")
            elif age > 120:
                raise ValueError("\nAge must be less than or equal to 120")
            else:
                return age
        except ValueError as e:
            print(f"Invalid input for age!"
                  f"\n{e}. Please try again")


def validate_sickness():
    """Get a patient sickness."""
    while True:
        try:
            # Input function just takes whatever the user inputs
            sickness = input(f"\nEnter Patient's sickness: ")

            if sickness == 'q' or sickness == 'Q':
                return None

            # First Condition: Checks whether the input is empty or just spaces,
            # If so, raises a ValueError :D
            if sickness == '' or sickness.isspace():
                raise ValueError("\nSickness cannot be empty")

            if not all(c.isalpha() or c.isspace() for c in sickness):
                clear_screen()
                raise ValueError(f"\nUser entered '{sickness}'. Error: Sickness contains a numerical character")

            sickness = str(sickness).title()

            if len(sickness) < 2:
                clear_screen()
                raise ValueError("\nSickness must be at least 2 characters long")
            else:
                if sickness.title() == 'Quit':
                    raise ValueError("\nSickness cannot be 'quit' or 'Quit'")
                else:
                    return sickness.title()

        except ValueError as e:
            print(f"Invalid input for sickness!"
                  f"\n{e}. Please try again")


def validate_urgency_level():
    """Validate a patient's urgency level."""
    while True:
        try:
            urgency_level = input(f"\nEnter Patient's urgency level: ")

            if urgency_level == 'q' or urgency_level == 'Q':
                return None

            if urgency_level == '' or urgency_level.isspace():
                clear_screen()
                raise ValueError("\nUrgency level cannot be empty")

            if not urgency_level.isdigit():
                clear_screen()
                raise ValueError("\nUrgency level must be a number")

            urgency_level = int(urgency_level)

            if urgency_level < 1 or urgency_level > 3:
                clear_screen()
                raise ValueError("\nUrgency level must be between 1 and 3")
            else:
                return urgency_level

        except ValueError as e:
            print(f"Invalid input for urgency level!"
                  f"\n{e}. Please try again")

def validate_choice(prompt, mode=1):
    """Validate user choice.
    \n mode 0: expects number as input
    \n mode 1: expects yes/no as input"""
    while True:
        if mode == 0:
            while True:
                try:
                    choice = input(f"{prompt}: ")

                    if choice == '' or choice.isspace():
                        raise ValueError("\nChoice cannot be empty")
                    if choice.isalpha():
                        raise ValueError("\nChoice must be a number, not a letter")

                    choice = int(choice)

                    if choice < 1 or choice > 6:
                        raise ValueError("\nChoice must be between 1 and 5")
                    else:
                        return choice


                except ValueError as e:
                    print(f"Invalid input for choice!"
                          f"\n{e}. Please try again")

        if mode == 1:
            while True:
                try:
                    choice = input(f"\n{prompt} (Yes/No): ")
                    if choice == '' or choice.isspace():
                        raise ValueError("Choice cannot be empty")
                    if choice.isdigit():
                        raise ValueError("Choice must be a letter, not a number")
                    choice = choice.strip().upper()
                    if choice == "YES" or choice == 'Y':  # Changed to "YES"
                        return choice
                    elif choice == "NO" or choice == 'N':  # Changed to "NO"
                        return choice
                    else:
                        raise ValueError("Choice must be either 'Yes' or 'No'")
                except ValueError as e:
                    print(f"Invalid input for choice!"
                          f"\n{e}. Please try again")


def combine_to_dict(name, age, sickness, urgency_level):
    """Combine validated inputs into a dictionary!"""

def gather_patient_info():
    """Gather all patient information."""
    while True:
        try:
            clear_screen()
            choice_1_title()
            patient_name = validate_name()

            if patient_name is None:
                return None

            clear_screen()
            choice_1_title()
            print(f"Entering details for Patient: {patient_name}\n")
            patient_age = validate_age()

            if patient_age is None:
                clear_screen()
                return None

            clear_screen()
            choice_1_title()
            print(f"Entering details for Patient: {patient_name}\n"
                  f"Patient Age: {patient_age}")
            patient_sickness = validate_sickness()

            if patient_sickness is None:
                clear_screen()
                return None

            clear_screen()
            choice_1_title()

            print(f"Entering details for Patient: {patient_name}\n"
                  f"Patient Age: {patient_age}\n"
                  f"Patient Sickness: {patient_sickness}")
            sickness_urgency_level = validate_urgency_level()

            if sickness_urgency_level is None:
                clear_screen()
                return None

            return combine_to_dict(patient_name, patient_age, patient_sickness, sickness_urgency_level)

        except ValueError as e:
            print(f"An invalid input was detected!"
                  f"\n{e}. Please try again")
