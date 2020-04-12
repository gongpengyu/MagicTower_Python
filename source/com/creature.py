from .. import constants as c
from .monster import *
from .npc import *

import os
import json
# 根据参数创建生物
# pos(行，列）

class CreatureList():
    def __init__(self):
        self.mons_path = os.path.join("source", "data", "monster.json")
        self.npc_path = os.path.join("source", "data", "npc.json")
        self.ar_list = {}
        self.npc_list = {}
        self.creature_list = []
        # 初始化
        self.init_arlist()

    def init_arlist(self):
        with open(self.mons_path, "r") as f:
            self.ar_list = json.load(f)
        with open(self.npc_path, "r", errors="ignore") as f2:
            self.npc_list = json.load(f2)
            print("test")

    def init_layer_creature(self, layer):
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
                elif layer[j][i] == c.MAP_NPC_RED:
                    npc = Npc(self.npc_list["npc_red_1"])
                    n_pos = (j, i)
                    mons_list.append([n_pos, npc])
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