from subject import Subject

class Marks(Subject):
    def __init__ (self,subName, subCode, credHr, quiz, assignment, test, project, finalExam):
        self.subName = subName
        self.subCode = subCode
        self.credHr = credHr
        self.quiz = quiz
        self.assignment = assignment
        self.test = test
        self.project = project
        self.finalExam = finalExam

    def getMarks(self):
        print("Quiz: " + str(self.quiz) + "\n")
        print("Assignment: " + str(self.assignment) + "\n")
        print("Test: " + str(self.test) + "\n")
        print("Project: " + str(self.project) + "\n")
        print("Final Exam: " + str(self.finalExam) + "\n")

    def getGrade(self,totalPr):
        if totalPr >=80 and totalPr <=100:
            grade = 'A'
            points = 4
            category = 'Excellent'
        elif totalPr >=60 and totalPr <80:
            grade = 'B'
            points = 3
            category = 'Pass'
        elif totalPr >=40 and totalPr <60:
            grade = 'C'
            points = 2
            category = 'Pass'
        else:
            grade = 'F'
            points = 0
            category = 'Fail'

        result = dict()
        result['grade'] = grade
        result['points'] = points
        result['category'] = category
        return result
        

        
