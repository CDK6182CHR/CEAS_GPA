"""
课程类。包含课程名，课程号，以及对各专业的课程性质。
"""
from typing import Dict,Union


class Course:
    Types = {
        0b10:'A类-本专业升学',
        0b01:'C类-就业创业',
    }
    BriefTypes = {
        0b10:'A',
        0b01:'C',
    }
    def __init__(self,name,id,semester,credits,majorTypes=None):
        self.name = name  # type:str
        self.id = id  # type:str
        self.semester = semester  # type:int
        self.credits = credits  # type:int
        if majorTypes is None:
            majorTypes={}
        self.majorTypes = majorTypes  # type:Dict[str,int]

    def addMajor(self,majorName:str,tp:int):
        self.majorTypes[majorName]=tp

    def getMajorType(self,majorName,default=0b00):
        return self.majorTypes.get(majorName,default)

    def __str__(self):
        return f"{self.id} {self.name} {self.credits}学分"
