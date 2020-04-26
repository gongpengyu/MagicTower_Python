__author__ = "scarecrow_gpy"

import random
from .. import constants as c

# 处理怪物相关的逻辑
class Monster():
    def __init__(self, m_dict):
        self.NAME = m_dict["name"]
        self.HP = m_dict["hp"]
        self.ATK = m_dict["atk"]
        self.DEF = m_dict["defend"]
        self.AGI = m_dict["agi"]
        self.ITEMS = {
            "exp": m_dict["exp"],
            "coin": m_dict["coin"]
        }
        self.SKIN_THICK = m_dict["skin_thick"]

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

class Slime(Monster):
    def __init__(self, m_dict):
        Monster.__init__(self, m_dict)

    # 继承父类
    # def attack(self, hero)
    # 继承父类
    # def give_items(self, hero)


class Bat(Monster):
    def __init__(self, m_dict):
        Monster.__init__(self, m_dict)

    # 继承父类
    # def attack(self, hero)
    # 继承父类
    # def give_items(self, hero)


class Skull(Monster):
    def __init__(self, m_dict):
        Monster.__init__(self, m_dict)
        self.WEAK_HIT = m_dict["weak_hit"]

    # rewrite
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

    # inherit
    # def give_items(self, hero)

class Mummy(Monster):
    def __init__(self, m_dict):
        Monster.__init__(self, m_dict)
        self.POI_HIT = m_dict["poison_hit"]

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

    # def give_items(self, hero)

# 魔法师的攻击,无视防御力
class Wizard(Monster):
    def __init__(self, m_dict):
        Monster.__init__(self, m_dict)

    def attack(self, hero):
        # 先算回避值
        if hero.AGI >= self.AGI:
            avoid = hero.AGI
        else:
            avoid = 0
        # 根据回避率来计算是否承受伤害
        if random.randint(0, 100) > avoid:
            if self.ATK < hero.DEF:
                damage = 0
            else:
                damage = self.ATK
                damage = round(damage)
        else:
            damage = 0
        # 对hero进行伤害计算
        hero.HP = hero.HP - damage

    # def give_items(self, hero)

# 骑士的攻击，无视敏捷
class Knight(Monster):
    def __init__(self, m_dict):
        Monster.__init__(self, m_dict)

    def attack(self, hero):
        # 直接伤害命中
        if self.ATK < hero.DEF:
            damage = 0
        else:
            damage = self.ATK
            damage = round(damage)

        # 对hero进行伤害计算
        hero.HP = hero.HP - damage

    # def give_items(self, hero)

# 守卫基本上就是防御力高
class Guard(Monster):
    def __init__(self, m_dict):
        Monster.__init__(self, m_dict)

    def attack(self, hero):
        # 先算回避值
        avoid = hero.AGI
        # 根据回避率来计算是否承受伤害
        if random.randint(0, 100) > avoid:
            if self.ATK < hero.DEF:
                damage = 1
            else:
                damage = self.ATK - hero.DEF
                damage = round(damage)
        else:
            damage = 0

        # 对hero进行伤害计算
        hero.HP = hero.HP - damage

    # def give_items(self, hero)

# 石怪的特性就是，当自身防御力低于hero时，伤害为1，当自身防御力高于hero时，defend当做atk使用
class StoneM(Monster):
    def __init__(self, m_dict):
        Monster.__init__(self, m_dict)

    def attack(self, hero):
        # 先算回避值
        avoid = hero.AGI
        # 根据回避率来计算是否承受伤害
        if random.randint(0, 100) > avoid:
            if self.ATK > hero.DEF:
                damage = self.ATK - hero.DEF
            else:
                damage = 1
        else:
            damage = 0

        # 对hero进行伤害计算
        hero.HP = hero.HP - damage

    # def give_items(self, hero)

class SlimeHuman(Monster):
    def __init__(self, m_dict):
        Monster.__init__(self, m_dict)

    # def attack(self, hero)
    # def get_items(self, hero)