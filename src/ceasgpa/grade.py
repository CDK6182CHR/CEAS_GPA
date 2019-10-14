"""
一个学生一门课的成绩。
与表中的记录构成一一映射。
只保存学号，不进行姓名检查！
"""

class Grade:
    def __init__(self,stu_number,course_number,course_name,credits,
                 semester,grade_type,total,note2,flag):
        self.stu_number = stu_number  # type:int
        self.course_number = course_number  # type:str
        self.course_name = course_name  # type:str
        self.credits = credits  # type:float
        self.semester = semester  # type:str
        self.grade_type = grade_type  # type:str
        self.total = total  # type:float
        self.note2 = note2  # type:str
        self.flag = flag

    def __str__(self):
        return f"{self.stu_number} {self.course_number} {self.course_name} " \
               f"{self.semester} {self.total} {self.note2} {self.flag}"

    def __eq__(self, other):
        if isinstance(other,Grade):
            return self.stu_number == other.stu_number and \
                    self.course_number == other.course_number and \
                self.course_name == other.course_name and \
                self.credits == other.credits and \
                self.semester == other.semester and \
                self.grade_type == other.grade_type and \
                self.total == other.total and \
                self.note2 == other.note2 and \
                self.flag == other.flag
        return False
