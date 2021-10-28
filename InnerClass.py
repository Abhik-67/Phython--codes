class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name , self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand ='DELL'   
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)        

s1 = Student('ABHIK',1000)
s2 = Student('DEBRAJ',1001)        

s1.show()
s2.show()
lap1 = Student.Laptop()


'''
OUTPUT:
ABHIK 1000
DELL i5 8
DEBRAJ 1001
DELL i5 8
'''