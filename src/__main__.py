from ceasgpa.courselib import CourseLib
from ceasgpa.studentlist import StudentList
from ceasgpa.gradelib import GradeLib

courseLib = CourseLib()
# courseLib.readLibFile()
# courseLib.saveJson()
courseLib.readJson()
courseLib.saveMarkdown()

stuList = StudentList()
# stuList.readList()
# stuList.saveJson()
stuList.readJson()
stuList.saveJson()

gradeLib = GradeLib(stuList)
gradeLib.readFileList()
