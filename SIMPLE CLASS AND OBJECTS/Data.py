class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def printdata(self):
        print("NAME = " + self.name)
        print("AGE = " + self.age)
        print("GENDER = " + self.gender)
        
name = input("Enter Your Name : ")
age  = input("Enter Your Age : ")
gender = input("Enter Your Gender : ")
    
s1 = Student(name,age,gender)
s1.printdata();
    