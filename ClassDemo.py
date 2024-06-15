'''
Main OOP Concept

1. Class
    - It is a group of different type of data and function.

2. Object
    -It is an instance of class.

3. Inheritance
    -The object of one class can aquire the properties of object of another
    class is called inheritance.
    -Creating a new class from an existing class is called inheritance.
    1. Single
    2. Multilevel
    3. Multiple
    4. Hierarchical
    5. Hybrid

4. Polymorphism - One name multiple form :
    1.Compile Time Polymorphism - (Method Overloading) - When there is a more
    than one method in a single class having same name but with different number
    of arguments then it is called method overloading.
    2. Run Time Polymorphism - (Method Overriding) - When there is a same
    method prototype in your both base class & derived class & if you call that method
    using the object of derived class, then only derived class method will be called.
    So you can say that method of derived class override method of base class.


5. Abstraction - Data hiding

6. Encapsulation - To bind a data and code into a single unit is called encapsulation.

'''


class Student:
    def getData(self,fname,lname):
        print("getdata Called")
        self.f=fname
        self.l=lname
    def putData(self):
        print("putData Called")
        print("First Name : ",self.f)
        print("Last Name : ",self.l)
s1=Student()
s1.getData("Akshay","Nagar")
s1.putData()













    
