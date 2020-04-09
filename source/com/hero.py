from . import items

# 负责主角的逻辑处理
class Hero():
    def __init__(self):
        self.LV = 1
        self.HP = 1000
        self.ATK = 10
        self.DEF = 10
        self.AGI = 2
        self.EXP = 0
        self.ITEMS = {
            "y_key": 1,
            "b_key": 1,
            "r_key": 1,
            "coin": 1
        }

    def attack(self, monster):
        # 计算造成的实际伤害
        damage = self.ATK - monster.DEF
        # 追加伤害
        monster.HP = monster.HP - damage

    def get_item(self, item_dict):
        self.ITEMS[item_dict["name"]] = item_dict
    def use_item(self, item_name):
        t_item = self.ITEMS[item_name]
        # 确定使用那种效果
        if t_item["exist"]:
            # 非快消品，另外考虑
            pass
        else:
            # 快消品直接使用
            for key in t_item:
                if key == "add_hp":
                    # 加血
                    self.HP += t_item[key]
                elif key == "add_atk":
                    # 加atk
                    self.ATK += t_item[key]
                elif key == "add_def":
                    # 加def
                    self.DEF += t_item[key]
                elif key == "add_agi":
                    # 加agi
                    self.AGI += t_item[key]

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




