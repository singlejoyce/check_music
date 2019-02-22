import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from checkmusic import *
from configreader import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.music = CheckMusic()
        self.check_assetbundle = QtWidgets.QCheckBox(self)
        self.check_musicsmp = QtWidgets.QCheckBox(self)
        self.check_stage = QtWidgets.QCheckBox(self)
        self.music_file_dir = QtWidgets.QTextEdit(self)
        self.label = QtWidgets.QLabel(self)
        self.adb_assetbundle_file_dir = QtWidgets.QTextEdit(self)
        self.label_2 = QtWidgets.QLabel(self)
        self.controller_txt_dir = QtWidgets.QTextEdit(self)
        self.label_3 = QtWidgets.QLabel(self)
        self.stage_dir = QtWidgets.QTextEdit(self)
        self.label_4 = QtWidgets.QLabel(self)
        self.label_5 = QtWidgets.QLabel(self)
        self.check_fairlyland = QtWidgets.QCheckBox(self)
        self.check_magiclamp = QtWidgets.QCheckBox(self)
        self.label_6 = QtWidgets.QLabel(self)
        self.check_dama = QtWidgets.QCheckBox(self)
        self.check_lwstar = QtWidgets.QCheckBox(self)
        self.check_starmentor = QtWidgets.QCheckBox(self)
        self.check_musicrank = QtWidgets.QCheckBox(self)
        self.check_diamondleague = QtWidgets.QCheckBox(self)
        self.startButton = QtWidgets.QPushButton(self)
        self.label_8 = QtWidgets.QLabel(self)
        self.ios_assetbundle_file_dir = QtWidgets.QTextEdit(self)
        self.resulttxt = QtWidgets.QTextEdit(self)
        self.label_7 = QtWidgets.QLabel(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 1060, 862)
        self.setWindowTitle('检查音乐工具')
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.setFont(font)
        self.check_assetbundle.setGeometry(QtCore.QRect(710, 330, 229, 22))
        self.check_assetbundle.setFont(font)
        self.check_assetbundle.setObjectName("check_assetbundle")
        self.check_musicsmp.setGeometry(QtCore.QRect(710, 360, 229, 22))
        self.check_musicsmp.setFont(font)
        self.check_musicsmp.setObjectName("check_musicsmp")
        self.check_stage.setGeometry(QtCore.QRect(710, 390, 229, 22))
        self.check_stage.setFont(font)
        self.check_stage.setObjectName("check_stage")
        self.music_file_dir.setGeometry(QtCore.QRect(240, 40, 761, 31))
        self.music_file_dir.setObjectName("music_file_dir")
        self.label.setGeometry(QtCore.QRect(30, 40, 201, 31))
        self.label.setObjectName("label")
        self.adb_assetbundle_file_dir.setGeometry(QtCore.QRect(240, 90, 761, 31))
        self.adb_assetbundle_file_dir.setObjectName("adb_assetbundle_file_dir")
        self.label_2.setGeometry(QtCore.QRect(30, 90, 201, 31))
        self.label_2.setObjectName("label_2")
        self.controller_txt_dir.setGeometry(QtCore.QRect(240, 190, 761, 31))
        self.controller_txt_dir.setObjectName("controller_txt_dir")
        self.label_3.setGeometry(QtCore.QRect(30, 190, 201, 31))
        self.label_3.setObjectName("label_3")
        self.stage_dir.setGeometry(QtCore.QRect(240, 240, 761, 31))
        self.stage_dir.setObjectName("stage_dir")
        self.label_4.setGeometry(QtCore.QRect(30, 240, 201, 31))
        self.label_4.setObjectName("label_4")
        self.label_5.setGeometry(QtCore.QRect(710, 300, 291, 16))
        self.label_5.setObjectName("label_5")
        self.check_fairlyland.setGeometry(QtCore.QRect(710, 530, 229, 22))
        self.check_fairlyland.setFont(font)
        self.check_fairlyland.setObjectName("check_fairlyland")
        self.check_magiclamp.setGeometry(QtCore.QRect(710, 470, 301, 22))
        self.check_magiclamp.setFont(font)
        self.check_magiclamp.setObjectName("check_magiclamp")
        self.label_6.setGeometry(QtCore.QRect(710, 440, 291, 16))
        self.label_6.setObjectName("label_6")
        self.check_dama.setGeometry(QtCore.QRect(710, 500, 229, 22))
        self.check_dama.setFont(font)
        self.check_dama.setObjectName("check_dama")
        self.check_lwstar.setGeometry(QtCore.QRect(710, 560, 229, 22))
        self.check_lwstar.setFont(font)
        self.check_lwstar.setObjectName("check_lwstar")
        self.check_starmentor.setGeometry(QtCore.QRect(710, 590, 301, 22))
        self.check_starmentor.setFont(font)
        self.check_starmentor.setObjectName("check_starmentor")
        self.check_musicrank.setGeometry(QtCore.QRect(710, 620, 229, 22))
        self.check_musicrank.setFont(font)
        self.check_musicrank.setObjectName("check_musicrank")
        self.check_diamondleague.setGeometry(QtCore.QRect(710, 650, 229, 22))
        self.check_diamondleague.setFont(font)
        self.check_diamondleague.setObjectName("check_diamondleague")
        self.startButton.setGeometry(QtCore.QRect(710, 750, 261, 51))
        self.startButton.setObjectName("startButton")
        self.startButton.clicked.connect(self.start)
        self.resulttxt.setGeometry(QtCore.QRect(30, 345, 631, 471))
        self.resulttxt.setObjectName("result")
        self.label_7.setGeometry(QtCore.QRect(30, 280, 400, 61))
        self.label_7.setObjectName("label_7")
        self.ios_assetbundle_file_dir.setGeometry(QtCore.QRect(240, 140, 761, 31))
        self.ios_assetbundle_file_dir.setObjectName("ios_assetbundle_file_dir")
        self.label_8.setGeometry(QtCore.QRect(30, 140, 201, 31))
        self.label_8.setObjectName("label_8")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.check_assetbundle.setText(_translate("Dialog", "检查assetbundle动作文件"))
        self.check_musicsmp.setText(_translate("Dialog", "检查音乐smp文件"))
        self.check_stage.setText(_translate("Dialog", "检查stage谱面文件"))
        self.label.setText(_translate("Dialog", "音乐文件Music地址："))
        self.label_2.setText(_translate("Dialog", "安卓-Animations地址："))
        self.label_3.setText(_translate("Dialog", "动作谱面Controller地址："))
        self.label_4.setText(_translate("Dialog", "谱面Stage地址："))
        self.label_5.setText(_translate("Dialog", "检查音乐表中相关资源："))
        self.check_fairlyland.setText(_translate("Dialog", "检查舞团秘境关卡配置"))
        self.check_magiclamp.setText(_translate("Dialog", "检查魔法神灯关卡配置（主题和主线）"))
        self.label_6.setText(_translate("Dialog", "检查其他功能模块中配置："))
        self.check_dama.setText(_translate("Dialog", "检查舞团大妈关卡配置"))
        self.check_lwstar.setText(_translate("Dialog", "检查恋舞之星关卡配置"))
        self.check_starmentor.setText(_translate("Dialog", "检查星恋挑战关卡配置"))
        self.check_musicrank.setText(_translate("Dialog", "检查音悦榜歌曲配置"))
        self.check_diamondleague.setText(_translate("Dialog", "检查钻石联赛歌曲配置"))
        self.startButton.setText(_translate("Dialog", "开始检查"))
        self.label_7.setText(_translate("Dialog", "结果说明:\n配置正常时结果格式为：[]\n配置异常时结果格式为：[歌曲ID,歌曲模式,歌曲难度]"))
        self.label_8.setText(_translate("Dialog", "IOS-Animations地址："))

        # 将配置加载到界面显示
        # 勾选框显示处理
        self.check_assetbundle.setChecked(int(self.music.check_assetbundle))
        self.check_musicsmp.setChecked(int(self.music.check_musicsmp))
        self.check_stage.setChecked(int(self.music.check_stage))
        self.check_fairlyland.setChecked(int(self.music.check_fairlyland))
        self.check_dama.setChecked(int(self.music.check_dama))
        self.check_magiclamp.setChecked(int(self.music.check_magiclamp))
        self.check_lwstar.setChecked(int(self.music.check_lwstar))
        self.check_starmentor.setChecked(int(self.music.check_starmentor))
        self.check_musicrank.setChecked(int(self.music.check_musicrank))
        self.check_diamondleague.setChecked(int(self.music.check_diamondleague))
        # 文本框显示处理
        self.music_file_dir.setPlainText(self.music.music_file_dir)
        self.stage_dir.setPlainText(self.music.stage_dir)
        self.controller_txt_dir.setPlainText(self.music.controller_txt_dir)
        self.adb_assetbundle_file_dir.setPlainText(self.music.adb_assetbundle_file_dir)
        self.ios_assetbundle_file_dir.setPlainText(self.music.ios_assetbundle_file_dir)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示', '确认退出吗？',
                                     QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel)
        if reply == QMessageBox.Ok:
            event.accept()
        elif reply == QMessageBox.Cancel:
            event.ignore()

    def save_config(self):
        fp = 'Config.ini'
        if os.path.exists(fp):
            config = ConfigReader(fp)
            config.setdic('fileDir', 'music_file_dir', self.music_file_dir.toPlainText())
            config.setdic('fileDir', 'stage_dir', self.stage_dir.toPlainText())
            config.setdic('fileDir', 'controller_txt_dir', self.controller_txt_dir.toPlainText())
            config.setdic('fileDir', 'adb_assetbundle_file_dir', self.adb_assetbundle_file_dir.toPlainText())
            config.setdic('fileDir', 'ios_assetbundle_file_dir', self.ios_assetbundle_file_dir.toPlainText())

            config.setdic('checkStatus', 'check_assetbundle', str(self.check_assetbundle.checkState()))
            config.setdic('checkStatus', 'check_musicsmp', str(self.check_musicsmp.checkState()))
            config.setdic('checkStatus', 'check_stage', str(self.check_stage.checkState()))
            config.setdic('checkStatus', 'check_fairlyland', str(self.check_fairlyland.checkState()))
            config.setdic('checkStatus', 'check_dama', str(self.check_dama.checkState()))
            config.setdic('checkStatus', 'check_magiclamp', str(self.check_magiclamp.checkState()))
            config.setdic('checkStatus', 'check_lwstar', str(self.check_lwstar.checkState()))
            config.setdic('checkStatus', 'check_starmentor', str(self.check_starmentor.checkState()))
            config.setdic('checkStatus', 'check_musicrank', str(self.check_musicrank.checkState()))
            config.setdic('checkStatus', 'check_diamondleague', str(self.check_diamondleague.checkState()))
            with open(fp, "w+") as f:
                config.CReader.write(f)

        # 将修改的状态同步到checkmusic类中
        self.music.music_file_dir = self.music_file_dir.toPlainText()
        self.music.stage_dir = self.stage_dir.toPlainText()
        self.music.controller_txt_dir = self.controller_txt_dir.toPlainText()
        self.music.adb_assetbundle_file_dir = self.adb_assetbundle_file_dir.toPlainText()
        self.music.ios_assetbundle_file_dir = self.ios_assetbundle_file_dir.toPlainText()

    def start(self):
        # 将修改的状态进行保存和同步
        self.save_config()
        resultstr = ''

        # 检查音乐表中相关资源是否存在
        if self.check_assetbundle.isChecked():
            result = self.music.process_assetbundle()
            resultstr = resultstr + "\nDance.txt文件检查结果：" + str(result[0]) + \
                        "\n安卓平台动作文件检查结果：" + str(result[1]) + "\nios平台动作文件检查结果：" \
                        + str(result[2])

        if self.check_musicsmp.isChecked():
            result = self.music.process_music_smp()
            resultstr = resultstr + "\n音乐smp文件检查结果：" + str(result)

        if self.check_stage.isChecked():
            result = self.music.process_stage()
            resultstr = resultstr + "\n安卓平台stage文件文件检查结果：" + str(result[0]) + \
                        "\nios平台stage文件文件检查结果：" + str(result[1])

        # 检查其他功能模块中配置的歌曲信息在音乐表中是否存在
        if self.check_dama.isChecked():
            result = self.music.process_dama()
            resultstr = resultstr + "\n广场舞大妈.xlsx检查结果：" + str(result)

        if self.check_fairlyland.isChecked():
            result = self.music.process_fairlyland()
            resultstr = resultstr + "\n舞团秘境.xlsx检查结果：" + str(result)

        if self.check_lwstar.isChecked():
            result = self.music.process_lwstar()
            resultstr = resultstr + "\n恋舞之星.xlsx检查结果：" + str(result)

        if self.check_magiclamp.isChecked():
            result = self.music.process_magiclamp()
            resultstr = resultstr + "\n魔法神灯.xlsx-主线关卡检查结果：" + str(result[0]) + \
                        "\n魔法神灯.xlsx-主题关卡检查结果：" + str(result[1])

        if self.check_diamondleague.isChecked():
            result = self.music.process_diamondleague()
            resultstr = resultstr + "\n钻石联赛.xlsx检查结果：" + str(result)

        if self.check_musicrank.isChecked():
            result = self.music.process_musicrank()
            resultstr = resultstr + "\n音悦榜.xlsx检查结果：" + str(result)

        if self.check_starmentor.isChecked():
            result = self.music.process_starmentor()
            resultstr = resultstr + "\n星恋挑战.xlsx检查结果：" + str(result)

        # 结果输入到resulttxt框控件内
        self.resulttxt.setPlainText(resultstr)
        # 检查结束，弹出检查完成提示框
        QMessageBox.information(self, "提示", self.tr("音乐检查完成!"), QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
