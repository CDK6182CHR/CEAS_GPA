"""
学生信息基本类
"""
class Student:
    def __init__(self,name,number,major):
        self.name = name   # type:str
        self.number = int(number) # type:int
        self.major = major  # type:str

    def __hash__(self):
        return hash(self.number)

    def __str__(self):
        return f"{self.number} {self.name} {self.major}"

    def __eq__(self, other):
        return self.numer == other.number
