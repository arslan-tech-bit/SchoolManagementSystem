import json
from abc import ABC, abstractmethod
from pathlib import Path

database = "school_data.json"
data = {"student_data": [], "teacher_data": []}

if Path(database).exists():
    with open(database, "r") as f:
        content = f.read()
        if content:
            data = {"student_data": [], "teacher_data": []} | json.loads(content)
def save():
    with open(database,"w") as f: # ager file Create nhi hogi toh ye Create kar dega Other wise "w" mode kuch nhi karega
     json.dump(data,f,indent=4)
       # adding the data In the Json data bases
       # or f means File 
       # and Indent shows the Indentation of Output means Output ache se aana chahiye 
class Person(ABC):
    @abstractmethod
    def generate_id(self):
            pass
    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def show_details(self):
        pass
    @abstractmethod
    def search(self):
            pass
    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email


class Student(Person):
    def get_role(self):
        return "Student"
    def generate_id(self):
                pass
    def register(self):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        email = input("Enter your email: ")
        roll_no = input("Enter your roll number: ")
        grade  = {}

        if not Person.validate_email(email):
            print("Invalid email")
            return

        for s in data["student_data"]:
            if s["roll_no"] == roll_no:
                print("Student already exists")
                return

        data["student_data"].append({
            "name": name,
            "age": age,
            "email": email,
            "roll_no": roll_no,
            "grade":{}
        })
        save()
        print("Student registered successfully")

    def show_details(self):
        for s in data["student_data"]:
            print(f"Name: {s['name']}, Age: {s['age']}, Email: {s['email']}, "
                  f"Roll No: {s['roll_no']}, Grades: {s['grade']}")
    def add_grade(self):
        roll_no= input("Enter the roll no")
        subject = input("Enter the subjects")
        marks = float(input("Enter The Marks "))
        for i in data['student_data']:
            if i['roll_no']==roll_no:
                i['grade'][subject] = marks
                save()
                print("Grads Added Sucessfully")
                return
        print("Student is not Found")
    def search(self):
        roll_no = input("Enter  RollNO: ")
        for i in data['student_data']:
            if i['roll_no']==roll_no:
                print("Student  Fount Sucessfully ")
                print("Roll No : ",i['roll_no'])
                print("Name: ",i['name'])
                print("Age: ",i['age'])
                print("Email: ",i['email'])
                print("Greade: ",i['grade'])
            else:
                print("Student Does not Exists")
class Teacher(Person):
    def get_role(self):
            pass
    def register(self):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        email = input("Enter your email: ")
        emp_id = input("Enter your Employee Id: ")
        subject = input("Enter your Subject")

        if not Person.validate_email(email):
            print("Invalid email")
            return

        for t in data["teacher_data"]:
            if t["emp_id"] == emp_id:
                print("Teacher  already exists")
                return

        data["teacher_data"].append({
            "name": name,
            "age": age,
            "email": email,
            "Subject": subject,
            "emp_id": emp_id
        })
        save()
        print("Teacher registered successfully")

    def show_details(self):
          for s in data["teacher_data"]:
            print(f"Name: {s['name']}, Age: {s['age']}, Email: {s['email']}, "
                    f"Employee Id : {s['emp_id']}, subject : {s['subject']}")
    def search(self):
        emp_id = input("Enter  RollNO: ")
        for i in data['teacher_data']:
            if i['emp_id']==emp_id:
             print("Teacher Fount Sucessfully ")
             print("Emp IId : ",i['emp_id'])
             print("Name: ",i['name'])
             print("Age: ",i['age'])
             print("Email: ",i['email'])
             print("Subject: ",i['subject'])
            else:
                print("Teacher Does not Exists ")
    def generate_id(self):
                pass
    
while True:
 print("Press 1 for Student")
 print("Press 2 for Teacher")
 print("Press 3 for add greads")
 print("Press 4 for All student details")
 print("Press 5 for  All teacher details")
 print("Press 6  for Search a Student")
 print("Press 7 for Search a Teacehr")
 choice= int(input("Enter Your Choice"))
 st = Student()
 tr = Teacher()
 if choice==1:
    st.register()
 elif choice==2:
    tr.register()
 elif choice==3:
    st.add_grade()
 elif choice==4:
    st.show_details()
 elif choice==5:
    tr.show_details()
 elif choice==6:
    st.search()
 elif choice==7:
    tr.search()
 elif choice==8:
   print("Visit Again")
   break
 else:
    print("Invalid")
# try:
#     choice = int(input("Enter your choice: "))
# except ValueError:
#     print("Please enter a number")