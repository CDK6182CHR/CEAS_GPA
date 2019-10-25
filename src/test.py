from ceasgpa.courselib import CourseLib
from ceasgpa.studentlist import StudentList
from ceasgpa.gradelib import GradeLib

courseLib = CourseLib()
courseLib.readLibFile()
# courseLib.saveJson()
# courseLib.readJson()
courseLib.saveMarkdown()
courseLib.saveCourseMarkdown()
courseLib.saveJson()
