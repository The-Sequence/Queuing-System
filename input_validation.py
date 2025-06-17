# input_validation.py

from patient_node import *
from patient_linkedlist import *

from os import system, name
from title import *


def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def validate_name():
    """Validate a patient's name."""
    while True:
        try:
            patient_name = input("Enter patient name: ").strip()

            if patient_name.lower() == 'q': # Made case-insensitive
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

            if age.lower() == 'q': # Made case-insensitive
                return None

            if age == '' or age.isspace():
                raise ValueError("\nAge cannot be empty")

            if not age.isdigit():
                raise ValueError(f"You have entered: '{age}'. \nAge must be a number")

            age = int(age)

            if age == 0:
                print(f"\nYou have entered: '{age}' \nNotification: Patient age is either unknown, or the patient is an infant.")
                input("Press Enter to continue...")
                return age
            elif age < 0:
                raise ValueError(f"\nYou have entered: '{age}'. \nAge cannot be a negative number")
            elif age > 120:
                raise ValueError(f"\nYou have entered: '{age}' \nAge must be less than or equal to 120")
            else:
                return age
        except ValueError as e:
            print(f"Invalid input for age!"
                  f"\n{e}. Please try again\n")

def validate_sickness():
    """
    Get a patient's sickness.
    Returns a tuple: (sickness, urgency_level)
    urgency_level will be an integer if the sickness is known, otherwise None.
    """
    known_sicknesses = {1: {"Injury", "Burn", "Seizure", "Bleeding", "Stroke"},
                        2: {"Fracture", "High Fever", "Diarrhea", "Vomiting", "Migraine"},
                        3: {"Fever", "Cold", "Flu", "Cough", "Headache"}}
    while True:
        try:
            sickness = input(f"\nEnter Patient's sickness: ")

            if sickness.lower() == 'q': # Made case-insensitive
                return None, None # Return two values to avoid unpack error

            if sickness == '' or sickness.isspace():
                raise ValueError("\nSickness cannot be empty")

            if not all(c.isalpha() or c.isspace() for c in sickness):
                raise ValueError(f"\nYou have entered '{sickness}'. \nError: Sickness cannot contain numbers or symbols")

            sickness = str(sickness).title()

            if len(sickness) < 2:
                raise ValueError(f"\nYou have entered '{sickness}'. \nSickness must be at least 2 characters long")
            
            if sickness == 'Quit':
                raise ValueError(f"\nYou have entered '{sickness}'. \nSickness cannot be 'quit' or 'Quit'")
                
            # *** CHANGED LOGIC START ***
            # Check if sickness is in our known list
            for level, illnesses in known_sicknesses.items():
                if sickness in illnesses:
                    print(f"\nThe sickness '{sickness}' is known and has a pre-assigned urgency level of {level}.")
                    testing = validate_choice(f"\nWould you like to use this urgency level {level} for the sickness '{sickness}'?", mode=1)
                    if testing == 'Yes' or testing == 'Y':
                        return sickness, level  # Return both sickness and its level
                    else:
                         # If the loop completes without finding a match, the sickness is not known.
                        return sickness, None # Return sickness and None for the level
                else:
                    return sickness, None
           

        except ValueError as e:
            print(f"Invalid input for sickness!"
                  f"\n{e}. Please try again\n")


def validate_urgency_level():
    """Validate a patient's urgency level."""
    while True:
        try:
            urgency_level = input(f"\nEnter Patient's urgency level (1-3): ")

            if urgency_level.lower() == 'q': # Made case-insensitive
                return None

            if urgency_level == '' or urgency_level.isspace():
                raise ValueError("\nUrgency level cannot be empty")

            if not urgency_level.isdigit():
                raise ValueError(f"\nYou have entered: '{urgency_level}'.\nUrgency level must be a number")

            urgency_level = int(urgency_level)

            if urgency_level < 1 or urgency_level > 3:
                raise ValueError(f"\nYou have entered: '{urgency_level}'.\nUrgency level must be between 1 and 3")
            else:
                return urgency_level

        except ValueError as e:
            print(f"Invalid input for urgency level!"
                  f"\n{e}. Please try again\n")

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
                        raise ValueError(f"\nYou have entered: '{choice}'. Choice must be a number, not a letter")

                    choice = int(choice)

                    if choice < 1 or choice > 6:
                        raise ValueError(f"\nYou have entered: '{choice}'. Choice must be between 1 and 5")
                    else:
                        return choice


                except ValueError as e:
                    print(f"Invalid input for choice!"
                          f"\n{e}. Please try again\n")

        if mode == 1:
            while True:
                try:
                    choice = input(f"\n{prompt} (Yes/No): ")
                    if choice == '' or choice.isspace():
                        raise ValueError("Choice cannot be empty")
                    if choice.isdigit():
                        raise ValueError(f"\nYou have entered: '{choice}'. \nChoice must be a letter, not a number")
                    choice = choice.strip().title()
                    if choice == "Yes" or choice == 'Y':  # Changed to "YES"
                        return choice
                    elif choice == "No" or choice == 'N':  # Changed to "NO"
                        return choice
                    else:
                        raise ValueError(f"\nYou have entered '{choice}'. \nChoice must be either 'Yes' or 'No'")
                except ValueError as e:
                    print(f"Invalid input for choice!"
                          f"\n{e}. Please try again\n")

def combine_to_dict(name, age, sickness, urgency_level):
    """Combine validated inputs into a dictionary!"""
    # *** IMPLEMENTED THIS FUNCTION ***
    return {
        'name': name,
        'age': age,
        'sickness': sickness,
        'urgency_level': urgency_level
    }

def gather_patient_info():
    """Gather all patient information."""
    # This function's main loop is redundant with the outer one in main.py,
    # but we'll keep it as is and just fix the logic.
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
            return None

        clear_screen()
        choice_1_title()
        print(f"Entering details for Patient: {patient_name}\n"
              f"Patient Age: {patient_age}")
        
        # *** CHANGED LOGIC START ***
        # Capture both returned values from the modified function
        patient_sickness, sickness_urgency_level = validate_sickness()

        if patient_sickness is None: # This now catches the (None, None) return
            return None
        
        clear_screen()
        choice_1_title()
        
        print(f"Entering details for Patient: {patient_name}\n"
              f"Patient Age: {patient_age}\n"
              f"Patient Sickness: {patient_sickness}")
        
        # Only ask for urgency level if it wasn't pre-determined
        if sickness_urgency_level is None:
            sickness_urgency_level = validate_urgency_level()
            if sickness_urgency_level is None: # Check if user cancelled here
                return None
        # *** CHANGED LOGIC END ***

        return combine_to_dict(patient_name, patient_age, patient_sickness, sickness_urgency_level)

    except ValueError as e:
        print(f"An invalid input was detected!"
              f"\n{e}. Please try again\n")
        return None # Return None on error to avoid crashing