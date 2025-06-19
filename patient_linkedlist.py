# patient_linked_list.py

from patient_node import *

class PatientLinkedList:
    def __init__ (self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def add_patient(self, patient_dict):
        name = patient_dict['name']
        age = patient_dict['age']
        sickness = patient_dict['sickness']
        urgency_level = patient_dict['urgency_level']

        new_node = PatientNode(name, age, sickness, urgency_level)

        if self.is_empty() or urgency_level < self.head.urgency_level:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and urgency_level >= current.next.urgency_level:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1

    def display_patients(self):
        if self.is_empty():
            return "No patients in queue"

        result = "Patients in queue:\n"
        current = self.head
        count = 1
        while current:
            result += f"{count}. {str(current)}\n"
            current = current.next
            count += 1
        return result

    def peek_patient(self, mode=0):
        """Returns the name of the patient at the front of the queue\n.
        If mode is 0, returns the first name of the patient\n
        If mode is 1, returns detailed information of the patient\n"""

        if self.is_empty():
            return None # Return None, let the caller handle printing
        else:
            if mode == 0:
                return self.head.name
            elif mode == 1:
                return (f"\nName:               {self.head.name}"
                        f"\nAge:                {self.head.age}"
                        f"\nSickness:           {self.head.sickness}"
                        f"\nUrgency Level:      {self.head.urgency_level}")
            else:
                return self.head

    def serve_patient(self):
        """Removes the patient at the front of the queue."""
        if self.is_empty():
            return None # Return None if nothing to serve

        served_patient_name = self.head.name
        self.head = self.head.next
        self.size -= 1
        return served_patient_name # Return the name of who was served

    def count_patients(self):
        return self.size