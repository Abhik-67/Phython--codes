class Student:

    collage = 'MEGHNAD SAHA INSTITUTE OF TECHNOLOGY'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return(self.m1 + self.m2 + self.m3)/3  

    def get_m1(self):           #Instance Methods type1 - Accessor Methods (For Fetching value)
        return self.m1

    def set_m1(self,value):     #Instance Methods type2 - Mutator Methods (For Modifying value)
        self.m1=value  
    
    @classmethod                #classmethod
    def getcollage(cls):
        return cls.collage

    @staticmethod               #staticmethod
    def info():
        print("WELCOME TO THE ELECTRICAL ENGINEERING DEPARTMENT OF MEGHNAD SAHA INSTITUTE OF TECHNOLOGY.")    
    
s1 = Student (99,99,99)
s2 = Student (80,70,99)

print(Student.getcollage())     # MEGHNAD SAHA INSTITUTE OF TECHNOLOGY
print(s1.avg())                 # 99.0
print(s2.avg())                 # 83.0
Student.info()     # WELCOME TO THE ELECTRICAL ENGINEERING DEPARTMENT OF MEGHNAD SAHA INSTITUTE OF TECHNOLOGY.

 