"""
计算器主类
"""
from .courselib import CourseLib
from .gradelib import GradeLib,StudentGrade
from .studentlist import StudentList
from .validator import GradeValidator
import openpyxl
from datetime import datetime

class GpaCalculator:
    def __init__(self,mode,start,end,useSubstitute,useFirst,firstYear,zeroForAbsent,precision):
        self.courseLib = CourseLib()
        self.courseLib.readLibFile()
        self.studentList = StudentList()
        self.studentList.readJson()
        self.gradeLib = GradeLib(self.studentList)
        self.gradeLib.readFileList()
        self.precision = 3
        self.mode = mode
        self.start = start
        self.end = end
        self.validator = GradeValidator(self.gradeLib,self.courseLib,
                                        mode,start,end,useSubstitute,useFirst,firstYear,zeroForAbsent)

    def validate(self):
        """
        筛选和整理数据
        """
        self.validator.validate()

    def calculate(self):
        for stu_number,stu_grade in self.gradeLib.items():
            print(stu_grade.student,stu_grade.calculate())

    def saveExcel(self,filename='../data/output.xlsx'):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = '概览'
        ws.append(['导出时间：'+datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
        header = ['学号','姓名','专业','学分绩','缺课门数','缺课表']
        ws.append(header)
        stu_grades = list(self.gradeLib.values())
        stu_grades.sort(key=lambda x:x.gpa,reverse=True)
        for stu_grade in stu_grades:
            stu_grade:StudentGrade
            ws.append(
                [str(stu_grade.student.number),stu_grade.student.name,stu_grade.student.major,
                 round(stu_grade.gpa,self.precision),stu_grade.absentCount]+stu_grade.absentNames
            )

        for major in CourseLib.ValidMajors:
            ws = wb.create_sheet(major)
            # 学号，姓名，总分，课程
            courses = self.courseLib.majorCourseList(major,self.mode,self.start,self.end)
            header = ['学号','姓名','学分绩']+[course.name for course in courses]
            ws.append(header)
            second = ['','','']+[course.credits for course in courses]
            ws.append(second)
            major_list = []
            for stu_id,stu_grade in self.gradeLib.items():
                stu_grade:StudentGrade
                if stu_grade.student.major != major:
                    continue
                major_list.append(stu_grade)
            major_list.sort(key=lambda stu_grade:stu_grade.gpa,reverse=True)
            for stu_grade in major_list:
                line = [str(stu_grade.student.number),stu_grade.student.name,
                        round(stu_grade.gpa,self.precision)]+\
                [stu_grade.getCourseGrade(course.id) for course in courses]
                ws.append(line)
        wb.save(filename)
        wb.close()