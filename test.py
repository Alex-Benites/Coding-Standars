class student:
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        self.grades = []
        self.is_passed = "NO"
        self.honor = "?"

    def addGrades(self, g):
        self.grades.append(g)

    def calcaverage(self):
        if len(self.grades) == 0:
            return 0
        t = 0
        for x in self.grades:
            t += x
        avg = t / len(self.grades)
        return avg

    def checkHonor(self):
        if self.calcAverage() > 90:
            self.honor = "yep"

    def deleteGrade(self, index):
        del self.grades[index]

    def report(self):  # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.grades))
        print("Final Grade = " + self.letter)


def startrun():
    a = student("x", "")
    a.addGrades(100)
    a.addGrades("Fifty")  # broken
    a.calcaverage()
    a.checkHonor()
    a.deleteGrade(5)  # IndexError
    a.report()


startrun()
