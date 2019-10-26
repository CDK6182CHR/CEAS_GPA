from ceasgpa.calculator import GpaCalculator
from configparser import ConfigParser

cp = ConfigParser()
try:
    cp.read('../data/config.ini')
    sec = 'ceas'

    mode = cp.getint(sec,'mode')
    start = cp.getint(sec,'startSemester')
    end = cp.getint(sec,'endSemester')
    useSubstitute = bool(cp.getint(sec,'useSubstitute'))
    useFirst = bool(cp.getint(sec,'useFirst'))
    firstYear = cp.get(sec,'firstYear')
    zeroForAbsent = bool(cp.getint(sec,'zeroForAbsent'))
    precision = cp.getint(sec,'precision')
except:
    print("读取配置文件失败，使用默认值。")
    mode = 0b10
    start = 1
    end = 4
    useSubstitute = False
    useFirst = True
    firstYear = "2017"
    zeroForAbsent = True
    precision = 3

info = f"""
欢迎使用现工院GPA计算系统  更新：2019年10月26日
请在准备以下文件：
成绩表文件，以.xls（小写）结尾，放在data/grades目录下。文件可以任意多，也可以在任一层的子目录下。
替代课程表文件，文件名为data/map/substitute.xlsx
多课程号映射文件，文件名为data/map/multiMap.xlsx
单课程号映射文件，文件名为data/map/singleMap.xlsx
--------------------------------------------------------
请确认以下运行参数：
课程集：{mode}-{'学年' if mode==1 else '保研'}
开始学期：{start}
结束学期：{end}
接受替代课程：{useSubstitute}
仅接受第一次结果：{useFirst}
缺课按0分计算：{zeroForAbsent}
输出小数位数：{precision}
如需修改请移步“参数设定”。
输出文件为data/output.xlsx和data/output_id.xlsx，这两个文件将被无条件覆盖。
按ENTER继续计算，否则请关闭窗口。
"""

input(info)
print("程序启动")

calculator = GpaCalculator(mode,start,end,useSubstitute,useFirst,firstYear,
                           zeroForAbsent,precision)
calculator.validate()
calculator.calculate()
calculator.saveExcel()
calculator.saveIdOnlyExcel()

input("计算完成，按ENTER关闭窗口")