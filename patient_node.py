class PatientNode:
    def __init__(self, name, age, sickness, urgency_level):
        self.name = name
        self.age = age
        self.sickness = sickness
        self.urgency_level = urgency_level
        self.next = None

    def __str__(self):
        return (f"Name: {self.name}, Age: {self.age}, "
                f"Sickness: {self.sickness}, Urgency Level: {self.urgency_level}")