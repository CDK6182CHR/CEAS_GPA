"""
一个学生的所有成绩。以学号为唯一的标识符，不做姓名检查。
读取时保存在list中，在计算系统中再做规范化。
访问方法封装。
"""
from .grade import Grade
from .student import Student
from typing import Union,Dict,List

class StudentGrade:
    def __init__(self,student:Student):
        self.student = student  # type:Student
        self._source = {}  # type:Dict[str,List[Grade]]
        self._table = {}  # type:Dict[str,Grade]
        self._ok = False
        self.gpa = 0  # type: float
        self.absentCount = 0  # type:int  # 缺课门数
        self.absentNames = []

    def addGrade(self,grade:Grade)->Grade:
        cur = self._source.setdefault(grade.course_number,[])
        if grade not in cur:
            cur.append(grade)

    def calculate(self)->float:
        if not self._ok:
            print("Not ready yet!")
            return 0
        totalGrades,totalCredits = 0,0
        for course_id,grade in self._table.items():
            totalCredits+=grade.credits
            totalGrades+=grade.total*grade.credits
        if totalCredits == 0:
            print("totalCredits==0!")
            return 0
        self.gpa = totalGrades/totalCredits/20
        return self.gpa

    def getCourseGrade(self,course_id:str):
        grade = self._table.get(course_id,None)
        if grade is None:  # 缺课返回空格
            return ''
        return grade.total

    def getCourseGradeObject(self,course_id:str)->Grade:
        return self._table.get(course_id,None)
