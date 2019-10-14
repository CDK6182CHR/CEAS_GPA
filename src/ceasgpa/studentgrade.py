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

    def addGrade(self,grade:Grade):
        self._source.setdefault(grade.course_number,[]).append(grade)
