from ceasgpa.courselib import CourseLib
from ceasgpa.studentlist import StudentList
from ceasgpa.gradelib import GradeLib

courseLib = CourseLib()
courseLib.readLibFile()
# courseLib.saveJson()
# courseLib.readJson()
courseLib.saveMarkdown(note='修正《高分子材料科学》《组织工程与再生医学》学分数。')
courseLib.saveCourseMarkdown(note='修正《高分子材料科学》《组织工程与再生医学》学分数。')
courseLib.saveJson()
