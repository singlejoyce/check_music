# -*- coding:utf-8 -*-
"""
Basic Layout
"""
import sys

import os

from checkmusic import CheckMusic
from configreader import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import *

__author__ = "joyce"


class MainUi(QWidget):
    def __init__(self):
        super(MainUi, self).__init__()
        self.startButton = QPushButton("开始检查")
        self.startButton.clicked.connect(self.start)
        self.resultEditor = QTextEdit()
        self.check_quest = QCheckBox("检查任务中歌曲配置")
        self.check_diamondleague = QCheckBox("检查钻石联赛歌曲配置")
        self.check_musicrank = QCheckBox("检查音悦榜歌曲配置")
        self.check_starmentor = QCheckBox("检查星恋挑战关卡配置")
        self.check_lwstar = QCheckBox("检查恋舞之星关卡配置")
        self.check_dama = QCheckBox("检查舞团大妈关卡配置")
        self.check_magiclamp = QCheckBox("检查魔法神灯关卡配置（主题和主线）")
        self.check_fairlyland = QCheckBox("检查舞团秘境关卡配置")
        self.check_music = QCheckBox("检查音乐文件")
        self.check_stage = QCheckBox("检查stage谱面文件")
        self.check_assetbundle = QCheckBox("检查assetbundle动作文件")

        # 勾选框状态显示处理
        self.check_assetbundle.setChecked(int(music.check_assetbundle))
        self.check_music.setChecked(int(music.check_music))
        self.check_stage.setChecked(int(music.check_stage))
        self.check_fairlyland.setChecked(int(music.check_fairlyland))
        self.check_dama.setChecked(int(music.check_dama))
        self.check_magiclamp.setChecked(int(music.check_magiclamp))
        self.check_lwstar.setChecked(int(music.check_lwstar))
        self.check_starmentor.setChecked(int(music.check_starmentor))
        self.check_musicrank.setChecked(int(music.check_musicrank))
        self.check_diamondleague.setChecked(int(music.check_diamondleague))
        self.check_quest.setChecked(int(music.check_quest))
        # 文本框内文字显示处理
        self.stage_dir_Editor = QLineEdit(music.stage_dir)
        self.music_file_dir_Editor = QLineEdit(music.music_file_dir)
        self.controller_txt_dir_Editor = QLineEdit(music.controller_txt_dir)
        self.adb_assetbundle_file_dir_Editor = QLineEdit(music.adb_assetbundle_file_dir)
        self.ios_assetbundle_file_dir_Editor = QLineEdit(music.ios_assetbundle_file_dir)

        self.initUi()

    def initUi(self):
        self.resize(1060, 662)
        self.setWindowTitle('检查音乐工具')
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.setFont(font)
        self.retranslateUi()

    def retranslateUi(self):
        reslutGroupBox = QGroupBox("结果输出：")
        checkbtnGroupBox1 = QGroupBox("检查音乐表中相关资源：")
        checkbtnGroupBox2 = QGroupBox("检查其他功能模块中配置：")
        dirGroupBox = QGroupBox("资源地址路径配置：")
        btnGroupBox = QGroupBox("")

        dir_layout = QGridLayout()
        music_file_dir_Label = QLabel("音乐文件Music地址：")
        stage_dir_Label = QLabel("谱面Stage地址：")
        controller_txt_dir_Label = QLabel("动作谱面Controller地址：")
        adb_assetbundle_file_dir_Label = QLabel("安卓-Animations地址：")
        ios_assetbundle_file_dir_Label = QLabel("iOS-Animations地址：")
        dir_layout.addWidget(music_file_dir_Label, 1, 0)
        dir_layout.addWidget(self.music_file_dir_Editor, 1, 1)
        dir_layout.addWidget(stage_dir_Label, 2, 0)
        dir_layout.addWidget(self.stage_dir_Editor, 2, 1)
        dir_layout.addWidget(controller_txt_dir_Label, 3, 0)
        dir_layout.addWidget(self.controller_txt_dir_Editor, 3, 1)
        dir_layout.addWidget(adb_assetbundle_file_dir_Label, 4, 0)
        dir_layout.addWidget(self.adb_assetbundle_file_dir_Editor, 4, 1)
        dir_layout.addWidget(ios_assetbundle_file_dir_Label, 5, 0)
        dir_layout.addWidget(self.ios_assetbundle_file_dir_Editor, 5, 1)
        dir_layout.setColumnStretch(1, 5)
        dirGroupBox.setLayout(dir_layout)

        checkbtn_layout1 = QVBoxLayout()
        checkbtn_layout1.addWidget(self.check_assetbundle)
        checkbtn_layout1.addWidget(self.check_music)
        checkbtn_layout1.addWidget(self.check_stage)
        checkbtnGroupBox1.setLayout(checkbtn_layout1)

        checkbtn_layout2 = QVBoxLayout()
        checkbtn_layout2.addWidget(self.check_quest)
        checkbtn_layout2.addWidget(self.check_fairlyland)
        checkbtn_layout2.addWidget(self.check_magiclamp)
        checkbtn_layout2.addWidget(self.check_dama)
        checkbtn_layout2.addWidget(self.check_lwstar)
        checkbtn_layout2.addWidget(self.check_starmentor)
        checkbtn_layout2.addWidget(self.check_musicrank)
        checkbtn_layout2.addWidget(self.check_diamondleague)
        checkbtnGroupBox2.setLayout(checkbtn_layout2)

        result_layout = QVBoxLayout()
        result_layout.addWidget(self.resultEditor)
        reslutGroupBox.setLayout(result_layout)

        btn_layout = QVBoxLayout()
        btn_layout.addWidget(self.startButton)
        btnGroupBox.setLayout(btn_layout)

        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(checkbtnGroupBox1)
        vboxLayout.addWidget(checkbtnGroupBox2)
        vboxLayout.addWidget(btnGroupBox)
        # vboxLayout.addStretch()  # 平分布局

        hboxLayout = QHBoxLayout()
        hboxLayout.addWidget(reslutGroupBox)
        hboxLayout.addLayout(vboxLayout)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(dirGroupBox)
        mainLayout.addLayout(hboxLayout)
        self.setLayout(mainLayout)
        
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示', '确认退出吗？',
                                     QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel)
        if reply == QMessageBox.Ok:
            event.accept()
        elif reply == QMessageBox.Cancel:
            event.ignore()

    def save_config(self):
        fp = os.getcwd() + "\\Config\\Config.ini"
        if os.path.exists(fp):
            config = ConfigReader(fp)
            config.setdic('fileDir', 'music_file_dir', self.music_file_dir_Editor.text())
            config.setdic('fileDir', 'stage_dir', self.stage_dir_Editor.text())
            config.setdic('fileDir', 'controller_txt_dir', self.controller_txt_dir_Editor.text())
            config.setdic('fileDir', 'adb_assetbundle_file_dir', self.adb_assetbundle_file_dir_Editor.text())
            config.setdic('fileDir', 'ios_assetbundle_file_dir', self.ios_assetbundle_file_dir_Editor.text())

            config.setdic('checkStatus', 'check_assetbundle', str(self.check_assetbundle.checkState()))
            config.setdic('checkStatus', 'check_music', str(self.check_music.checkState()))
            config.setdic('checkStatus', 'check_stage', str(self.check_stage.checkState()))
            config.setdic('checkStatus', 'check_fairlyland', str(self.check_fairlyland.checkState()))
            config.setdic('checkStatus', 'check_dama', str(self.check_dama.checkState()))
            config.setdic('checkStatus', 'check_magiclamp', str(self.check_magiclamp.checkState()))
            config.setdic('checkStatus', 'check_lwstar', str(self.check_lwstar.checkState()))
            config.setdic('checkStatus', 'check_starmentor', str(self.check_starmentor.checkState()))
            config.setdic('checkStatus', 'check_musicrank', str(self.check_musicrank.checkState()))
            config.setdic('checkStatus', 'check_diamondleague', str(self.check_diamondleague.checkState()))
            config.setdic('checkStatus', 'check_quest', str(self.check_quest.checkState()))
            with open(fp, "w+") as f:
                config.CReader.write(f)

    def synch_config(self):
        # 将修改的状态同步到checkmusic类中
        if os.path.exists(self.music_file_dir_Editor.text()):
            music.music_file_dir = self.music_file_dir_Editor.text()
        else:
            reply = QMessageBox.critical(self, "提示", self.tr("资源地址不存在，请检查!"), QMessageBox.Ok)
            if reply == QMessageBox.Ok:
                return False

        if os.path.exists(self.stage_dir_Editor.text()):
            music.stage_dir = self.stage_dir_Editor.text()
        else:
            reply = QMessageBox.critical(self, "提示", self.tr("资源地址不存在，请检查!"), QMessageBox.Ok)
            if reply == QMessageBox.Ok:
                return False

        if os.path.exists(self.controller_txt_dir_Editor.text()):
            music.controller_txt_dir = self.controller_txt_dir_Editor.text()
        else:
            reply = QMessageBox.critical(self, "提示", self.tr("资源地址不存在，请检查!"), QMessageBox.Ok)
            if reply == QMessageBox.Ok:
                return False

        if os.path.exists(self.adb_assetbundle_file_dir_Editor.text()):
            music.adb_assetbundle_file_dir = self.adb_assetbundle_file_dir_Editor.text()
        else:
            reply = QMessageBox.critical(self, "提示", self.tr("资源地址不存在，请检查!"), QMessageBox.Ok)
            if reply == QMessageBox.Ok:
                return False

        if os.path.exists(self.ios_assetbundle_file_dir_Editor.text()):
            music.ios_assetbundle_file_dir = self.ios_assetbundle_file_dir_Editor.text()
        else:
            reply = QMessageBox.critical(self, "提示", self.tr("资源地址不存在，请检查!"), QMessageBox.Ok)
            if reply == QMessageBox.Ok:
                # sys.exit(0)
                return False
        return True

    def start(self):
        # 将修改的状态进行保存和同步
        state = self.synch_config()
        if not state:
            return False
        self.save_config()
        self.resultEditor.setPlainText("")

        # 检查音乐表中相关资源是否存在
        if self.check_assetbundle.isChecked():
            result = music.process_assetbundle()
            self.resultEditor.append("Dance.txt文件检查结果：" + str(result[0]) + "\n安卓平台动作文件检查结果：" + str(result[1])
                                     + "\niOS平台动作文件检查结果：" + str(result[2]))

        if self.check_music.isChecked():
            result = music.process_music_smp()
            if len(result) == 0:
                self.resultEditor.append("icon和音乐资源名称配置检查结果：[]\nsmp/sog音乐资源文件检查结果：[]")
            else:
                if 'icon' in result.keys():
                    self.resultEditor.append("音乐表sheet音乐icon配置检查结果：" + str(result['icon']))
                if 'musicfile' in result.keys():
                    self.resultEditor.append("音乐表sheet音乐资源名称配置检查结果：" + str(result['musicfile']))
                if 'smp' in result.keys():
                    self.resultEditor.append("音乐smp文件检查结果：" + str(result['smp']))
                if 'sog' in result.keys():
                    self.resultEditor.append("音乐sog文件检查结果：" + str(result['sog']))

        if self.check_stage.isChecked():
            result = music.process_stage()
            self.resultEditor.append("安卓平台stage文件文件检查结果：" + str(result[0]) +
                                     "\niOS平台stage文件文件检查结果：" + str(result[1]))

        # 检查其他功能模块中配置的歌曲信息在音乐表中是否存在
        if self.check_dama.isChecked():
            xls = os.getcwd() + "\\Config\\广场舞大妈.xlsx"
            if not os.path.exists(xls):
                reply = QMessageBox.critical(self, "提示", self.tr("广场舞大妈.xlsx不存在，请检查!"), QMessageBox.Ok)
                if reply == QMessageBox.Ok:
                    return False
            result = music.process_dama(xls)
            self.resultEditor.append("广场舞大妈.xlsx检查结果：" + str(result))

        if self.check_fairlyland.isChecked():
            xls = os.getcwd() + "\\Config\\舞团秘境.xlsx"
            if not os.path.exists(xls):
                reply = QMessageBox.critical(self, "提示", self.tr("舞团秘境.xlsx不存在，请检查!"), QMessageBox.Ok)
                if reply == QMessageBox.Ok:
                    return False
            result = music.process_fairlyland(xls)
            self.resultEditor.append("舞团秘境.xlsx检查结果：" + str(result))

        if self.check_lwstar.isChecked():
            xls = os.getcwd() + "\\Config\\恋舞之星.xlsx"
            if not os.path.exists(xls):
                reply = QMessageBox.critical(self, "提示", self.tr("恋舞之星.xlsx不存在，请检查!"), QMessageBox.Ok)
                if reply == QMessageBox.Ok:
                    return False
            result = music.process_lwstar(xls)
            self.resultEditor.append("恋舞之星.xlsx检查结果：" + str(result))

        if self.check_magiclamp.isChecked():
            xls = os.getcwd() + "\\Config\\魔法神灯.xlsx"
            if not os.path.exists(xls):
                reply = QMessageBox.critical(self, "提示", self.tr("魔法神灯.xlsx.xlsx不存在，请检查!"), QMessageBox.Ok)
                if reply == QMessageBox.Ok:
                    return False
            result = music.process_magiclamp(xls)
            self.resultEditor.append("魔法神灯.xlsx-主线关卡检查结果：" + str(result[0]) +
                                     "\n魔法神灯.xlsx-主题关卡检查结果：" + str(result[1]))

        if self.check_diamondleague.isChecked():
            xls = os.getcwd() + "\\Config\\钻石联赛.xlsx"
            if not os.path.exists(xls):
                reply = QMessageBox.critical(self, "提示", self.tr("钻石联赛.xlsx不存在，请检查!"), QMessageBox.Ok)
                if reply == QMessageBox.Ok:
                    return False
            result = music.process_diamondleague(xls)
            self.resultEditor.append("钻石联赛.xlsx检查结果：" + str(result))

        if self.check_quest.isChecked():
            xml = os.getcwd() + "\\Config\\quest.xml"
            if not os.path.exists(xml):
                reply = QMessageBox.critical(self, "提示", self.tr("quest.xml不存在，请检查!"), QMessageBox.Ok)
                if reply == QMessageBox.Ok:
                    return False
            result = music.process_quest(xml)
            self.resultEditor.append("quest.xml检查结果：" + str(result))

        if self.check_musicrank.isChecked():
            xls = os.getcwd() + "\\Config\\音悦榜.xlsx"
            if not os.path.exists(xls):
                reply = QMessageBox.critical(self, "提示", self.tr("音悦榜.xlsx不存在，请检查!"), QMessageBox.Ok)
                if reply == QMessageBox.Ok:
                    return False
            result = music.process_musicrank(xls)
            self.resultEditor.append("音悦榜.xlsx检查结果：" + str(result))

        if self.check_starmentor.isChecked():
            xls = os.getcwd() + "\\Config\\星恋挑战.xlsx"
            if not os.path.exists(xls):
                reply = QMessageBox.critical(self, "提示", self.tr("星恋挑战.xlsx不存在，请检查!"), QMessageBox.Ok)
                if reply == QMessageBox.Ok:
                    return False
            result = music.process_starmentor(xls)
            self.resultEditor.append("星恋挑战.xlsx检查结果：" + str(result))

        # 检查结束，弹出检查完成提示框
        QMessageBox.information(self, "提示", self.tr("音乐检查完成!"), QMessageBox.Ok)
        return True


if __name__ == '__main__':
    music = CheckMusic()
    app = QApplication(sys.argv)
    ex = MainUi()
    ex.show()
    sys.exit(app.exec_())
