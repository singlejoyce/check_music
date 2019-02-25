# -*- coding: UTF-8 -*-
import os
import re

import sys

from logger import Logger
from configreader import *
import pandas as pd


__author__ = "joyce"


class CheckMusic(object):
    def __init__(self):
        self.mylogger = Logger(logger='CheckMusic').getlog()

        # 读取Config.ini中配置文件
        cofigini = os.getcwd() + "\\Config\\Config.ini"
        if not os.path.exists(cofigini):
            self.mylogger.error("Config.ini文件缺失!")
            exit()
        self.config = ConfigReader(cofigini)

        self.music_file_dir = self.config.getdic('fileDir')['music_file_dir']
        self.stage_dir = self.config.getdic('fileDir')['stage_dir']
        self.controller_txt_dir = self.config.getdic('fileDir')['controller_txt_dir']
        self.adb_assetbundle_file_dir = self.config.getdic('fileDir')['adb_assetbundle_file_dir']
        self.ios_assetbundle_file_dir = self.config.getdic('fileDir')['ios_assetbundle_file_dir']

        self.check_assetbundle = self.config.getdic('checkStatus')['check_assetbundle']
        self.check_musicsmp = self.config.getdic('checkStatus')['check_musicsmp']
        self.check_stage = self.config.getdic('checkStatus')['check_stage']
        self.check_fairlyland = self.config.getdic('checkStatus')['check_fairlyland']
        self.check_dama = self.config.getdic('checkStatus')['check_dama']
        self.check_magiclamp = self.config.getdic('checkStatus')['check_magiclamp']
        self.check_lwstar = self.config.getdic('checkStatus')['check_lwstar']
        self.check_starmentor = self.config.getdic('checkStatus')['check_starmentor']
        self.check_musicrank = self.config.getdic('checkStatus')['check_musicrank']
        self.check_diamondleague = self.config.getdic('checkStatus')['check_diamondleague']

        # 读取音乐表信息
        self.music = self.read_musicinfo_excel()
        self.song_list_from_music_xls = list(set(self.music['id_mode_level'].tolist()))

    def get_dance_txt_file(self, file_dir):
        # 获得Dance.txt文件路径
        L = []
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                # if os.path.splitext(file)[1] == '.jpeg':
                #     L.append(os.path.join(root, file))
                if file == "Dance.txt":
                    L.append(os.path.join(root, file))
        return L

    def get_music_smp_file(self, file_dir):
        # 获得音乐smp文件路径
        L = []
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                if file.find("song") != -1:
                    if os.path.splitext(file)[1] == '.smp':
                        L.append(os.path.join(root, file))
        return L

    def get_file_by_listdir(self, file_dir):
        L = []
        for file in os.listdir(file_dir):
            L.append(file)
        return L

    def get_file_by_walk(self, file_dir):
        L = []
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                L.append(os.path.join(root, file))
        return L

    def read_musicinfo_excel(self):
        # 模式id与模式对应的缩写转换
        modestr_dict = {
            1: 'tg',
            2: 'td',
            3: 'os',
            4: 'au',
            11: 'sg',
            12: 'sd',
            13: 'so',
            14: 'su',
            21: 'hb',
            5: 'rh',
            22: 'ig',
        }

        # 模式id与模式对应的全称转换
        mode_filename_dict = {
            1: "taigu",
            2: "tradition",
            3: "osu",
            4: "au",
            11: "taigu",
            12: "tradition",
            13: "osu",
            14: "au",
            21: "heartbeats",
            5: "rhythm",
            22: "taigu",
        }

        # 难度id与难度对应的缩写转换
        levelstr_dict = {
            1: 'e',
            2: 'n',
            3: 'h',
        }

        xls = os.getcwd() + '\\Config\\音乐表.xlsx'
        if not os.path.exists(xls):
            self.mylogger.error("音乐表.xlsx文件缺失!")
            sys.exit(0)
        df = pd.read_excel(xls, sheetname='关卡表')
        df['songid'] = df['歌曲ID'].apply(lambda x: str(x).zfill(4))
        df['modestr'] = df['模式ID'].apply(lambda x: modestr_dict.get(x))
        df['mode_filename'] = df['模式ID'].apply(lambda x: mode_filename_dict.get(x))
        df['levelstr'] = df['难度'].apply(lambda x: levelstr_dict.get(x))
        df['id_mode_level'] = df['歌曲ID'].map(str) + ',' + df['模式ID'].map(str) + ',' + df['难度'].map(str)
        df_new = df[['歌曲名', 'songid', 'modestr', 'mode_filename', 'levelstr', 'id_mode_level']]
        df_new.rename(columns={'歌曲名': 'name'}, inplace=True)
        df_new.reset_index(drop=True, inplace=True)
        # music_new.to_excel("result.xlsx", index=False)  # write data to excel
        return df_new

    def process_assetbundle(self):
        # 检查动作文件
        # 目标文件夹下已上传存在的Dance.txt文件列表
        dance_txt_list_from_dir = self.get_dance_txt_file(self.controller_txt_dir)
        self.music['dancetxt_file_dir'] = self.controller_txt_dir + "\\song" + self.music['songid'] + "\\Dance.txt"
        dance_txt_list_from_music_xls = list(set(self.music['dancetxt_file_dir'].tolist()))
        dance_txt_failed_file = list(set(dance_txt_list_from_music_xls).difference(set(dance_txt_list_from_dir)))
        if len(dance_txt_failed_file) != 0:
            self.mylogger.error("缺失的Dance.txt文件为：%s" % list(set(dance_txt_failed_file)))
        else:
            self.mylogger.info("Dance.txt文件未缺失！")

        # 目标文件夹下已上传存在的动作文件列表
        adb_assetbundle_list_from_dir = self.get_file_by_listdir(self.adb_assetbundle_file_dir)
        ios_assetbundle_list_from_dir = self.get_file_by_listdir(self.ios_assetbundle_file_dir)
        # 音乐表中必要的动作文件列表
        assetbundle_list_from_music_xls = []

        for dance_txt_file in dance_txt_list_from_dir:
            # mylogger.info("开始处理%s文件" % dance_txt_file)
            with open(dance_txt_file, encoding='utf-8') as f:  # 从Dance.txt文件中读出数据
                for line in f.readlines():
                    m = re.findall(r"Motion:\w+", line)  # 匹配含有字符'Motion:'的行
                    if m:
                        assetbundle_file_name = line.strip('\n').strip('\t').split(':')[1].upper() + ".assetbundle"
                        assetbundle_list_from_music_xls.append(assetbundle_file_name)

        # list(set(failed_file)) 对failed_file列表进行去重操作，去掉同名文件
        assetbundle_list_from_music_xls = list(set(assetbundle_list_from_music_xls))
        # 获取两个list的差集: list(set(b).difference(set(a))) # b中有而a中没有的      非常高效！
        adb_assetbundle_failed_file = list(
            set(assetbundle_list_from_music_xls).difference(set(adb_assetbundle_list_from_dir)))
        ios_assetbundle_failed_file = list(
            set(assetbundle_list_from_music_xls).difference(set(ios_assetbundle_list_from_dir)))

        if len(adb_assetbundle_failed_file) != 0:
            self.mylogger.error("安卓平台缺失的动作文件为：%s" % list(set(adb_assetbundle_failed_file)))
        else:
            self.mylogger.info("安卓平台动作文件未缺失！")
        if len(ios_assetbundle_failed_file) != 0:
            self.mylogger.error("iOS平台缺失的动作文件为：%s" % list(set(ios_assetbundle_failed_file)))
        else:
            self.mylogger.info("iOS平台动作文件未缺失！")
        return dance_txt_failed_file, adb_assetbundle_failed_file, ios_assetbundle_failed_file

    def process_stage(self):
        # 检查stage文件
        # 目标文件夹下已上传存在的stage文件列表
        adb_stage_list_from_dir = self.get_file_by_walk(self.stage_dir + "\\android\\")
        ios_stage_list_from_dir = self.get_file_by_walk(self.stage_dir + "\\ios\\")
        self.music['adb_stagefile_dir'] = self.stage_dir + "\\android\\" + self.music['mode_filename'] + "\\song" + self.music[
            'songid'] + "." + self.music['modestr'] + self.music['levelstr']
        self.music['ios_stagefile_dir'] = self.stage_dir + "\\ios\\" + self.music['mode_filename'] + "\\song" + self.music[
            'songid'] + "." + self.music['modestr'] + self.music['levelstr']
        adb_stage_list_from_music_xls = list(set(self.music['adb_stagefile_dir'].tolist()))
        ios_stage_list_from_music_xls = list(set(self.music['ios_stagefile_dir'].tolist()))
        # 获取两个 list 的差集
        adb_stage_failed_file = list(set(adb_stage_list_from_music_xls).difference(set(adb_stage_list_from_dir)))
        ios_stage_failed_file = list(set(ios_stage_list_from_music_xls).difference(set(ios_stage_list_from_dir)))

        if len(adb_stage_failed_file) != 0:
            self.mylogger.error("安卓平台缺失的stage文件为：%s" % list(set(adb_stage_failed_file)))
        else:
            self.mylogger.info("安卓平台stage文件未缺失！")
        if len(ios_stage_failed_file) != 0:
            self.mylogger.error("iOS平台缺失的stage文件为：%s" % list(set(ios_stage_failed_file)))
        else:
            self.mylogger.info("iOS平台stage文件未缺失！")
        return adb_stage_failed_file, ios_stage_failed_file

    def process_music_smp(self):
        # 检查Music目录下的songxxxx.smp文件
        # 目标文件夹下已上传存在的音乐smp文件列表
        music_file_list_from_dir = self.get_music_smp_file(self.music_file_dir)
        self.music['music_file_dir'] = self.music_file_dir + "\\song" + self.music['songid'] + ".smp"
        music_file_list_from_music_xls = list(set(self.music['music_file_dir'].tolist()))
        music_failed_file = list(set(music_file_list_from_music_xls).difference(set(music_file_list_from_dir)))
        if len(music_failed_file) != 0:
            self.mylogger.error("缺失的音乐资源smp文件为：%s" % list(set(music_failed_file)))
        else:
            self.mylogger.info("音乐资源smp文件未缺失！")
        return music_failed_file

    def process_dama(self, xls):
        dama = pd.read_excel(xls, sheetname='歌曲表')
        # .map(str)实现数据转换，强制转换为string型
        dama['id_mode_level'] = dama['歌曲ID'].map(str) + ',' + dama['模式ID'].map(str) + ',' + dama['难度'].map(str)
        dama_song_list = list(set(dama['id_mode_level'].tolist()))
        dama_failed_file = list(set(dama_song_list).difference(set(self.song_list_from_music_xls)))
        if len(dama_failed_file) != 0:
            self.mylogger.error("广场舞大妈.xlsx中在音乐表中不存在的歌曲信息：%s" % list(set(dama_failed_file)))
        else:
            self.mylogger.info("广场舞大妈.xlsx检查通过！")
        return dama_failed_file

    def process_lwstar(self, xls):
        lwstar = pd.read_excel(xls, sheetname='考核项')
        # 恋舞之星后面阶段为pvp不需要配置歌曲和模式，空值行需删除
        # axis: 维度，axis = 0表示index行, axis = 1表示columns列，默认为0
        # how: "all"表示这一行或列中的元素全部缺失（为nan）才删除这一行或列，
        # "any"表示这一行或列中只要有元素缺失，就删除这一行或列
        # thresh: 一行或一列中至少出现了thresh个才删除。
        # subset：在某些列的子集中选择出现了缺失值的列删除，不在子集中的含有缺失值得列或行不会删除（有axis决定是行还是列）
        # inplace：刷选过缺失值得新数据是存为副本还是直接在原数据上进行修改。
        lwstar.dropna(axis=0, how='any', thresh=None, subset=None, inplace=True)
        # 恋舞之星中格式为float64，需先转换为int型
        lwstar['歌曲ID'] = lwstar['歌曲ID'].map(int)
        lwstar['模式'] = lwstar['模式'].map(int)
        lwstar['难度'] = lwstar['难度'].map(int)
        # .map(str)实现数据转换，强制转换为string型
        lwstar['id_mode_level'] = lwstar['歌曲ID'].map(str) + ',' + lwstar['模式'].map(str) + ',' + lwstar['难度'].map(str)
        lwstar_song_list = list(set(lwstar['id_mode_level'].tolist()))
        lwstar_failed_file = list(set(lwstar_song_list).difference(set(self.song_list_from_music_xls)))
        if len(lwstar_failed_file) != 0:
            self.mylogger.error("恋舞之星.xlsx中在音乐表中不存在的歌曲信息：%s" % list(set(lwstar_failed_file)))
        else:
            self.mylogger.info("恋舞之星.xlsx检查通过！")
        return lwstar_failed_file

    def process_magiclamp(self, xls):
        magiclamp = pd.read_excel(xls, sheetname='主线关卡')
        # .map(str)实现数据转换，强制转换为string型
        magiclamp['id_mode_level'] = magiclamp['歌曲ID'].map(str) + ',' + magiclamp['歌曲模式'].map(str) + ',' + magiclamp[
            '歌曲难度'].map(str)
        magiclamp_song_list = list(set(magiclamp['id_mode_level'].tolist()))
        magiclamp_failed_file_line = list(set(magiclamp_song_list).difference(set(self.song_list_from_music_xls)))
        if len(magiclamp_failed_file_line) != 0:
            self.mylogger.error("魔法神灯.xlsx-主线关卡sheet中在音乐表中不存在的歌曲信息：%s" % list(set(magiclamp_failed_file_line)))
        else:
            self.mylogger.info("魔法神灯.xlsx-主线关卡sheet检查通过！")

        magiclamp = pd.read_excel(xls, sheetname='主题关卡')
        # .map(str)实现数据转换，强制转换为string型
        magiclamp['id_mode_level'] = magiclamp['歌曲ID'].map(str) + ',' + magiclamp['歌曲模式'].map(str) + ',' + magiclamp[
            '歌曲难度'].map(str)
        magiclamp_song_list = list(set(magiclamp['id_mode_level'].tolist()))
        magiclamp_failed_file_theme = list(set(magiclamp_song_list).difference(set(self.song_list_from_music_xls)))
        if len(magiclamp_failed_file_theme) != 0:
            self.mylogger.error("魔法神灯.xlsx-主题关卡sheet中在音乐表中不存在的歌曲信息：%s" % list(set(magiclamp_failed_file_theme)))
        else:
            self.mylogger.info("魔法神灯.xlsx-主题关卡sheet检查通过！")
        return magiclamp_failed_file_line, magiclamp_failed_file_theme

    def process_fairlyland(self, xls):
        fairlyland = pd.read_excel(xls, sheetname='FairlylandChapter')
        # .map(str)实现数据转换，强制转换为string型
        fairlyland['id_mode_level'] = fairlyland['MusicId'].map(str) + ',' + fairlyland['DanceType'].map(str) + ',' + \
                                      fairlyland['DifficultyLevel'].map(str)
        fairlyland_song_list = list(set(fairlyland['id_mode_level'].tolist()))
        fairlyland_failed_file = list(set(fairlyland_song_list).difference(set(self.song_list_from_music_xls)))
        if len(fairlyland_failed_file) != 0:
            self.mylogger.error("舞团秘境.xlsx中在音乐表中不存在的歌曲信息：%s" % list(set(fairlyland_failed_file)))
        else:
            self.mylogger.info("舞团秘境.xlsx检查通过！")
        return fairlyland_failed_file

    def process_starmentor(self, xls):
        starmentor = pd.read_excel(xls, sheetname='关卡')
        # .map(str)实现数据转换，强制转换为string型
        starmentor['id_mode_level'] = starmentor['歌曲ID'].map(str) + ',' + starmentor['歌曲模式'].map(str) + ',' + \
                                      starmentor['歌曲难度'].map(str)
        starmentor_song_list = list(set(starmentor['id_mode_level'].tolist()))
        starmentor_failed_file = list(set(starmentor_song_list).difference(set(self.song_list_from_music_xls)))
        if len(starmentor_failed_file) != 0:
            self.mylogger.error("星恋挑战.xlsx中在音乐表中不存在的歌曲信息：%s" % list(set(starmentor_failed_file)))
        else:
            self.mylogger.info("星恋挑战.xlsx检查通过！")
        return starmentor_failed_file

    def process_diamondleague(self, xls):
        diamondleague = pd.read_excel(xls, sheetname='活动时间')
        # .map(str)实现数据转换，强制转换为string型
        diamondleague['id_mode_level'] = diamondleague['歌曲ID'].map(str) + ',' + diamondleague['歌曲模式'].map(str) + ',' + \
                                         diamondleague['歌曲难度'].map(str)
        diamondleague_song_list = list(set(diamondleague['id_mode_level'].tolist()))
        diamondleague_failed_file = list(set(diamondleague_song_list).difference(set(self.song_list_from_music_xls)))
        if len(diamondleague_failed_file) != 0:
            self.mylogger.error("钻石联赛.xlsx中在音乐表中不存在的歌曲信息：%s" % list(set(diamondleague_failed_file)))
        else:
            self.mylogger.info("钻石联赛.xlsx检查通过！")
        return diamondleague_failed_file

    def process_musicrank(self, xls):
        musicrank = pd.read_excel(xls, sheetname='榜单模式')
        # .map(str)实现数据转换，强制转换为string型
        # 音悦榜默认歌曲难度为困难模式，id=3
        musicrank['id_mode_level'] = musicrank['歌曲ID'].map(str) + ',' + musicrank['模式ID'].map(str) + ',3'
        musicrank_song_list = list(set(musicrank['id_mode_level'].tolist()))
        musicrank_failed_file = list(set(musicrank_song_list).difference(set(self.song_list_from_music_xls)))
        if len(musicrank_failed_file) != 0:
            self.mylogger.error("音悦榜.xlsx中在音乐表中不存在的歌曲信息：%s" % list(set(musicrank_failed_file)))
        else:
            self.mylogger.info("音悦榜.xlsx检查通过！")
        return musicrank_failed_file



