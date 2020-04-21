from .. import constants as c
from .monster import *

import os
import json
# 根据参数创建生物
# pos(行，列）

class CreatureList():
    def __init__(self):
        self.mons_path = os.path.join("source", "data", "monster.json")
        self.ar_list = {}
        self.creature_list = []
        # 初始化
        self.init_arlist()

    def init_arlist(self):
        with open(self.mons_path, "r") as f:
            self.ar_list = json.load(f)

    def init_layer_mons(self, layer):
        # 获取当前该图层信息
        h_g = len(layer)
        w_g = len(layer[0])

        # 代表当层的所有怪物的list
        mons_list = []
        for j in range(h_g):
            for i in range(w_g):
                if layer[j][i] == c.MAP_MONS_SG:
                    # m_pos中i为列，j为行
                    mons = Slime(self.ar_list["slime_green"])
                    m_pos = (j, i)
                    mons_list.append([m_pos, mons])
                elif layer[j][i] == c.MAP_MONS_SR:
                    mons = Slime(self.ar_list["slime_red"])
                    m_pos = (j, i)
                    mons_list.append([m_pos, mons])
                elif layer[j][i] == c.MAP_MONS_SB:
                    mons = Slime(self.ar_list["slime_black"])
                    m_pos = (j, i)
                    mons_list.append([m_pos, mons])
                elif layer[j][i] == c.MAP_MONS_BATF:
                    mons = Bat(self.ar_list["bat_first"])
                    m_pos = (j, i)
                    mons_list.append([m_pos, mons])
                elif layer[j][i] == c.MAP_MONS_BATS:
                    mons = Bat(self.ar_list["bat_second"])
                    m_pos = (j, i)
                    mons_list.append([m_pos, mons])
                elif layer[j][i] == c.MAP_MONS_BATT:
                    mons = Bat(self.ar_list["bat_third"])
                    m_pos = (j, i)
                    mons_list.append([m_pos, mons])
                elif layer[j][i] == c.MAP_MONS_SKULLF:
                    mons = Skull(self.ar_list["skull_first"])
                    m_pos = (j, i)
                    mons_list.append([m_pos, mons])
                elif layer[j][i] == c.MAP_MONS_SKULLS:
                    mons = Skull(self.ar_list["skull_second"])
                    m_pos = (j, i)
                    mons_list.append([m_pos, mons])
                elif layer[j][i] == c.MAP_MONS_SKULLT:
                    mons = Skull(self.ar_list["skull_third"])
                    m_pos = (j, i)
                    mons_list.append([m_pos, mons])
                elif layer[j][i] == c.MAP_MONS_MUMMYF:
                    mons = Mummy(self.ar_list["mummy_first"])
                    m_pos = (j, i)
                    mons_list.append([m_pos, mons])
                elif layer[j][i] == c.MAP_MONS_WZF:
                    mons = Wizard(self.ar_list["wizard_first"])
                    m_pos = (j, i)
                    mons_list.append([m_pos, mons])
                elif layer[j][i] == c.MAP_MONS_WZS:
                    mons = Wizard(self.ar_list["wizard_second"])
                    m_pos = (j, i)
                    mons_list.append([m_pos, mons])
                elif layer[j][i] == c.MAP_MONS_NIGHTF:
                    mons = Knight(self.ar_list["night_first"])
                    m_pos = (j, i)
                    mons_list.append([m_pos, mons])
                elif layer[j][i] == c.MAP_MONS_GUARDF:
                    mons = Guard(self.ar_list["guard_first"])
                    m_pos = (j, i)
                    mons_list.append([m_pos, mons])
                elif layer[j][i] == c.MAP_MONS_STONEM:
                    mons = StoneM(self.ar_list["stonem_first"])
                    m_pos = (j, i)
                    mons_list.append([m_pos, mons])
                elif layer[j][i] == c.MAP_MONS_SLIMEH:
                    mons = SlimeHuman(self.ar_list["slimehuman_first"])
                    m_pos = (j, i)
                    mons_list.append([m_pos, mons])

        self.creature_list.append(mons_list)


    # 查找怪物,返回该层怪物列表中的索引号
    def find_mons(self, index, pos):
        mons_list = self.creature_list[index]
        for pos_mons in mons_list:
            if pos_mons[0] == pos:
                return mons_list.index(pos_mons)

    # index当前图层索引值，pos怪物所在位置,pos(行，列）
    def delete_mons(self, index, pos):
        mons_list = self.creature_list[index]
        i = self.find_mons(index, pos)

        if i is None:
            print("find_mons problem")
        else:
            mons_list.pop(i)

    def get_mons(self, index, pos):
        mons_list = self.creature_list[index]
        i = self.find_mons(index, pos)
        pos_mons = mons_list[i]
        return pos_mons[1]