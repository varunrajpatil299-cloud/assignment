# Base Class
class User:
    def __init__(self, user_id, name, email):
        self.__user_id = user_id
        self.__name = name
        self.__email = email

    def get_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def display_details(self):
        print(f"ID: {self.__user_id}")
        print(f"Name: {self.__name}")
        print(f"Email: {self.__email}")


# Student Class
class Student(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.__course = None

    def enroll_course(self, course_name):
        self.__course = course_name
        print("Course enrolled successfully!")

    # Polymorphism (Method Overriding)
    def display_details(self):
        super().display_details()
        print(f"Course: {self.__course}")
        print("-" * 30)


# Mentor Class
class Mentor(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.__students = []

    def assign_student(self, student):
        self.__students.append(student)
        print("Student assigned to mentor!")

    def display_details(self):
        super().display_details()
        print("Assigned Students:")
        for student in self.__students:
            print("-", student.get_name())
        print("-" * 30)


# Admin Class
class Admin(User):
    def view_students(self, students):
        print("\n--- All Students ---")
        for student in students:
            student.display_details()

    def view_mentors(self, mentors):
        print("\n--- All Mentors ---")
        for mentor in mentors:
            mentor.display_details()


# ---------------- MAIN PROGRAM ---------------- #

students = []
mentors = []

admin = Admin("A1", "Admin", "admin@edtech.com")

while True:
    print("\n===== EdTech Management System =====")
    print("1. Add Student")
    print("2. Add Mentor")
    print("3. Enroll Student in Course")
    print("4. Assign Student to Mentor")
    print("5. View All Students")
    print("6. View All Mentors")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        user_id = input("Enter ID: ")
        name = input("Enter Name: ")
        email = input("Enter Email: ")

        student = Student(user_id, name, email)
        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        user_id = input("Enter ID: ")
        name = input("Enter Name: ")
        email = input("Enter Email: ")

        mentor = Mentor(user_id, name, email)
        mentors.append(mentor)
        print("Mentor added successfully!")

    elif choice == "3":
        if not students:
            print("No students available!")
        else:
            student_id = input("Enter Student ID: ")
            for student in students:
                if student.get_id() == student_id:
                    course = input("Enter Course Name: ")
                    student.enroll_course(course)
                    break
            else:
                print("Student not found!")

    elif choice == "4":
        if not students or not mentors:
            print("Students or Mentors not available!")
        else:
            student_id = input("Enter Student ID: ")
            mentor_id = input("Enter Mentor ID: ")

            selected_student = None
            selected_mentor = None

            for student in students:
                if student.get_id() == student_id:
                    selected_student = student

            for mentor in mentors:
                if mentor.get_id() == mentor_id:
                    selected_mentor = mentor

            if selected_student and selected_mentor:
                selected_mentor.assign_student(selected_student)
            else:
                print("Invalid Student or Mentor ID!")

    elif choice == "5":
        admin.view_students(students)

    elif choice == "6":
        admin.view_mentors(mentors)

    elif choice == "7":
        print("Exiting system...")
        break

    else:
        print("Invalid choice! Try again.")
