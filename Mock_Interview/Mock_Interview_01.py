while True:
    print("\n--- Student Management Menu ---")
    print("1. Add Student")
    print("2. View Student by Roll No")
    print("3. Modify Student Details")
    print("4. Delete Student by Roll No")
    print("5. Exit")

    choice = input("Enter your choice (1-6): ")
    students = []
    if choice == '1':
        students = []
        n = int(input("How many students do you want to enter? "))

        for i in range(n):
            print(f"\nEnter details for student {i + 1}:")
            student = {'name': input("Name : "), 'Roll_no': int(input("Roll_no : ")), 'age': input("Age : "),
                       'Course': (input('Course : '),)}

            marks = {'English': int(input("Enter English Marks : ")), 'Maths': int(input("Enter Maths Marks : ")),
                     'Science': int(input("Enter Science Marks : "))}

            student['Marks'] = marks
            avg = round((marks['English'] + marks['Maths'] + marks['Science']) / 3)
            student['Average_marks'] = avg
            if avg >= 90:
                Grade = "A+"
            elif avg >= 75:
                Grade = "A"
            elif avg >= 60:
                Grade = "B"
            elif avg >= 40:
                Grade = "C"
            else:
                Grade = "Fail"
            student['Grade'] = Grade
            students.append(student)
            x = 1
            for s in students:
                print(f"Student {x} :\n {s}")
                x += 1
        pass

    elif choice == '2':
        print("\nSEARCH STUDENT BY ROLL NO :")
        roll = int(input("Enter roll no: "))
        found = False
        target_student = None

        for student in students:
            if roll == student['Roll_no']:
                print("\nStudent Found:")
                for key, value in student.items():
                    print(f"{key.capitalize()}: {value}")
                found = True
                target_student = student
                break

        if not found:
            print("No student found with that roll number.")
        pass

    elif choice == '3':
        target_student = 0
        print("\nMODIFY STUDENT DETAILS :")
        print("\nWhat would you like to modify?")
        print("1. Name\n2. Age\n3. Course")
        choice = input("Enter choice (1-3): ")

        if choice == '1':
            target_student['name'] = input("Enter new name: ")
        elif choice == '2':
            target_student['age'] = int(input("Enter new age: "))
        elif choice == '3':
            target_student['course'] = (input("Enter new course: "),)
        else:
            print("Invalid choice.")

        print("\nUPDATED STUDENT DETAILS :")
        for key, value in target_student.items():
            print(f"{key.capitalize()}: {value}")
        pass

    elif choice == '4':
        print("\nREMOVE STUDENT RECORDS")
        roll = int(input("Enter roll number to remove: "))
        found = False

        for student in students:
            if student['Roll_no'] == roll:
                students.remove(student)
                found = True
                print(f"\nStudent with Roll No {roll} has been removed.")
                break

        if not found:
            print("No student found with that roll number.")
        pass

    elif choice == '5':
        print("\nThank you for using the Student Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
