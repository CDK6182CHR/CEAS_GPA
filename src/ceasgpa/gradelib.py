"""
成绩数据库。先从excel读原始数据，保存格式为：
学号->StudentGrade
"""
from .studentgrade import Grade,StudentGrade
from .studentlist import StudentList,Student
import xlrd,os

class GradeLib(dict):
    def __init__(self,studentList:StudentList):
        super(GradeLib, self).__init__()
        self.studentList = studentList  # type:StudentList

    # 这些数据从0开始
    StudentNumberCol = 0
    CourseNumberCol = 3
    CourseNameCol = 4
    CreditCol = 5
    SemesterCol = 7
    TypeCol = 10
    TotalCol = 14
    StartRow = 0  # 一般来说第0行总是无效的，但有的数据的表头在最后。
    # 对于学号为“学号”出错的，不报错而直接继续
    def readFile(self,filename):
        wb = xlrd.open_workbook(filename)
        ws = wb.sheet_by_index(0)
        for row in range(self.StartRow,ws.nrows):
            stu_num_str = ws.cell_value(row,self.StudentNumberCol)
            if stu_num_str == '学号':
                continue
            try:
                stu_num = int(stu_num_str)
            except ValueError:
                print(f"Invalid student number at file {filename}, "
                      f"row {row}: {stu_num_str}")
                stu_num = 0
            course_number = ws.cell_value(row,self.CourseNumberCol)
            course_name = ws.cell_value(row,self.CourseNameCol)
            credit_str = ws.cell_value(row,self.CreditCol)
            try:
                credit = float(credit_str)
            except ValueError:
                print(f"Invalid credit at file {filename}, "
                      f"row {row}: {credit_str}")
                credit = 0
            semester = ws.cell_value(row,self.SemesterCol)
            course_type = ws.cell_value(row,self.TypeCol)
            total_str = ws.cell_value(row,self.TotalCol)
            if not total_str:
                # 退选成绩为空
                continue
            try:
                total = float(total_str)
            except ValueError:
                print(f"Invalid total at file {filename}, "
                      f"row {row}:{total_str}")
                total = 0
            try:
                self.setdefault(stu_num,
                    StudentGrade(
                    self.studentList.studentByNumber(stu_num))).addGrade(
                    Grade(
                    stu_num,course_number,course_name,credit,semester,
                    course_type,total
                ))
            except KeyError:
                print("Student not in list: ",stu_num)


    def readFileList(self,root='../data/grades'):
        """
        读取root下的每一个.xls文件。
        """
        for a,b,c in os.walk(root):
            for t in c:
                if t.endswith('.xls'):
                    filename = a+'/'+t
                    self.readFile(filename)
