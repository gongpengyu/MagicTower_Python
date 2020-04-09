from .com.map import Map
from .com.hero import Hero
from .shower import Shower
from .com.creature import CreatureList
from . import constants as c
# state用于存储重要的状态
import pygame as pg

class State():
    def __init__(self):
        # 指示游戏是否结束,True开始运行，False运行结束
        self.done = False
        # 指示当前所在地图
        self.now_map = None
        # 代表当前主角状态
        self.now_hero = None
        # 代表主角在地图中位置（列，行）
        self.pos = None
        # 存储待战斗的怪物
        self.mons_list = None
        # 储存shower
        self.now_shower = None


class Control(State):
    def __init__(self):
        State.__init__(self)

    # 初始化状态
    def init_State(self):
        self.done = True
        self.now_map = Map()
        self.now_shower = Shower()
        self.now_hero = Hero()
        self.pos = [6, 12]
        self.mons_list = CreatureList()
        # 创建初始怪物
        self.mons_list.init_layer_creature(self.now_map.now_layer())

    # 角色的状态检测
    def to_touch(self, key):
        data = self.now_map.now_layer()
        pos = self.pos
        h_g = len(data)
        w_g = len(data[0])

        if key == c.KEY_UP:
            if (pos[1]-1 < 0) or (data[pos[1]-1][pos[0]] == c.MAP_W_STONE):
                self.to_stop(key)
                return c.KEY_STOP
            elif data[pos[1]-1][pos[0]] == c.MAP_B_STONE:
                self.to_move(key)
                return c.KEY_UP
            elif data[pos[1]-1][pos[0]] == c.MAP_MONS_SG:
                pos = (pos[1]-1, pos[0])
                mons = self.mons_list.get_mons(self.now_map.get_now_index(), pos)
                self.to_attack(mons, pos)
                return c.KEY_TOATK
            elif data[pos[1]-1][pos[0]] == c.MAP_NPC_RED:
                pos = (pos[1]-1, pos[0])
                self.to_trade(pos)
                return c.KEY_TRADE
            elif data[pos[1]-1][pos[0]] == c.MAP_IRON_RAIL:
                e_pos = [pos[1]-1, pos[0]]
                self.to_open(e_pos)
            elif data[pos[1]-1][pos[0]] == c.MAP_UP_FLO:
                self.to_up(key)
        elif key == c.KEY_DOWN:
            if (pos[1]+1 >= h_g) or (data[pos[1]+1][pos[0]] == c.MAP_W_STONE):
                self.to_stop(key)
                return c.KEY_STOP
            elif data[pos[1]+1][pos[0]] == c.MAP_B_STONE:
                self.to_move(key)
                return c.KEY_DOWN
            elif data[pos[1]+1][pos[0]] == c.MAP_MONS_SG:
                pos = (pos[1]+1, pos[0])
                mons = self.mons_list.get_mons(self.now_map.get_now_index(), pos)
                self.to_attack(mons, pos)
                return c.KEY_TOATK
            elif data[pos[1]+1][pos[0]] == c.MAP_NPC_RED:
                pos = (pos[1]+1, pos[0])
                self.to_trade(pos)
                return c.KEY_TRADE
            elif data[pos[1]+1][pos[0]] == c.MAP_IRON_RAIL:
                e_pos = [pos[1] + 1, pos[0]]
                self.to_open(e_pos)
            elif data[pos[1]+1][pos[0]] == c.MAP_UP_FLO:
                self.to_up(key)
        elif key == c.KEY_LEFT:
            if (pos[0]-1 < 0) or (data[pos[1]][pos[0]-1] == c.MAP_W_STONE):
                self.to_stop(key)
                return c.KEY_STOP
            elif data[pos[1]][pos[0]-1] == c.MAP_B_STONE:
                self.to_move(key)
                return c.KEY_LEFT
            elif data[pos[1]][pos[0]-1] == c.MAP_MONS_SG:
                pos = (pos[1], pos[0]-1)
                mons = self.mons_list.get_mons(self.now_map.get_now_index(), pos)
                self.to_attack(mons)
                return c.KEY_TOATK
            elif data[pos[1]][pos[0]-1] == c.MAP_NPC_RED:
                pos = (pos[1], pos[0]-1)
                self.to_trade(pos)
                return c.KEY_TRADE
            elif data[pos[1]][pos[0]-1] == c.MAP_IRON_RAIL:
                e_pos = [pos[1], pos[0]-1]
                self.to_open(e_pos)
            elif data[pos[1]][pos[0]-1] == c.MAP_UP_FLO:
                self.to_up(key)
        elif key == c.KEY_RIGHT:
            if (pos[0]+1 >= w_g) or (data[pos[1]][pos[0]+1] == c.MAP_W_STONE):
                self.to_stop(key)
                return c.KEY_STOP
            elif data[pos[1]][pos[0]+1] == c.MAP_B_STONE:
                self.to_move(key)
                return c.KEY_RIGHT
            elif data[pos[1]][pos[0]+1] == c.MAP_MONS_SG:
                pos = (pos[1], pos[0]+1)
                mons = self.mons_list.get_mons(self.now_map.get_now_index(), pos)
                self.to_attack(mons)
                return c.KEY_TOATK
            elif data[pos[1]][pos[0]+1] == c.MAP_NPC_RED:
                pos = (pos[1], pos[0]+1)
                self.to_trade(pos)
                return c.KEY_TRADE
            elif data[pos[1]][pos[0]+1] == c.MAP_IRON_RAIL:
                e_pos = [pos[1], pos[0]+1]
                self.to_open(e_pos)
            elif data[pos[1]][pos[0]+1] == c.MAP_UP_FLO:
                self.to_up(key)
    # 控制角色的移动
    def to_move(self, key):
        if key == c.KEY_UP:
            self.pos[1] -= 1
        elif key == c.KEY_DOWN:
            self.pos[1] += 1
        elif key == c.KEY_LEFT:
            self.pos[0] -= 1
        elif key == c.KEY_RIGHT:
            self.pos[0] += 1
        print(key, ":", self.pos)

    # 角色停止
    def to_stop(self, key):
        print(key, ":", self.pos)

    # 角色攻击
    def to_attack(self, mons, pos):
        hero = self.now_hero
        # 确定先攻权,true为hero->mons,false为mons->hero
        atk_direct = None
        if hero.AGI >= mons.AGI:
            atk_direct = True
        else:
            atk_direct = False
        # 开始攻击，直到一方血条为0
        while hero.HP > 0 and mons.HP > 0:
            if atk_direct:
                hero.attack(mons)
                atk_direct = not atk_direct
            else:
                mons.attack(hero)
                atk_direct = not atk_direct
            print("hero_hp:", hero.HP, "mons_hp:", mons.HP)

        # 处理战败的对象
        if mons.HP <= 0:
            self.mons_list.delete_mons(self.now_map.get_now_index(), pos)
            # 修改地图映射
            self.now_map.update_layer(pos, c.MAP_B_STONE)
            print("delete it")
        else:
            print("game over")


    # 角色交易
    def to_trade(self, pos):
        print("to trade")
        npc = self.mons_list.get_mons(self.now_map.get_now_index(), pos)
        npc.to_talk()
        print("finish trade")


    # 开机关
    def to_open(self, e_pos):
        print("open door")
        self.now_map.update_layer(e_pos, c.MAP_B_STONE)

    # 楼层移动
    def to_up(self, key):
        # 强行让主角沿着该方向移动一步
        self.to_move(key)
        # 接着跳转下一层
        print("next layer")
        self.now_map.next_layer()
        print("test")



    # 动态监测键盘事件
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = False
            elif event.type == pg.KEYDOWN:
                print("keydown")
                keys = pg.key.get_pressed()
                if pg.key.get_pressed():
                    if keys[pg.K_UP]:
                        self.to_touch(c.KEY_UP)
                    elif keys[pg.K_DOWN]:
                        self.to_touch(c.KEY_DOWN)
                    elif keys[pg.K_LEFT]:
                        self.to_touch(c.KEY_LEFT)
                    elif keys[pg.K_RIGHT]:
                        self.to_touch(c.KEY_RIGHT)

    def main(self):
        # 主要运行函数
        self.init_State()

        while self.done:
            self.event_loop()