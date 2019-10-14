"""
成绩有效性处理器。
聚合于Calculator中
"""
from .gradelib import GradeLib
from .studentgrade import StudentGrade,Grade
from .courselib import CourseLib,Course
from .coursemaps import multiMapTable,singleMapTable
from datetime import datetime

import json

class GradeValidator:
    LogDir = '../log/'
    def __init__(self,gradeLib,courseLib:CourseLib,mode,start,end):
        self.gradeLib = gradeLib  # type:GradeLib
        self.courseLib = courseLib  # type:CourseLib
        self.mode = mode  # type:int
        self.startSemester = start  # type:int
        self.endSemester = end  # type:int
        self.log = open(
            self.LogDir+datetime.now().strftime('log %Y-%m-%d_%H-%M-%S.txt'),
            'w',encoding='utf-8',errors='ignore'
        )

    def __del__(self):
        pass
        # self.log.close()

    def validate(self):
        """
        接口方法
        """
        self.multiMap()
        self.singleMap()
        self.choose()
        self.filtByList()

    def multiMap(self):
        """
        对体验英语的特殊处理。一门体验英语映射到同一学期的两门英语课中。
        仍在list中完成。
        """
        self.log.write("**********multiMap**********\n")
        for stu_number,stu_grade in self.gradeLib.items():
            stu_grade:StudentGrade
            for courseId,grade in stu_grade._source.copy().items():
                if multiMapTable.get(courseId,None) is None:
                    continue
                # 在multiMap映射表中
                if len(grade)!=1:
                    print(f"multiMap: more than one courses to be multi map, student {stu_number} course {courseId} length {len(grade)}")

                for newId in multiMapTable[courseId]:
                    mappedCourse = self.courseLib.courseById(newId)
                    if mappedCourse is None:
                        print(f"Unexpceted None course {newId},"
                              f"mapped from {courseId}")
                    stu_grade.addGrade(
                        Grade(
                            stu_number,
                            newId,
                            mappedCourse.name,
                            mappedCourse.credits,
                            grade[0].semester,
                            grade[0].grade_type,
                            grade[0].total,
                            grade[0].note2+" mapped",
                            grade[0].flag
                        )
                    )
                self.log.write(f"{courseId}->{newId}, student{stu_number}\n")
                del stu_grade._source[courseId]

    def singleMap(self):
        """
        处理英语课名称不同需要映射的情况。需考虑多条数据。
        """
        self.log.write("**********singleMap*********\n")
        for stu_number,stu_grade in self.gradeLib.items():
            stu_grade:StudentGrade
            for courseId, grades in stu_grade._source.copy().items():
                newId = singleMapTable.get(courseId,None)
                if newId is None:
                    continue
                mappedCourse = self.courseLib.courseById(newId)
                for grade in grades:
                    grade.course_name = mappedCourse.name
                    grade.course_number = mappedCourse.id
                    grade.note2+=" mapped"
                    self.log.write(f"{grade}->{mappedCourse}\n")
                stu_grade._source[newId]=stu_grade._source[courseId]
                del stu_grade._source[courseId]

    def choose(self):
        """
        在有多条记录的选项中，选择一条记录来处理
        """
        self.log.write("*******choose******\n")
        for stu_number,stu_grade in self.gradeLib.items():
            stu_grade:StudentGrade
            for courseId, grades in stu_grade._source.copy().items():
                if len(grades)==1:
                    continue
                # 先按学期排序
                grades.sort(key=lambda grade:grade.semester)
                for grade in grades.copy():
                    if grade.semester != grades[0].semester:
                        grades.remove(grade)
                        self.log.write(f"By semester: delete {grade}\n")
                if len(grades) == 1:
                    continue
                # 一个学期内应该最多两条记录，一个原始一个补考
                # 现在只剩两个
                for grade in grades.copy():
                    if '补考' in grade.flag:
                        grades.remove(grade)
                        self.log.write(f"By flag 补考: delete {grade}\n")
                if len(grades) >= 2:
                    print(f"choose: unknown multi courses length {len(grades)}",*grades)
            stu_grade._ok = True

    def filtByList(self):
        """
        按所选模式筛选课程，并放进table中
        """
        self.log.write("**********filtByList***********\n")
        for stu_number,stu_grade in self.gradeLib.items():
            stu_grade:StudentGrade
            student = stu_grade.student
            major = stu_grade.student.major
            for course_id, course in self.courseLib.items():
                course:Course
                if not self.startSemester <= course.semester <= self.endSemester:
                    continue
                if course.majorTypes[major] & self.mode:
                    # 添加这门课程！
                    grades = stu_grade._source.get(course_id,None)
                    if grades is None:
                        stu_grade._table[course_id]=Grade(
                            student.number,course_id,course.name,
                            course.credits,'NA','NA',0.0,'缺数据',''
                        )
                        self.log.write(f"缺少必修课程：{course} {student} 自动添加0分数据\n")
                        print(f"缺少必修课程：{course} {student} 自动添加0分数据")
                    else:
                        grade = grades[0]
                        stu_grade._table[course_id]=grade
                        if grade.course_name != course.name:
                            print(f"课程名不一致 {course} {grade}")
                            # self.log.write(
                            #     f"课程名不一致 {course} {grade}\n")
                        elif grade.credits != course.credits:
                            print(f"学分数不一致 {course} {grade}")
                            self.log.write(
                                f"学分数不一致 {course} {grade}\n")
                        del stu_grade._source[course_id]
            for course_id,grades in stu_grade._source.items():
                self.log.write(f"非必修课 {grades[0]}\n")



