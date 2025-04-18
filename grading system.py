class GradingSystem:
    def __init__(self):
        self.students = {}

    def add_grade(self, student_name, grade):
        if student_name in self.students:
            print(f"Grade for {student_name} is already added. Updating grade to {grade}.")
        else:
            print(f"Grade for {student_name} added.")
        self.students[student_name] = grade

    def view_grades(self):
        if not self.students:
            print("No student grades available.")
        else:
            print("\n---- Student Grades ----")
            for student, grade in self.students.items():
                print(f"{student}: {grade}")

    def calculate_average(self):
        if self.students:
            average_grade = sum(self.students.values()) / len(self.students)
            print(f"The average grade of the class is: {average_grade:.2f}")
        else:
            print("No grades available to calculate the average.")

    def find_highest_lowest(self):
        if self.students:
            highest_grade = max(self.students.values())
            lowest_grade = min(self.students.values())
            highest_student = [student for student, grade in self.students.items() if grade == highest_grade]
            lowest_student = [student for student, grade in self.students.items() if grade == lowest_grade]
            print(f"Highest grade: {highest_grade}, achieved by {', '.join(highest_student)}.")
            print(f"Lowest grade: {lowest_grade}, achieved by {', '.join(lowest_student)}.")
        else:
            print("No grades available to find highest or lowest.")

def menu():
    grading_system = GradingSystem()

    while True:
        print("\n---- Student Grading System ----")
        print("1. Add a student's grade")
        print("2. View all student grades")
        print("3. Calculate the average grade of the class")
        print("4. Find the highest and lowest grade")
        print("5. Exit")

        try:
            choice = int(input("Choose an option (1-5): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            student_name = input("Enter student name: ")
            try:
                grade = float(input(f"Enter grade for {student_name}: "))
                if 0 <= grade <= 100:
                    grading_system.add_grade(student_name, grade)
                else:
                    print("Invalid grade! Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a valid grade.")

        elif choice == 2:
            grading_system.view_grades()

        elif choice == 3:
            grading_system.calculate_average()

        elif choice == 4:
            grading_system.find_highest_lowest()

        elif choice == 5:
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid option! Please choose a number between 1 and 5.")

# Running the menu
menu()
