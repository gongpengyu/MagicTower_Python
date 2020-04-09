
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

    # def sayHello(self):
    #     print("hp:",self.HP,"atk:",self.ATK)
    #     print("hello, I'm Slime")
    def attack(self, hero):
        # 先计算slime造成的实际伤害
        damage = (self.ATK - hero.DEF)
        # 对hero进行伤害计算
        hero.HP = hero.HP - damage

