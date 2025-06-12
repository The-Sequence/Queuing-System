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
        print(f"Patient ' {name} ' has been added to the queue.")

    def service_patient(self):
        if self.is_empty():
            print ("There are no patients in the queue.")
            return
        else:

            current = self.head

            while current:
                print(f"Patient ' {current}'")
                current = current.next

    def display_patients(self):
        if self.is_empty():
            return "No patients in queue"

        result = "Patients in queue:\n"
        current = self.head
        while current:
            result += str(current) + "\n"
            current = current.next
        return result

    def serve_patient(self):
        if self.is_empty():
            print("No patients to serve.")
            return
        else:
            served = self.head
            self.head = self.head.next
            self.size -= 1
            print(f"Serving patient: {served}")

    def count_patients(self):
        return self.size
