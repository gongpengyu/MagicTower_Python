from .com.map import Map
from .com.hero import Hero
from .shower import Shower
from .com.creature import CreatureList
from . import constants as c
from .tool import Tool
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
        # 指示主角朝向
        self.key_direct = None
        # 判断战斗事件是否结束
        self.attack_event = False


class Control(State):
    def __init__(self):
        State.__init__(self)

    # 初始化状态
    def init_State(self):
        # 逻辑数据
        self.done = True
        self.now_map = Map()
        self.now_hero = Hero()
        self.pos = [6, 12]
        self.mons_list = CreatureList()
        self.mons_list.init_layer_creature(self.now_map.now_layer())

        self.now_shower = Shower()
        # 绑定用于展示的数据
        self.now_shower.init_shower(self.now_map.now_layer(), self.now_hero, self.now_hero.ITEMS)
        self.key_direct = c.KEY_UP

    # 角色的状态检测
    def to_touch(self):
        data = self.now_map.now_layer()
        pos = self.pos
        h_g = len(data)
        w_g = len(data[0])
        key = self.key_direct

        if key == c.KEY_UP:
            if (pos[1]-1 < 0) or (data[pos[1]-1][pos[0]] == c.MAP_W_STONE):
                self.to_stop()
                return c.KEY_STOP
            elif data[pos[1]-1][pos[0]] == c.MAP_B_STONE:
                self.to_move()
                return c.KEY_UP
            elif data[pos[1]-1][pos[0]] >= c.MAP_MONS_SG and data[pos[1]-1][pos[0]] <= c.MAP_MONS_M:
                m_pos = (pos[1]-1, pos[0])
                mons = self.mons_list.get_mons(self.now_map.get_now_index(), m_pos)
                self.to_attack(mons, m_pos)
                return c.KEY_TOATK
            elif data[pos[1]-1][pos[0]] == c.MAP_NPC_RED:
                n_pos = (pos[1]-1, pos[0])
                self.to_trade(n_pos)
                return c.KEY_TRADE
            elif data[pos[1]-1][pos[0]] == c.MAP_IRON_RAIL:
                e_pos = [pos[1]-1, pos[0]]
                self.to_open(e_pos)
            elif data[pos[1]-1][pos[0]] == c.MAP_UP_FLO:
                self.to_up()
        elif key == c.KEY_DOWN:
            if (pos[1]+1 >= h_g) or (data[pos[1]+1][pos[0]] == c.MAP_W_STONE):
                self.to_stop()
                return c.KEY_STOP
            elif data[pos[1]+1][pos[0]] == c.MAP_B_STONE:
                self.to_move()
                return c.KEY_DOWN
            elif data[pos[1]+1][pos[0]] == c.MAP_MONS_SG and data[pos[1]+1][pos[0]] <= c.MAP_MONS_M:
                m_pos = (pos[1]+1, pos[0])
                mons = self.mons_list.get_mons(self.now_map.get_now_index(), m_pos)
                self.to_attack(mons, m_pos)
                return c.KEY_TOATK
            elif data[pos[1]+1][pos[0]] == c.MAP_NPC_RED:
                n_pos = (pos[1]+1, pos[0])
                self.to_trade(n_pos)
                return c.KEY_TRADE
            elif data[pos[1]+1][pos[0]] == c.MAP_IRON_RAIL:
                e_pos = [pos[1]+1, pos[0]]
                self.to_open(e_pos)
            elif data[pos[1]+1][pos[0]] == c.MAP_UP_FLO:
                self.to_up()
        elif key == c.KEY_LEFT:
            if (pos[0]-1 < 0) or (data[pos[1]][pos[0]-1] == c.MAP_W_STONE):
                self.to_stop()
                return c.KEY_STOP
            elif data[pos[1]][pos[0]-1] == c.MAP_B_STONE:
                self.to_move()
                return c.KEY_LEFT
            elif data[pos[1]][pos[0]-1] == c.MAP_MONS_SG and data[pos[1]][pos[0]-1] <= c.MAP_MONS_M:
                m_pos = (pos[1], pos[0]-1)
                mons = self.mons_list.get_mons(self.now_map.get_now_index(), m_pos)
                self.to_attack(mons, m_pos)
                return c.KEY_TOATK
            elif data[pos[1]][pos[0]-1] == c.MAP_NPC_RED:
                n_pos = (pos[1], pos[0]-1)
                self.to_trade(n_pos)
                return c.KEY_TRADE
            elif data[pos[1]][pos[0]-1] == c.MAP_IRON_RAIL:
                e_pos = [pos[1], pos[0]-1]
                self.to_open(e_pos)
            elif data[pos[1]][pos[0]-1] == c.MAP_UP_FLO:
                self.to_up()
        elif key == c.KEY_RIGHT:
            if (pos[0]+1 >= w_g) or (data[pos[1]][pos[0]+1] == c.MAP_W_STONE):
                self.to_stop()
                return c.KEY_STOP
            elif data[pos[1]][pos[0]+1] == c.MAP_B_STONE:
                self.to_move()
                return c.KEY_RIGHT
            elif data[pos[1]][pos[0]+1] == c.MAP_MONS_SG and data[pos[1]][pos[0]+1] <= c.MAP_MONS_M:
                m_pos = (pos[1], pos[0]+1)
                mons = self.mons_list.get_mons(self.now_map.get_now_index(), m_pos)
                self.to_attack(mons, m_pos)
                return c.KEY_TOATK
            elif data[pos[1]][pos[0]+1] == c.MAP_NPC_RED:
                n_pos = (pos[1], pos[0]+1)
                self.to_trade(n_pos)
                return c.KEY_TRADE
            elif data[pos[1]][pos[0]+1] == c.MAP_IRON_RAIL:
                e_pos = [pos[1], pos[0]+1]
                self.to_open(e_pos)
            elif data[pos[1]][pos[0]+1] == c.MAP_UP_FLO:
                self.to_up()
    # 控制角色的移动
    def to_move(self):
        key = self.key_direct

        # 先绘制走路动画
        for i in range(4):
            self.now_shower.fresh_layer()
            self.now_shower.fresh_walk(self.pos, key, i)
            pg.time.delay(200)
            pg.display.update(c.ACT_RECT)

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
    def to_stop(self):
        print("to stop")

    # 角色攻击,pos怪物的位置
    def to_attack(self, mons, pos):
        self.attack_event = True

        # 展示战斗面板
        self.now_shower.fresh_atk_pane(mons, self.now_hero)
        pg.display.update()

        # 开始战斗
        hero = self.now_hero
        # 确定先攻权,true为hero->mons,false为mons->hero
        atk_direct = None
        if hero.AGI >= mons.AGI:
            atk_direct = True
        else:
            atk_direct = False
        # 开始攻击，直到一方血条为0
        while self.attack_event:
            if hero.HP > 0 and mons.HP > 0:
                if atk_direct:
                    hero.attack(mons)
                    atk_direct = not atk_direct
                else:
                    mons.attack(hero)
                    atk_direct = not atk_direct
            print("hero_hp:", hero.HP, "mons_hp:", mons.HP)
            self.now_shower.fresh_atk_pane(mons, self.now_hero)
            pg.time.delay(200)
            pg.display.update()

            # 监测键盘事件
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    keys = pg.key.get_pressed()
                    if keys[pg.K_SPACE]:
                        print("you print enter")
                        self.attack_event = False

        # 处理战败的对象
        if mons.HP <= 0:
            self.mons_list.delete_mons(self.now_map.get_now_index(), pos)
            # 修改地图映射
            self.now_map.update_layer(pos, c.MAP_B_STONE)

            # 刷新图层
            self.now_shower.draw_sta_pane()
            self.now_shower.fresh_hero_atr()
            self.now_shower.fresh_item()
            self.now_shower.fresh_layer()
            self.now_shower.fresh_hero(self.pos, self.key_direct)
            pg.display.update()

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
        door_type = self.now_map.get_value_nowlayer(e_pos)
        if door_type == c.MAP_IRON_RAIL:
            # 开门动画
            for i in range(4):
                self.now_shower.fresh_layer()
                self.now_shower.fresh_hero(self.pos, self.key_direct)
                self.now_shower.fresh_open(Tool.change_xy_pos(e_pos), door_type, i)
                pg.time.delay(200)
                pg.display.update(c.ACT_RECT)

        # 更新地图数据
        self.now_map.update_layer(e_pos, c.MAP_B_STONE)

    # 楼层移动
    def to_up(self):
        # 强行让主角沿着该方向移动一步
        self.to_move()
        # 接着跳转下一层
        print("next layer")
        next_l = self.now_map.next_layer()
        # 更新shower的数据
        self.now_shower.set_data(next_l)
        self.now_shower.l_count = Tool.animate_count(4)
        # 更新mons_list的数据
        self.mons_list.init_layer_creature(self.now_map.now_layer())
        print("test")



    # 动态监测键盘事件
    def event_loop(self):
        self.now_shower.fresh_layer()
        self.now_shower.fresh_hero(self.pos, self.key_direct)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = False
            elif event.type == pg.KEYDOWN:
                print("keydown")
                keys = pg.key.get_pressed()
                if pg.key.get_pressed():
                    if keys[pg.K_UP]:
                        self.key_direct = c.KEY_UP
                        self.to_touch()
                    elif keys[pg.K_DOWN]:
                        self.key_direct = c.KEY_DOWN
                        self.to_touch()
                    elif keys[pg.K_LEFT]:
                        self.key_direct = c.KEY_LEFT
                        self.to_touch()
                    elif keys[pg.K_RIGHT]:
                        self.key_direct = c.KEY_RIGHT
                        self.to_touch()

        pg.time.delay(200)
        pg.display.update()

    def main(self):
        # 主要运行函数
        self.init_State()
        # 绘制静态层
        self.now_shower.draw_sta_pane()
        self.now_shower.fresh_hero_atr()
        self.now_shower.fresh_item()
        pg.display.update()

        # 动态绘制
        while self.done:
            self.event_loop()