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

class Slime(Monster):
    def __init__(self, dict):
        Monster.__init__(self, dict["hp"], dict["atk"], dict["defend"], dict["agi"])
        self.NAME = dict["name"]

    # def sayHello(self):
    #     print("hp:",self.HP,"atk:",self.ATK)
    #     print("hello, I'm Slime")
    def attack(self, hero):
        # 先计算slime造成的实际伤害
        damage = (self.ATK - hero.DEF)
        # 对hero进行伤害计算
        hero.HP = hero.HP - damage

class Bat(Monster):
    def __init__(self, dict):
        Monster.__init__(self, dict["hp"], dict["atk"], dict["defend"], dict["agi"])
        self.NAME = dict["name"]

    def attack(self, hero):
        # 根据根据二者敏捷度进行判断，如果hero敏捷大于怪物，其回避率为其敏捷值
        if hero.AGI >= self.AGI:
            avoid = hero.AGI
        else:
            avoid = 0

        # 根据回避率来计算是否承受伤害
        rand = random.randint(0, 100)
        if rand >= 0 and rand <= avoid:
            damage = 0
        else:
            damage = (self.ATK - hero.DEF)

        # 对hero进行伤害计算
        hero.HP = hero.HP - damage


class Skull(Monster):
    def __init__(self, m_dict):
        Monster.__init__(self, m_dict["hp"], m_dict["atk"], m_dict["defend"], m_dict["agi"])
        self.NAME = m_dict["name"]
        self.WEAK_HIT = m_dict["weak_hit"]

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
            hero.STATE = c.HERO_STA["weak"]

        # 根据回避计算伤害
            # 根据回避率来计算是否承受伤害
        if random.randint(0, 100) > avoid:
            damage = (self.ATK - hero.DEF)
        else:
            damage = 0

        # 对hero进行伤害计算
        hero.HP = hero.HP - damage



