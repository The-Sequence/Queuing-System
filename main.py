"""
Group 5 - Queuing System (Linked List Implementation)
A Machine Project submitted in partial fulfillment of the 3rd Term Requirement for the subject DASTRUC

Presented by the following students of IT242:
1.
2.
3.

Submitted to: Mr. Renan Bacit
Date: June 13, 2025 (Friday)

"""

import sys
import traceback

def show_error_and_exit(exc_type, exc_value, exc_traceback):
    """Display error information and wait for user input before exiting."""
    print("An error occurred:")
    traceback.print_exception(exc_type, exc_value, exc_traceback)
    input("Press Enter to exit...")
    sys.__excepthook__(exc_type, exc_value, exc_traceback)

# Set up global exception handler
sys.excepthook = show_error_and_exit

from input_validation import *
from title import *

def main():
    patient_list = PatientLinkedList()

    while True:
        clear_screen()
        print("***** Queuing System Menu *****\n"
              "1. Add a patient\n"
              "2. Remove a patient\n"
              "3. Display patients in queue\n"
              "4. Number of patients in queue\n"
              "5. Exit\n")

        choice = validate_choice("Please enter your choice", mode=0)

        if choice == 1:
            patient_info = gather_patient_info()

            if patient_info is None:
                clear_screen()
                continue

            clear_screen()
            choice_1_title()
            print(f"Please confirm the following patient information:\n"
                  f"Name:               {patient_info['name']}\n"
                  f"Age:                {patient_info['age']}\n"
                  f"Sickness:           {patient_info['sickness']}\n"
                  f"Urgency Level:      {patient_info['urgency_level']}\n")

            choice = validate_choice("Would you like to add this patient?")
            if choice is None or choice == 'No' or choice == 'N':
                clear_screen()
                choice_1_title()
                print("Patient information discarded.\n")
                input("Press any key to return to the menu...")
                continue

            elif choice == 'Yes' or choice == 'Y':
                clear_screen()
                choice_1_title()
                patient_list.add_patient(patient_info)
                print(f"Patient {patient_info['name']} has been added to the queue.")
                input("Press any key to return to the menu...")

            else:
                continue

        elif choice == 2:
            clear_screen()
            choice_2_title()

            if patient_list.is_empty():
                print("There are no patients in the queue.")
                input("Press any key to return to the menu...")
                continue
            else:
                print(f"The patient next on queue is: {patient_list.peek_patient(mode=1)}")
                choice = validate_choice(f"\nWould you like to serve patient {patient_list.peek_patient()}", mode=1)

            if choice is None or choice == 'No' or choice == 'N':
                print("Returning to menu...")
                input("Press any key to return to the menu...")
                continue

            elif choice == 'Yes' or choice == 'Y':
                print(f"Patient {patient_list.peek_patient(mode=0)} has been served and is removed from the queue.")
                patient_list.serve_patient()
                input("Press any key to return to the menu...")

            else:
                continue


        elif choice == 3:
            clear_screen()
            choice_3_title()
            # Code to display patients

            # Note: Not actual implementation
            print(patient_list.display_patients())
            input("Press Enter to continue...")

        elif choice == 4:
            clear_screen()
            choice_4_title()
            # Code to count patients

            # Note: Not actual implementation
            if patient_list.is_empty():
                print("There are no patients in the queue.")
            else:
                print(f"Number of patients in queue: {patient_list.size}")
            input("Press Enter to continue...")

        elif choice == 5:
            clear_screen()
            choice_5_title()
            print("Exiting the system. Goodbye!")
            input("Press Enter to exit...")
            exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Set up global exception handler
    sys.excepthook = show_error_and_exit
    main()