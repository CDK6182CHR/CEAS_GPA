#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string boolToString(bool x) {
	return x ? "是" : "否";
}

int main()
{
	cout << "欢迎使用现工院GPA计算系统-配置维护模块" << endl;
	cout << "配置文件保存在data/config.ini中，可通过本程序修改，也可直接编辑。" << endl;
	cout << "如需维护课程映射表，请移步data/map目录，直接编辑xlsx文件。" << endl;
	cout << "请依据提示输入配置信息：" << endl;
	cout << "选择课程集，1表示学年学分绩，2表示保研学分绩";
	int mode;
	cin >> mode;
	cout << "开始学期，用1--8的整数表示";
	int start, end;
	cin >> start;
	cout << "结束学期，用1--8的整数表示";
	cin >> end;
	bool useSubstitute;
	cout << "是否允许替代课程，1表示允许，0表示禁止";
	cin >> useSubstitute;
	cout << "是否仅使用第一次成绩（不认可补考、重修），1-是，0-否";
	bool useFirst;
	cin >> useFirst;
	int firstYear;
	cout<< "请输入要计算的年级，如“2017”";
	cin >> firstYear;
	cout << "是否使用0分来替代所缺课程，1-是，0-否";
	bool zeroForAbsent;
	cin >> zeroForAbsent;
	cout << "输出数据的小数位数";
	int prec;
	cin >> prec;
	cout << "输入完成，请确认您需要的配置是否为：" << endl;
	cout << "***********************************************" << endl;
	cout << "课程集合:" << mode << endl;
	cout << "开始学期:" << start << endl;
	cout << "结束学期:" << end << endl;
	cout << "是否允许替代课程:" << boolToString(useSubstitute) << endl;
	cout << "是否仅使用第一次成绩:" << boolToString(useFirst) << endl;
	cout << "要计算的年级:" << firstYear << endl;
	cout << "是否使用0分替代所缺课程:" << boolToString(zeroForAbsent) << endl;
	cout << "输出数据的小数位数:" << prec << endl;
	cout << "***********************************************" << endl;
	cout << "如果确认请输入1，输入其他任意内容则退出: ";
	int flag;
	cin >> flag;
	if (flag != 1)
		return 0;
	cout << "开始写入文件" << endl;
	ofstream file("../data/config.ini", ios::out);
	if (!file.is_open()) {
		cerr << "错误：无法打开文件config.ini。请确认上级目录中存在data子目录且有写入权限。" << endl;
		system("pause");
	}
	file << "# " << endl;
	file << "[ceas]" << endl;
	file << "mode = " << mode << endl;
	file << "startSemester = " << start << endl;
	file << "endSemester = " << end << endl;
	file << "useSubstitute = " << useSubstitute << endl;
	file << "useFirst = " << useFirst << endl;
	file << "firstYear = " << firstYear << endl;
	file << "zeroForAbsent = " << zeroForAbsent << endl;
	file << "precision = " << prec << endl;
	file.close();
	cout << "写入成功！" << endl;
	system("pause");
}
