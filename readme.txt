1、pyinstaller参数说明：
-F 表示生成单个可执行文件
-w 表示去掉控制台窗口，这在GUI界面时非常有用。不过如果是命令行程序的话那就把这个选项删除吧！
-p 表示你自己自定义需要加载的类路径，一般情况下用不到
-i 表示可执行文件的图标

2、list(set(failed_file)) 对failed_file列表进行去重操作，去掉同名文件
c = [1, 1, 2, 2, 3, 4, 5, 6]
print(set(c))  # 输出：{1, 2, 3, 4, 5, 6}
print(list(set(c)))  # 输出：[1, 2, 3, 4, 5, 6]

3、获取两个list的差集: list(set(b).difference(set(a))) # b中有而a中没有的      非常高效！
a = [1, 2, 3, 4, 5, 6]
b = [1, 4, 5]
print("获取两个列表所有成员（并集）:", set(a).union(set(b)))  # 输出：{1, 2, 3, 4, 5, 6}
print("获取两个列表相同成员（交集）:", set(a).intersection(set(b)))  # 输出：{1, 4, 5}
print("在集合a中但不再集合b中（差集）:", set(a).difference(set(b)))  # 输出：{2, 3, 6}
print("在集合b中但不再集合a中（差集）:", set(b).difference(set(a)))  # 输出：set()  空集合
print("返回两个集合交集的补集,即获取两个列表不同成员:", set(a).symmetric_difference(set(b)))  # 输出：{2, 3, 6}
print("判断集合a是不是集合b的子集:", set(a).issubset(set(b)))  # 输出：False
print("判断集合b是不是集合a的子集:", set(b).issubset(set(a)))  # 输出：True
print("判断集合a是不是集合b的父集合: ", set(a).issuperset(set(b)))  # 输出：True
print("判断集合b是不是集合a的父集合:", set(b).issuperset(set(a)))  # 输出：False

4、.map(str)实现数据转换，强制转换为string型
df['id_mode_level'] = df['歌曲ID'].map(str) + ',' + df['模式ID'].map(str) + ',' + df['难度'].map(str)
恋舞之星中格式为float64，需先转换为int型
lwstar['歌曲ID'] = lwstar['歌曲ID'].map(int)
lwstar['模式'] = lwstar['模式'].map(int)
lwstar['难度'] = lwstar['难度'].map(int)

5、恋舞之星特殊处理：
lwstar.dropna(axis=0, how='any', thresh=None, subset=None, inplace=True)
恋舞之星后面阶段为pvp不需要配置歌曲和模式，空值行需删除
axis: 维度，axis = 0表示index行, axis = 1表示columns列，默认为0
how: "all"表示这一行或列中的元素全部缺失（为nan）才删除这一行或列，
"any"表示这一行或列中只要有元素缺失，就删除这一行或列
thresh: 一行或一列中至少出现了thresh个才删除。
subset：在某些列的子集中选择出现了缺失值的列删除，不在子集中的含有缺失值得列或行不会删除（有axis决定是行还是列）
inplace：刷选过缺失值得新数据是存为副本还是直接在原数据上进行修改。

6、QMessageBox的使用方法：
reply = QMessageBox.information(self,  # 使用infomation信息框
                            "标题",
                            "消息",
                            QMessageBox.Yes | QMessageBox.No)
具体参照QMessageBox-test.py文件样例

7、QTextEdit的使用方法：
toPlainText()	返回文本框的内容
setPlainText()	设置文本框的内容
append()	文本框中追加内容

8、QCheckBox的使用方法：
isChecked()   检查复选框是否被选中
setChecked()  设置复选框的状态，设置为True表示选中，False表示取消选中的复选框

9、QPushButton的使用方法：
#点击信号与槽函数进行连接，这一步实现：在控制台输出被点击的按钮
self.btn1.clicked.connect(lambda :self.whichbtn(self.btn1))
#点击信号与槽函数进行连接，实现的目的：输入安妞的当前状态，按下还是释放
self.btn1.clicked.connect(self.btnstate)
#setEnabled()设置按钮是否可以使用，当设置为False的时候，按钮变成不可用状态，点击它不会发射信号
self.btn3.setEnabled(False)

10、QLineEdit的使用方法：
setText()	设置文本框的内容
text()	返回文本框的内容

11、ConfigReader的使用方法：
set(section,option,value)：对section中的option信息进行写入
add_section()：添加一个新的section
remove_option(option,value) 删除某个section下的option的数值
remove_section(section)  删除某个section的数值








