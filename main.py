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

from input_validation import *

patient_list = PatientLinkedList()

while True:
    print("***** Queuing System Menu *****\n"
          "1. Add a patient\n"
          "2. Remove a patient\n"
          "3. Display patients in queue\n"
          "4. Number of patients in queue\n"
          "Q. Exit\n")

    choice = input("Please enter your choice: ").strip().upper()

    if choice == '1':
        print("***** Queuing System - Add a Patient *****\n")
        patient_name = validate_name()

        if patient_name is None: # Returns to the menu as soon as the user enters 'q' or 'Q'
            continue
        patient_age = validate_age() # Returns to the menu as soon as the user enters 'q' or 'Q'

        if patient_age is None:
            continue
        patient_sickness = validate_sickness() # Returns to the menu as soon as the user enters 'q' or 'Q'

        if patient_sickness is None:
            continue
        sickness_urgency_level = validate_urgency_level() # Returns to the menu as soon as the user enters 'q' or 'Q'

        if sickness_urgency_level is None:
            continue

        patient_info = combine_to_dict(patient_name, patient_age, patient_sickness, sickness_urgency_level)
        patient_list.add_patient(patient_info)

        print(f"Patient {patient_name} added successfully.")

        input("Press Enter to continue...")

    elif choice == '2':
        print("***** Queuing System - Serve a Patient *****\n")
        # Code to remove a patient

        print(f"The patient next on queue is: {patient_list.peek_patient(mode=1)}")
        choice = validate_choice("Would you like to serve this patient? ")

        if choice is None:
            print("Returning to menu...")
            input("Press Enter to continue...")
            continue

        elif choice == 'Y':
            patient_list.serve_patient()
            print(f"Patient {patient_list.peek_patient(mode=0)} has been served and removed from the queue.")
            input("Press Enter to continue...")

        elif choice == 'N':
            print("Returning to menu...")
            input("Press Enter to continue...")
            continue
        else:
            continue


    elif choice == '3':
        print("***** Queuing System - Display Patient List *****\n")
        # Code to display patients

        #Note: Not actual implementation
        print(patient_list.display_patients())
        input("Press Enter to continue...")

    elif choice == '4':
        print("***** Queuing System - Number of Patients in Queue *****\n")
        # Code to count patients

        #Note: Not actual implementation
        print(f"Number of patients in queue: {patient_list.size}")
        input("Press Enter to continue...")

    elif choice == 'Q':
        print("Exiting the system. Goodbye!")
        exit(0)

    else:
        raise ValueError("Invalid choice. Please try again.")
