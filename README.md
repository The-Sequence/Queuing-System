# 🏥 Patient Queuing System  

A console-based patient queuing system built using a singly linked list in Python.  
Developed as a machine project for the subject **DASTRUC** by Group 5 of IT242.

---

## 📌 Features

- Add patients to a priority queue (urgency-based)
- Serve patients based on urgency level (1 is most urgent)
- View all patients in the queue
- Count current number of patients
- Graceful handling of invalid inputs and cancellation
- Clean console interface with custom titles and screens
- Global error handler for safe exit on exception

---

## 🧠 Urgency Levels

Patients are queued based on how urgent their condition is:

| Urgency | Level | Examples                        |
|---------|-------|---------------------------------|
| High    | 1     | Injury, Stroke, Seizure, etc.   |
| Medium  | 2     | Fracture, Vomiting, Migraine    |
| Low     | 3     | Cold, Flu, Headache, etc.       |

---
## 📌 How to use?

### 1️⃣ Add a Patient

- Select option `1`.
- You will be prompted to enter the patient's:
  - Name
  - Age
  - Sickness
- If the sickness is recognized, the system will suggest an urgency level.
- You can accept or manually enter a different urgency level.
- Confirm the patient details to add them to the queue.

🛑 **You can type `Q` at any input prompt to cancel and return to the main menu.**

---

### 2️⃣ Remove / Serve a Patient (Remove a patient from the Queue)

- Select option `2`.
- The system will display the next patient in line (highest urgency).
- Confirm if you want to serve (remove) the patient.
- If confirmed, the patient will be removed from the queue.

---

### 3️⃣ Display Patients

- Select option `3`.
- Shows a list of all patients in the queue, ordered by urgency level.
- Each patient entry includes:
  - Name
  - Age
  - Sickness
  - Urgency level

---

### 4️⃣ Number of Patients

- Select option `4`.
- Displays the current number of patients in the queue.

---

### 5️⃣ Exit

- Select option `5`.
- Exits the program safely.

---

### 🛡️ Input Notes

- Only numbers are allowed for age and urgency level.
- Only letters and spaces are allowed for name and sickness.
- Urgency level must be between 1 (highest) and 3 (lowest).
- Known sicknesses may automatically assign an urgency level.

---

> 📝 **Note:**  
> This program was co-authored with the assistance of AI tools, including **ChatGPT** and **Gemini**, to help with debugging and documentation.

---


