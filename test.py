"""
This module defines the Student class and demonstrates its functionality.
It includes methods for managing grades, calculating averages, and generating reports.
"""

class Student:
    """
    Represents a student with an ID, name, grades, and other attributes.
    Provides methods to manage grades and calculate averages.
    """
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        self.grades = []
        self.is_passed = "NO"
        self.honor = "?"

    def add_grades(self, grade):
        """
        Adds a grade to the student's list of grades.

        Args:
            grade (int): The grade to add.
        """
        self.grades.append(grade)

    def calc_average(self):

        """
        Calculates the average of the student's grades.

        Returns:
            float: The average grade, or 0 if there are no grades.
        """

        if len(self.grades) == 0:
            return 0
        total = 0
        for grade in self.grades:
            total += grade
        avg = total / len(self.grades)
        return avg

    def check_honor(self):

        """
        Checks if the student's average grade is above 90.
        If so, sets the honor attribute to 'yep'.
        """
        if self.calc_average() > 90:
            self.honor = "yep"

    def delete_grade(self, index):

        """
        Deletes a grade from the student's list of grades by index.

        Args:
            index (int): The index of the grade to delete.

        Raises:
            IndexError: If the index is out of range.
        """


        if 0 <= index < len(self.grades):
            del self.grades[index]
        else:
            print("Invalid index")

    def report(self):

        """
        Prints a report of the student's details, including ID, name,
        number of grades, and average grade.
        """

        print("ID: " + str(self.id))
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.grades)))
        print("Average Grade: " + str(self.calc_average()))


def start_run():
    """
    Demonstrates the functionality of the Student class by creating
    a student, adding grades, calculating averages, and printing a report.
    """

    a = Student("x", "")
    a.add_grades(100)
    a.add_grades(50)  # broken
    a.calc_average()
    a.check_honor()
    a.delete_grade(0)  # IndexError
    a.report()


start_run()
