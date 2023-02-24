from student import Student
from marks import Marks

#INPUT STUDENT
print("INPUT STUDENT DETAILS")
print("------------------------------------------------")
name = input("Student Name : ")
id = input("Student ID   : ")
programme = input("Programme    : ")
print("------------------------------------------------")
student = Student(name,id,programme)

#INPUT SUBJECT
print("\nINPUT SUBJECT DETAILS")
print("------------------------------------------------")
subName = input("Subject Name : ")
subCode = input("Subject Code : ")
credHr = int(input("Credit Hour  : "))
print("------------------------------------------------\n")

#INPUT MARKS
while True:
    try:
        print("Input the marks for...")
        quiz = float(input("Quiz (out of 20)        : "))
        assignment = float(input("Assignment (out of 20)  : "))
        test = float(input("Test (out of 30)        : "))
        project = float(input("Project (out of 30)     : "))
        finalExam = float(input("Final Exam (out of 100) : "))

        if quiz<=20 and assignment<=20 and test <=30 and project<=30 and finalExam<=100:
            break
        else:
            print("\n---------------------------------")
            print("Error: Some marks exceed the maximum value.")
            print("Please try again !")
            print("---------------------------------\n")
    except :
        print("Please input numeric value only")
print("------------------------------------------------\n")
subject = Marks(subName,subCode,credHr,quiz,assignment,test,project,finalExam)

#CALCULATE MARKS PERCENTAGE
prQuiz = (quiz / 20)*10
prAssg = (assignment / 20)*10
prTest = (test / 30)*20
prProj = (project / 30)*20
totalCoursework = prQuiz + prAssg + prTest + prProj
prFinal = (finalExam / 100) * 40
totalPr = totalCoursework + prFinal
result = subject.getGrade(totalPr)


#CALCULATE POINTS AND GPA
totalPoints = float(result['points']) * float(subject.credHr)
gpa = totalPoints / float(subject.credHr)

#RESULT
print("--------------------------------------------------------------------------")
print("                         UNIVERSITI KUALA LUMPUR                          ")
print("               MALAYSIAN INSTITUTE OF INFORMATION TECHNOLOGY              ")
print("                1016 JALAN SULTAN ISMAIL 50250 KUALA LUMPUR               ")
print("--------------------------------------------------------------------------")
print("                   Result Slip Semester September 2020                    ")
print("Name         : " + student.name)
print("Student ID  : " + student.id )
print("Programme   : " + student.programme)
print("__________________________________________________________________________")
print("Subject Code: " + str(subject.subCode))
print("Subject Name: " + str(subject.subName))
print("Credit Hour: " + str(subject.credHr) + "   |   Point: " + str(result["points"]))
print("--------------------------------------------------------------------------")
print("     GPA: " + str(gpa) + "   |   Category: " + str(result["category"]) + "   |   Grade: " + str(result["grade"]))
print("__________________________________________________________________________")
print("ACCUMULATED MARKS FOR " + subject.subCode)
print("Quiz         : " + str(round(subject.quiz,2)) + "/20")
print("Assignment   : " + str(round(subject.assignment,2))+ "/20")
print("Test         : " + str(round(subject.test,2))+ "/30")
print("Project      : " + str(round(subject.project,2))+ "/30")
print("Final Exam   : " + str(round(subject.finalExam,2))+ "/100")
print("--------------------------------------------------------------------------")
print("Total Marks  : " + str(round(totalPr,2)) + "%")
print("--------------------------------------------------------------------------")
print("__________________________________________________________________________")