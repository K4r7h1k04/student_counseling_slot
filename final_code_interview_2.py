def findCounselling(no_of_slots, no_of_students, slots, students, date):
    # Sort the students based on cutoff marks, age, HSC marks, and SSLC marks in descending order
    students.sort(key=lambda x: (-x[1], -x[2], -x[3], -x[4]))

    # Initialize a dictionary to store the allocated slots
    allocated_slots = {}

    # Iiterate over the slots and allocate seats to the students
    for slot in slots:
        slot_date = slot[0]
        slot_id = slot[1]
        no_of_seats = slot[2]
        if slot_date not in allocated_slots:
            allocated_slots[slot_date] = {}
        allocated_slots_on_date = allocated_slots[slot_date]
        for i in range(1, no_of_seats + 1):
            if len(students) == 0:
                break
            student = students.pop(0)
            student_id = student[0]
            allocated_slots_on_date[student_id] = slot_id

    # Print the details of students who got the slot on the specific date
    if date in allocated_slots:
        allocated_slots_on_date = allocated_slots[date]
        for student in allocated_slots_on_date:
            slot_id = allocated_slots_on_date[student]
            print(f"{date}|{student}|{slot_id}")            
# Get slots
no_of_slots = int(input())
slots = []
for _ in range(no_of_slots):
    date = int(input()) # Slot date
    slot_id = int(input()) # Slot id
    no_of_seats = int(input()) # Number of seats available in the slot
    slot = [date, slot_id, no_of_seats]
    slots.append(slot)
    
# Get students
no_of_students = int(input())
students = []
for _ in range(no_of_students):
    stud_id = int(input()) # Student ID
    cutoff_mark = int(input()) # Student cutoff mark
    age = int(input()) # Student age
    hsc_mark = int(input()) # Student HSC mark
    sslc_mark = int(input()) # Student SSLC mark
    student = [stud_id, cutoff_mark, age, hsc_mark, sslc_mark]
    students.append(student)  
# Get date
date = int(input())

findCounselling(no_of_slots, no_of_students, slots, students, date)