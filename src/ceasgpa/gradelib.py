"""
成绩数据库。先从excel读原始数据，保存格式为：
学号->StudentGrade
"""
from .studentgrade import Grade,StudentGrade
from .studentlist import StudentList,Student
import xlrd,os,openpyxl

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
    Note2Col = 17
    FlagCol = 18

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
            note2 = ws.cell_value(row,self.Note2Col)
            try:
                flag = ws.cell_value(row,self.FlagCol)
            except IndexError:
                flag = ''
            try:
                self.setdefault(stu_num,
                    StudentGrade(
                    self.studentList.studentByNumber(stu_num))).addGrade(
                    Grade(
                    stu_num,course_number,course_name,credit,semester,
                    course_type,total,note2,flag
                ))
            except KeyError:
                print("Student not in list: ",stu_num)
        print(f'Read file {filename}')


    def readFileList(self,root='../data/grades'):
        """
        读取root下的每一个.xls文件。
        """
        for a,b,c in os.walk(root):
            for t in c:
                if t.endswith('.xls') or t.endswith('xlsx'):
                    filename = a+'/'+t
                    self.readFile(filename)

    def writeFIle(self,filename):
        """
        写文件。使得写出的文件能被本程序再次读取。
        """
        wb = openpyxl.Workbook()
        ws = wb.active
        header = (
            '学号','姓名','所属院系','课程编号','课程名称','学分','学时','学期','课程类别','公选类型',
            '成绩类别','平时','期中','期末','总评','对应课程','备注','备注2','标记'
        )
        ws.append(header)
        for num, stu_grade in self.items():
            stu_grade:StudentGrade
            stu = stu_grade.student
            for grade in stu_grade.grades():
                line = (
                    str(num),stu.name,'',grade.course_number,grade.course_name,
                    str(grade.credits),'',grade.semester,'','',grade.grade_type,'','','',
                    grade.total,'',grade.note,grade.note2,grade.flag
                )
                ws.append(line)
        wb.save(filename)
