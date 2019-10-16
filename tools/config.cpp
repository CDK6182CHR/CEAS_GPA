#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string boolToString(bool x) {
	return x ? "��" : "��";
}

int main()
{
	cout << "��ӭʹ���ֹ�ԺGPA����ϵͳ-����ά��ģ��" << endl;
	cout << "�����ļ�������data/config.ini�У���ͨ���������޸ģ�Ҳ��ֱ�ӱ༭��" << endl;
	cout << "����ά���γ�ӳ������Ʋ�data/mapĿ¼��ֱ�ӱ༭xlsx�ļ���" << endl;
	cout << "��������ʾ����������Ϣ��" << endl;
	cout << "ѡ��γ̼���1��ʾѧ��ѧ�ּ���2��ʾ����ѧ�ּ�";
	int mode;
	cin >> mode;
	cout << "��ʼѧ�ڣ���1--8��������ʾ";
	int start, end;
	cin >> start;
	cout << "����ѧ�ڣ���1--8��������ʾ";
	cin >> end;
	bool useSubstitute;
	cout << "�Ƿ���������γ̣�1��ʾ����0��ʾ��ֹ";
	cin >> useSubstitute;
	cout << "�Ƿ��ʹ�õ�һ�γɼ������Ͽɲ��������ޣ���1-�ǣ�0-��";
	bool useFirst;
	cin >> useFirst;
	int firstYear;
	cout<< "������Ҫ������꼶���硰2017��";
	cin >> firstYear;
	cout << "�Ƿ�ʹ��0���������ȱ�γ̣�1-�ǣ�0-��";
	bool zeroForAbsent;
	cin >> zeroForAbsent;
	cout << "������ݵ�С��λ��";
	int prec;
	cin >> prec;
	cout << "������ɣ���ȷ������Ҫ�������Ƿ�Ϊ��" << endl;
	cout << "***********************************************" << endl;
	cout << "�γ̼���:" << mode << endl;
	cout << "��ʼѧ��:" << start << endl;
	cout << "����ѧ��:" << end << endl;
	cout << "�Ƿ���������γ�:" << boolToString(useSubstitute) << endl;
	cout << "�Ƿ��ʹ�õ�һ�γɼ�:" << boolToString(useFirst) << endl;
	cout << "Ҫ������꼶:" << firstYear << endl;
	cout << "�Ƿ�ʹ��0�������ȱ�γ�:" << boolToString(zeroForAbsent) << endl;
	cout << "������ݵ�С��λ��:" << prec << endl;
	cout << "***********************************************" << endl;
	cout << "���ȷ��������1���������������������˳�: ";
	int flag;
	cin >> flag;
	if (flag != 1)
		return 0;
	cout << "��ʼд���ļ�" << endl;
	ofstream file("../data/config.ini", ios::out);
	if (!file.is_open()) {
		cerr << "�����޷����ļ�config.ini����ȷ���ϼ�Ŀ¼�д���data��Ŀ¼����д��Ȩ�ޡ�" << endl;
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
	cout << "д��ɹ���" << endl;
	system("pause");
}
