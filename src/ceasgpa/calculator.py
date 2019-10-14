"""
计算器主类
"""
from .courselib import CourseLib
from .gradelib import GradeLib
from .studentlist import StudentList

class GpaCalculator:
    def __init__(self):
        self.courseLib = CourseLib()
        self.courseLib.readJson()
        self.studentList = StudentList()
        self.studentList.readJson()
        self.gradeLib = GradeLib(self.studentList)
        self.gradeLib.readFileList()

    def validate(self):
        """
        筛选和整理数据
        """
        pass

    def calculate(self):
        pass

    def saveExcel(self):
        pass