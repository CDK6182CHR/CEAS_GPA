"""
一个学生一门课的成绩。
与表中的记录构成一一映射。
只保存学号，不进行姓名检查！
"""

class Grade:
    def __init__(self,stu_number,course_number,course_name,credits,
                 semester,grade_type,total):
        self.stu_number = stu_number  # type:int
        self.course_number = course_number  # type:str
        self.course_name = course_name  # type:str
        self.credits = credits  # type:float
        self.semester = semester  # type:str
        self.grade_type = grade_type  # type:str
        self.total = total  # type:float
