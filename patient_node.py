class PatientNode:
    def __init__(self, name, age, ailment, urgency_level):
        self.name = name
        self.age = age
        self.ailment = ailment
        self.urgency_level = urgency_level
        self.next = None

    def __str__(self):
        return (f"Patient (Name: {self.name}, Age: {self.age}, "
                f"Ailment: {self.ailment}, Urgency Level: {self.urgency_level})")