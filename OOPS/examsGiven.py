class Student:
    exams_Given=[]
    def __init__(self,id):
        self.books=[]
        self.roll_no=id
        self.college="AB"
st1=Student(5)
st2=Student(7)
st1.exams_Given.append("JEE")
st2.exams_Given.append("NEET")
st1.books.append("b")
st2.books.append("a")
print(st1.roll_no)
print(st2.roll_no)
print(st1.exams_Given)
print(st2.exams_Given)
print(st1.college)
print(st2.college)
print(st1.books)
print(st2.books)