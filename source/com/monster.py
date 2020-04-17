import random
from .. import constants as c

# 处理怪物相关的逻辑
class Monster():
    def __init__(self, hp, atk, defend, agi):
        self.HP = hp
        self.ATK = atk
        self.DEF = defend
        self.AGI = agi

    def attack(self, hero):
        pass
    def give_item(self, hero):
        pass

class Slime(Monster):
    def __init__(self, m_dict):
        Monster.__init__(self, m_dict["hp"], m_dict["atk"], m_dict["defend"], m_dict["agi"])
        self.NAME = m_dict["name"]
        self.ITEMS = {
            "exp": m_dict["exp"],
            "coin": m_dict["coin"]
        }

    # def sayHello(self):
    #     print("hp:",self.HP,"atk:",self.ATK)
    #     print("hello, I'm Slime")
    def attack(self, hero):
        # 先计算slime造成的实际伤害
        damage = (self.ATK - hero.DEF)
        damage = round(damage)
        # 对hero进行伤害计算
        hero.HP = hero.HP - damage

    def give_items(self, hero):
        # 将怪物身上物品交与主角
        hero.EXP += self.ITEMS["exp"]
        hero.ITEMS["coin"] += self.ITEMS["coin"]


class Bat(Monster):
    def __init__(self, m_dict):
        Monster.__init__(self, m_dict["hp"], m_dict["atk"], m_dict["defend"], m_dict["agi"])
        self.NAME = m_dict["name"]
        self.ITEMS = {
            "exp": m_dict["exp"],
            "coin": m_dict["coin"]
        }

    def attack(self, hero):
        # 根据根据二者敏捷度进行判断，如果hero敏捷大于怪物，其回避率为其敏捷值
        if hero.AGI >= self.AGI:
            avoid = hero.AGI
        else:
            avoid = 0

        # 根据回避率来计算是否承受伤害
        rand = random.randint(0, 100)
        if 0 <= rand <= avoid:
            damage = 0
        else:
            if self.ATK < hero.DEF:
                damage = 0
            else:
                damage = (self.ATK - hero.DEF)
                damage = round(damage)

        # 对hero进行伤害计算
        hero.HP = hero.HP - damage

    def give_items(self, hero):
        # 将怪物身上物品交与主角
        hero.EXP += self.ITEMS["exp"]
        hero.ITEMS["coin"] += self.ITEMS["coin"]


class Skull(Monster):
    def __init__(self, m_dict):
        Monster.__init__(self, m_dict["hp"], m_dict["atk"], m_dict["defend"], m_dict["agi"])
        self.NAME = m_dict["name"]
        self.WEAK_HIT = m_dict["weak_hit"]
        self.ITEMS = {
            "exp": m_dict["exp"],
            "coin": m_dict["coin"]
        }

    def attack(self, hero):
        # 先算回避值
        if hero.AGI >= self.AGI:
            avoid = hero.AGI
        else:
            avoid = 0

        # weak_hit的单位为百分比
        if random.randint(0, 100) >= self.WEAK_HIT:
            # 虚弱没命中
            print("weak don't hit")
        else:
            # 虚弱命中
            hero.be_weak()

        # 根据回避计算伤害
            # 根据回避率来计算是否承受伤害
        if random.randint(0, 100) > avoid:
            if self.ATK < hero.DEF:
                damage = 0
            else:
                damage = (self.ATK - hero.DEF)
                damage = round(damage)
        else:
            damage = 0

        # 对hero进行伤害计算
        hero.HP = hero.HP - damage

    def give_items(self, hero):
        # 将怪物身上物品交与主角
        hero.EXP += self.ITEMS["exp"]
        hero.ITEMS["coin"] += self.ITEMS["coin"]

class Mummy(Monster):
    def __init__(self, m_dict):
        Monster.__init__(self, m_dict["hp"], m_dict["atk"], m_dict["defend"], m_dict["agi"])
        self.NAME = m_dict["name"]
        self.POI_HIT = m_dict["poison_hit"]
        self.ITEMS = {
            "exp": m_dict["exp"],
            "coin": m_dict["coin"]
        }

    def attack(self, hero):
        # 先算回避值
        if hero.AGI >= self.AGI:
            avoid = hero.AGI
        else:
            avoid = 0

        # 计算是否poison击中
        if random.randint(0, 100) >= self.POI_HIT:
            # 虚弱没命中
            print("poison don't hit")
        else:
            # 虚弱命中
            print("poison")
            hero.be_poison()

        # 根据回避计算伤害
        # 根据回避率来计算是否承受伤害
        if random.randint(0, 100) > avoid:
            if self.ATK < hero.DEF:
                damage = 0
            else:
                damage = (self.ATK - hero.DEF)
                damage = round(damage)
        else:
            damage = 0

        # 对hero进行伤害计算
        hero.HP = hero.HP - damage

    def give_items(self, hero):
        # 将怪物身上物品交与主角
        hero.EXP += self.ITEMS["exp"]
        hero.ITEMS["coin"] += self.ITEMS["coin"]

