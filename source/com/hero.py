from . import items
from .. import constants as c


import random
# 负责主角的逻辑处理
class Hero():
    def __init__(self):
        self.NAME = "steve"
        self.LV = 1
        self.HP = 10000
        self.ATK = 10
        self.DEF = 10
        self.AGI = 2
        self.EXP = 0
        self.STATE = c.HERO_STA["normal"]
        self.ITEMS = {
            "y_key": 1,
            "b_key": 1,
            "r_key": 1,
            "coin": 100
        }
        self.temp_data = {}

    def attack(self, monster):
        # 根据根据二者敏捷度进行判断，如果hero敏捷大于怪物，其回避率为其敏捷值
        if monster.AGI > self.AGI:
            avoid = monster.AGI
        else:
            avoid = 0

        # 根据回避率来计算是否承受伤害
        rand = random.randint(0, 100)
        if 0 <= rand <= avoid:
            damage = 0
        else:
            if self.ATK < monster.DEF:
                damage = 0
            else:
                damage = (self.ATK - monster.DEF)
                damage = round(damage)

        # 追加伤害
        monster.HP = monster.HP - damage

    # 当主距处于weak状态,下降自身攻击力、防御的10%
    def be_weak(self):
        if self.STATE != c.HERO_STA["weak"]:
            self.STATE = c.HERO_STA["weak"]
            self.temp_data["atk"] = self.ATK * 0.1
            self.temp_data["def"] = self.DEF * 0.1
            self.ATK -= self.temp_data["atk"]
            self.DEF -= self.temp_data["def"]
        else:
            print("jump")

    # 当主角处于poison状态下，每行一步扣自身1%血量，每加一步+1%
    def be_poison(self):
        if self.STATE != c.HERO_STA["poison"]:
            self.STATE = c.HERO_STA["poison"]
            self.temp_data["poi_add"] = 1
            self.HP = self.HP - (self.temp_data["poi_add"]/100)*self.HP
            self.HP = round(self.HP, 2)
        else:
            self.temp_data["poi_add"] += 1
            self.HP = self.HP - (self.temp_data["poi_add"]/100)*self.HP
            self.HP = round(self.HP, 2)


    # 角色正常化，部分状态可恢复
    def be_normal(self):
        if self.STATE == c.HERO_STA["weak"]:
            self.ATK += self.temp_data["atk"]
            self.DEF += self.temp_data["def"]
            # 清空临时数据
            self.temp_data["atk"] = None
            self.temp_data["def"] = None
        elif self.STATE ==c.HERO_STA["poison"]:
            self.temp_data["poi_add"] = None

        self.STATE = c.HERO_STA["normal"]

    # name表示从商店购买的货物名称
    def use_trade_item(self, name):
        if name == "red_gem":
            self.use_item(items.ITEM_RED_GEM)
        elif name == "blue_gem":
            self.use_item(items.ITEM_BLUE_GEM)

    def use_item(self, item_dict):
        # 记录效果
        txt = ""
        # 确定使用那种效果
        if item_dict["exist"]:
            # 非快消品，另外考虑
            pass
        else:
            # 快消品直接使用
            for key in item_dict:
                if key == "add_hp":
                    # 加血
                    self.HP += item_dict[key]
                    txt = txt + key + ": " + str(item_dict[key]) + ";"
                elif key == "add_atk":
                    # 加atk
                    self.ATK += item_dict[key]
                    txt = txt + key + ": " + str(item_dict[key]) + ";"
                elif key == "add_def":
                    # 加def
                    self.DEF += item_dict[key]
                    txt = txt + key + ": " + str(item_dict[key]) + ";"
                elif key == "add_agi":
                    # 加agi
                    self.AGI += item_dict[key]
                    txt = txt + key + ": " + str(item_dict[key]) + ";"
        return txt

    def print_hero(self):
        print("hp:", self.HP)
        print("level:", self.LV)
        print("atk:",self.ATK)
        print("def:",self.DEF)
        print("agi:",self.AGI)
        print("EXP:",self.EXP)
        print("Items:")
        for key in self.ITEMS:
            print(self.ITEMS[key])




