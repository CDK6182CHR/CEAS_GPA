"""
成绩有效性处理器。
聚合于GradeLib中。最后要删除gradeLib
"""
from .gradelib import GradeLib
from .gradelib import StudentGrade,Grade
from .courselib import CourseLib
from .coursemaps import multiMapTable,singleMapTable
from datetime import datetime

import json

class GradeValidator:
    LogDir = '../log/'
    def __init__(self,gradeLib,courseLib:CourseLib,mode:int=0b10):
        self.gradeLib = gradeLib  # type:GradeLib
        self.courseLib = courseLib  # type:CourseLib
        self.mode = mode  # type:int
        self.log = open(
            self.LogDir+datetime.now().strftime('log %Y-%m-%d_%H-%M-%S'),
            encoding='utf-8',errors='ignore'
        )

    def __del__(self):
        self.log.close()

    def validate(self):
        """
        接口方法
        """
        self.multiMap()

    def multiMap(self):
        """
        对体验英语的特殊处理。一门体验英语映射到同一学期的两门英语课中。
        仍在list中完成。
        """
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
                    stu_grade.addGrade(
                        Grade(
                            stu_number,
                            newId,
                            mappedCourse.name,
                            mappedCourse.credits,
                            grade[0].semester,
                            grade[0].grade_type,
                            grade[0].total
                        )
                    )
                self.log.write(f"multiMap: {courseId}->{newId}, student{stu_number}\n")
                del stu_grade._source[courseId]

    def singleMap(self):
        """
        处理英语课名称不同需要映射的情况。需考虑多条数据。
        """



