students = []

# Ask how many students to enter
while True:
    try:
        count = int(input("How many students? "))
        if count <= 0:
            raise ValueError("Enter a number greater than zero.")
        break
    except Exception as e:
        print("Invalid input:", e)

# Collect student details
for i in range(count):
    print(f"\nStudent {i + 1}")

    while True:
        name = input("Enter student name: ").strip()
        if name:
            break
        print("Name cannot be empty.")

    while True:
        try:
            marks = int(input("Enter marks (0–100): "))

            if not 0 <= marks <= 100:
                raise ValueError("Marks must be between 0 and 100.")

            break
        except Exception as e:
            print("Invalid input:", e)

    # Assign a grade
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    else:
        grade = "F"

    students.append({"name": name, "marks": marks, "grade": grade})

# Display all results
print("\n--- Student Results ---")
print(f"{'Name':<20} {'Marks':<10} Grade")

for student in students:
    print(
        f"{student['name']:<20} "
        f"{student['marks']:<10} "
        f"{student['grade']}"
    )