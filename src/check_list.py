"""
与数据库对照，检查保研课程清单是否正确。
基于课程名称检验，名称不同的人工。
"""
from ceasgpa.courselib import CourseLib, Course

src = '../data/list.txt'
sep = '==============================='
tp = 0b10  # A类课程

majors = CourseLib.ValidMajors
lib = CourseLib()
lib.readLibFile()

with open(src,encoding='utf-8',errors='ignore') as fp:
    txt = fp.read()
txt_lst = txt.split(sep)

assert len(txt_lst) == len(majors)

for t,major in zip(txt_lst,majors):
    print(f"=========={major}===========")
    courses_lib_lst = lib.majorCourseList(major,tp,1,6)
    courses_lib = dict([(c.name,c) for c in courses_lib_lst])
    courses_src = dict(map(lambda x:[x.split('\t')[0],int(x.split('\t')[1])],
                           filter(bool,map(lambda x:x.strip(),t.split('\n')))))
    set_lib = set(courses_lib.keys())
    set_src = set(courses_src.keys())
    print("在数据库但不在列表中的课程：",end='')
    set1 = set_lib-set_src
    print(len(set1))
    print("课程\t学分")
    for n in set1:
        c:Course = courses_lib[n]
        print(f"{n}\t{c.credits}")
    print("在列表但不在数据库中的课程：",end='')
    set2 = set_src-set_lib
    print(len(set2))
    for n in (set2):
        print(f"{n}\t{courses_src[n]}")
    print("学分数不一致的课程：")
    print(f"课程名\t数据库\t列表")
    for n in (set_src & set_lib):
        c:Course = courses_lib[n]
        if c.credits != courses_src[n]:
            print(f"{n}\t{c.credits}\t{courses_src[n]}")





