# _*_ coding: utf-8 _*_

__author__ = "joyce"

import configparser


class ConfigReader(object):
    def __init__(self, path):
        self.CReader = configparser.ConfigParser()
        self.CReader.read(path, encoding='utf8')

    def getSection(self):
        return self.CReader.sections()

    def getdic(self, section):
        s = {}
        for k, v in self.CReader.items(section):
            s[k] = v
        return s

    def setdic(self, section, option, value):
        # 修改配置文件
        # set(section,option,value)：对section中的option信息进行写入
        self.CReader.set(section, option, value)

    def addsection(self, section):
        # add_section()：添加一个新的section
        self.CReader.add_section(section)

    def removeoption(self, option, value):
        # remove_option(option,value) 删除某个section下的option的数值
        self.CReader.remove_option(option, value)

    def removesection(self, section):
        # remove_section(section)  删除某个section的数值
        self.CReader.remove_section(section)
