from .com.map import Map
from .com.hero import Hero
from .shower import Shower
from .com.creature import CreatureList
from . import constants as c
from .tool import Tool
from .com import items
from .com.npc import NpcList
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
        # 存储npc的数据
        self.npc_list = None
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
        self.mons_list.init_layer_mons(self.now_map.now_layer())
        self.npc_list = NpcList()

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
            elif c.MAP_MONS_SG <= data[pos[1] - 1][pos[0]] <= c.MAP_MONS_M:
                m_pos = (pos[1]-1, pos[0])
                mons = self.mons_list.get_mons(self.now_map.get_now_index(), m_pos)
                self.to_attack(mons, m_pos)
                return c.KEY_TOATK
            elif c.MAP_NPC_RED <= data[pos[1]-1][pos[0]] <= c.MAP_NPC_M:
                n_pos = (pos[1]-1, pos[0])
                self.to_trade(n_pos)
                return c.KEY_TRADE
            elif c.MAP_IRON_RAIL <= data[pos[1]-1][pos[0]] <= c.MAP_DOOR_RED:
                e_pos = [pos[1]-1, pos[0]]
                self.to_open(e_pos)
            elif c.MAP_ITEM_RM <= data[pos[1]-1][pos[0]] <= c.MAP_ITEM_M:
                e_pos = [pos[1]-1, pos[0]]
                self.to_get_item(e_pos)
            elif data[pos[1]-1][pos[0]] == c.MAP_UP_FLO:
                self.to_up()
            elif data[pos[1]-1][pos[0]] == c.MAP_DOWN_FLO:
                self.to_down()
        elif key == c.KEY_DOWN:
            if (pos[1]+1 >= h_g) or (data[pos[1]+1][pos[0]] == c.MAP_W_STONE):
                self.to_stop()
                return c.KEY_STOP
            elif data[pos[1]+1][pos[0]] == c.MAP_B_STONE:
                self.to_move()
                return c.KEY_DOWN
            elif c.MAP_MONS_SG <= data[pos[1] + 1][pos[0]] <= c.MAP_MONS_M:
                m_pos = (pos[1]+1, pos[0])
                mons = self.mons_list.get_mons(self.now_map.get_now_index(), m_pos)
                self.to_attack(mons, m_pos)
                return c.KEY_TOATK
            elif c.MAP_NPC_RED <= data[pos[1] + 1][pos[0]] <= c.MAP_NPC_M:
                n_pos = (pos[1]+1, pos[0])
                self.to_trade(n_pos)
                return c.KEY_TRADE
            elif c.MAP_IRON_RAIL <= data[pos[1]+1][pos[0]] <= c.MAP_DOOR_RED:
                e_pos = [pos[1]+1, pos[0]]
                self.to_open(e_pos)
            elif c.MAP_ITEM_RM <= data[pos[1]+1][pos[0]] <= c.MAP_ITEM_M:
                e_pos = [pos[1]+1, pos[0]]
                self.to_get_item(e_pos)
            elif data[pos[1]+1][pos[0]] == c.MAP_UP_FLO:
                self.to_up()
            elif data[pos[1]+1][pos[0]] == c.MAP_DOWN_FLO:
                self.to_down()
        elif key == c.KEY_LEFT:
            if (pos[0]-1 < 0) or (data[pos[1]][pos[0]-1] == c.MAP_W_STONE):
                self.to_stop()
                return c.KEY_STOP
            elif data[pos[1]][pos[0]-1] == c.MAP_B_STONE:
                self.to_move()
                return c.KEY_LEFT
            elif c.MAP_MONS_SG <= data[pos[1]][pos[0] - 1] <= c.MAP_MONS_M:
                m_pos = (pos[1], pos[0]-1)
                mons = self.mons_list.get_mons(self.now_map.get_now_index(), m_pos)
                self.to_attack(mons, m_pos)
                return c.KEY_TOATK
            elif c.MAP_NPC_RED <= data[pos[1]][pos[0] - 1] <= c.MAP_NPC_M:
                n_pos = (pos[1], pos[0]-1)
                self.to_trade(n_pos)
                return c.KEY_TRADE
            elif c.MAP_IRON_RAIL <= data[pos[1]][pos[0]-1] <= c.MAP_DOOR_RED:
                e_pos = [pos[1], pos[0]-1]
                self.to_open(e_pos)
            elif c.MAP_ITEM_RM <= data[pos[1]][pos[0]-1] <= c.MAP_ITEM_M:
                e_pos = [pos[1], pos[0]-1]
                self.to_get_item(e_pos)
            elif data[pos[1]][pos[0]-1] == c.MAP_UP_FLO:
                self.to_up()
            elif data[pos[1]][pos[0]-1] == c.MAP_DOWN_FLO:
                self.to_down()
        elif key == c.KEY_RIGHT:
            if (pos[0]+1 >= w_g) or (data[pos[1]][pos[0]+1] == c.MAP_W_STONE):
                self.to_stop()
                return c.KEY_STOP
            elif data[pos[1]][pos[0]+1] == c.MAP_B_STONE:
                self.to_move()
                return c.KEY_RIGHT
            elif c.MAP_MONS_SG <= data[pos[1]][pos[0] + 1] <= c.MAP_MONS_M:
                m_pos = (pos[1], pos[0]+1)
                mons = self.mons_list.get_mons(self.now_map.get_now_index(), m_pos)
                self.to_attack(mons, m_pos)
                return c.KEY_TOATK
            elif c.MAP_NPC_RED <= data[pos[1]][pos[0] + 1] <= c.MAP_NPC_M:
                n_pos = (pos[1], pos[0]+1)
                self.to_trade(n_pos)
                return c.KEY_TRADE
            elif c.MAP_IRON_RAIL <= data[pos[1]][pos[0]+1] <= c.MAP_DOOR_RED:
                e_pos = [pos[1], pos[0]+1]
                self.to_open(e_pos)
            elif c.MAP_ITEM_RM <= data[pos[1]][pos[0]+1] <= c.MAP_ITEM_M:
                e_pos = [pos[1], pos[0]+1]
                self.to_get_item(e_pos)
            elif data[pos[1]][pos[0]+1] == c.MAP_UP_FLO:
                self.to_up()
            elif data[pos[1]][pos[0]+1] == c.MAP_DOWN_FLO:
                self.to_down()
    # 控制角色的移动
    def to_move(self):
        key = self.key_direct

        # 先绘制走路动画
        for i in range(4):
            self.now_shower.fresh_layer()
            self.now_shower.fresh_walk(self.pos, key, i)
            pg.time.delay(100)
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

        # 根据状态执行相应工作
        if self.now_hero.STATE == c.HERO_STA["normal"]:
            pass
        elif self.now_hero.STATE == c.HERO_STA["poison"]:
            self.now_hero.be_poison()
            # 刷新数据
            self.now_shower.fresh_hero_pane()
            pg.display.update()

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
            pg.time.delay(100)
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
            # 将战利品给予hero
            mons.give_items(hero)
            self.mons_list.delete_mons(self.now_map.get_now_index(), pos)
            # 修改地图映射
            self.now_map.update_layer(pos, c.MAP_B_STONE)
            print("delete it")
        else:
            print("game over")

        # 刷新图层
        self.now_shower.update_all(self.pos, self.key_direct)

    # 角色交易
    def to_trade(self, pos):
        print("to trade")
        self.npc_list.set_npc(self.now_map.get_now_index(), pos)
        npc_data = self.npc_list.now_npc

        if npc_data["n_items"] == "":
            print("just talk")
            self.npc_list.talk()
            # 展示talk面板
            self.now_shower.fresh_talk_pane(npc_data["word"])
            pg.display.update()

            talk_event = True
            while talk_event:
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        keys = pg.key.get_pressed()
                        if keys[pg.K_SPACE]:
                            print("you print enter")
                            talk_event = False

        else:
            self.npc_list.talk()
            self.now_shower.fresh_talk_pane(npc_data["word"])

            # 通过key事件控制,k_index指示位置
            trade_event = True
            k_index = 0
            while trade_event:
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        keys = pg.key.get_pressed()
                        if keys[pg.K_UP]:
                            if k_index - 1 < 0:
                                pass
                            else:
                                k_index -= 1
                        elif keys[pg.K_DOWN]:
                            if k_index + 1 > 2:
                                pass
                            else:
                                k_index += 1
                        elif keys[pg.K_z]:
                            print("enter z")
                            # 表示要购买该物资了
                            buy_item = npc_data["n_items"][k_index]
                            self.npc_list.trade(buy_item, self.now_hero)

                            # 刷新页面状态
                            self.now_shower.fresh_hero_pane()
                            self.now_shower.fresh_item_pane()

                            trade_event = False
                        elif keys[pg.K_SPACE]:
                            trade_event = False
                # 动画展示
                self.now_shower.fresh_trade_pane(npc_data["n_items"], k_index)
                pg.display.update()

            print("test")

        print("finish trade")


    # 开机关
    def to_open(self, e_pos):
        print("open door")
        door_type = self.now_map.get_value_nowlayer(e_pos)
        print(door_type)
        if door_type == c.MAP_IRON_RAIL:
            # 开门动画
            for i in range(4):
                # self.now_shower.fresh_layer()
                # self.now_shower.fresh_hero(self.pos, self.key_direct)
                self.now_shower.fresh_open(Tool.change_xy_pos(e_pos), door_type, i)
                pg.time.delay(100)
                pg.display.update(c.ACT_RECT)

            # 更新地图数据
            self.now_map.update_layer(e_pos, c.MAP_B_STONE)
        elif door_type == c.MAP_DOOR_YELLOW:
            print("yellow door")
            # 有钥匙才开门
            if self.now_hero.ITEMS["y_key"] > 0:
                self.now_hero.ITEMS["y_key"] -= 1
                # 刷新item
                self.now_shower.fresh_item_pane()
                pg.display.update(c.ITEM_RECT)

                for i in range(4):
                    # self.now_shower.fresh_layer()
                    # self.now_shower.fresh_hero(self.pos, self.key_direct)
                    self.now_shower.fresh_open(Tool.change_xy_pos(e_pos), door_type, i)
                    pg.time.delay(100)
                    pg.display.update(c.ACT_RECT)

                # 更新地图数据
                self.now_map.update_layer(e_pos, c.MAP_B_STONE)
            else:
                print("you don't have key")
        elif door_type == c.MAP_DOOR_BLUE:
            if self.now_hero.ITEMS["b_key"] > 0:
                self.now_hero.ITEMS["b_key"] -= 1
                self.now_shower.fresh_item_pane()
                pg.display.update(c.ITEM_RECT)

                for i in range(4):
                    self.now_shower.fresh_open(Tool.change_xy_pos(e_pos), door_type, i)
                    pg.time.delay(100)
                    pg.display.update(c.ACT_RECT)

                # 更新地图数据
                self.now_map.update_layer(e_pos, c.MAP_B_STONE)
            else:
                print("you don't have key")

    # 获取物品,物品位置
    def to_get_item(self, e_pos):
        get_item_event = True
        # 根据物品类型执行相相应效果
        item_val = self.now_map.get_value_nowlayer(e_pos)
        if item_val == c.MAP_ITEM_YK:
            self.now_hero.ITEMS["y_key"] += 1
            txt = "y_key: +1"
        elif item_val == c.MAP_ITEM_BK:
            self.now_hero.ITEMS["b_key"] += 1
            txt = "b_key: +1"
        elif item_val == c.MAP_ITEM_RK:
            self.now_hero.ITEMS["r_key"] += 1
            txt = "r_key: +1"
        elif item_val == c.MAP_ITEM_RM:
            txt = self.now_hero.use_item(items.ITEM_RED_MEDICINE)
        elif item_val == c.MAP_ITEM_RG:
            txt = self.now_hero.use_item(items.ITEM_RED_GEM)
        elif item_val == c.MAP_ITEM_BG:
            txt = self.now_hero.use_item(items.ITEM_BLUE_GEM)

        # 展示动画
        while get_item_event:
            self.now_shower.fresh_get_pane(txt)
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    keys = pg.key.get_pressed()
                    if keys[pg.K_SPACE]:
                        print("you print enter")
                        get_item_event = False

        # 恢复原状
        self.now_map.update_layer(e_pos, c.MAP_B_STONE)
        self.now_shower.update_all(self.pos, self.key_direct)


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
        self.mons_list.init_layer_mons(self.now_map.now_layer())
        print("test")

    # 下楼
    def to_down(self):
        # 强行让主距沿着该方向移动一步
        self.to_move()
        # 接着返回前一层
        print("pre layer")
        pre_l = self.now_map.pre_layer()
        # 更新shower数据
        self.now_shower.set_data(pre_l)
        self.now_shower.l_count = Tool.animate_count(4)



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

        pg.time.delay(100)
        pg.display.update()

    def main(self):
        # 主要运行函数
        self.init_State()
        # 绘制静态层
        self.now_shower.draw_sta_pane()
        self.now_shower.fresh_hero_pane()
        self.now_shower.fresh_item_pane()
        pg.display.update()

        # 动态绘制
        while self.done:
            self.event_loop()