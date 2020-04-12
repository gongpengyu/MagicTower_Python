# 负责游戏的展示
import pygame as pg
from . import constants as c
from . import tool

# 对图片进行处理，根据需求动态返回图像对象
class ImgList():
    def __init__(self):
        self.img_list = {}

        self.img_path = tool.Tool.get_dict_resource_path()
        # 静态文字素材
        self.s_txt = pg.font.SysFont("幼圆", int(c.PIXEL_GRID/2))
        self.s_txt.set_bold(True)
        self.m_txt = pg.font.SysFont("幼圆", 20)
        self.m_txt.set_bold(True)

    def init_imglist(self):
        self.img_list = {
            "bg_stone_s": self.get_static_img(c.BG_STONE_IMG),
            "w_stone_s": self.get_static_img(c.WHITE_STONE_IMG),
            "b_stone_s": self.get_static_img(c.BALCK_STONE_IMG),
            "up_floor_s": self.get_static_img(c.UP_FLOOR_IMG),
            "down_floor_s": self.get_static_img(c.DOWN_FLOOR_IMG),
            "iron_rail_s": self.get_static_img(c.IRON_RAIL_IMG),
            "hero_up_s": self.get_static_img(c.HERO_UP_IMG),
            "hero_down_s": self.get_static_img(c.HERO_DOWN_IMG),
            "hero_left_s": self.get_static_img(c.HERO_LEFT_IMG),
            "hero_right_s": self.get_static_img(c.HERO_RIGHT_IMG),
            "door_yellow_s": self.get_static_img(c.DOOR_YELLOW_IMG),
            "door_blue_s": self.get_static_img(c.DOOR_BLUE_IMG),
            "item_rkey_s": self.get_static_img(c.RKEY_IMG),
            "item_bkey_s": self.get_static_img(c.BKEY_IMG),
            "item_ykey_s": self.get_static_img(c.YKEY_IMG),
            "item_coin_s": self.get_static_img(c.COIN_IMG),
            "item_rmf_s": self.get_static_img(c.RED_MEDIF_IMG),
            "item_rgf_s": self.get_static_img(c.RED_GEM_IMG),
            "item_bgf_s": self.get_static_img(c.BLUE_GEM_IMG),
            "txt_state_s": self.get_sta_txt("状态：", "small"),
            "txt_level_s": self.get_sta_txt("等级：", "small"),
            "txt_hp_s": self.get_sta_txt("体力：", "small"),
            "txt_atk_s": self.get_sta_txt("攻击力：", "small"),
            "txt_def_s": self.get_sta_txt("防御力：", "small"),
            "txt_agi_s": self.get_sta_txt("敏捷：", "small"),
            "txt_exp_s": self.get_sta_txt("经验值：", "small"),
            "txt_vs_s": self.get_sta_txt("VS", "small"),
            "monster_sg_s": self.get_static_img(c.MONS_SLING_IMG),
            "magma_d": self.get_dynamic_img(c.MAGMA_IMG),
            "iron_rail_d": self.get_dynamic_img(c.IRON_RAIL_IMG),
            "hero_up_d": self.get_dynamic_img(c.HERO_UP_IMG),
            "hero_down_d": self.get_dynamic_img(c.HERO_DOWN_IMG),
            "hero_left_d": self.get_dynamic_img(c.HERO_LEFT_IMG),
            "hero_right_d": self.get_dynamic_img(c.HERO_RIGHT_IMG),
            "monster_sg_d": self.get_dynamic_img(c.MONS_SLING_IMG),
            "monster_sr_d": self.get_dynamic_img(c.MONS_SLINR_IMG),
            "monster_bf_d": self.get_dynamic_img(c.MONS_BATF_IMG),
            "monster_skullf_d": self.get_dynamic_img(c.MONS_SKULLF_IMG),
            "monster_mummyf_d": self.get_dynamic_img(c.MONS_MUMMYF_IMG),
            "npc_red_d": self.get_dynamic_img(c.NPC_RED_IMG),
            "npc_blue_d": self.get_dynamic_img(c.NPC_BLUE_IMG)
        }

    # 获取静态素材，根据素材字典和路径字典,path通过文件名获取路径，img中有存储对应文件名
    def get_static_img(self, img_dict):
        source_img = pg.image.load(self.img_path[img_dict["super"]])
        sub_img = pg.transform.scale(
            source_img.subsurface(img_dict["sta_rect"]),
            (img_dict["sta_wh_g"][0] * c.PIXEL_GRID, img_dict["sta_wh_g"][1] * c.PIXEL_GRID)
        )
        return sub_img

    # 获取动态素材，根据img_dict, img_path
    def get_dynamic_img(self, img_dict):
        source_img = pg.image.load(self.img_path[img_dict["super"]])
        sub_img = pg.transform.scale(
            source_img.subsurface(img_dict["dyn_rect"]),
            (img_dict["dyn_wh_g"][0] * c.PIXEL_GRID, img_dict["dyn_wh_g"][1] * c.PIXEL_GRID)
        )
        return sub_img

    # 获取静态文字素材
    def get_sta_txt(self, txt, size):
        if size == "small":
            txt_r = self.s_txt.render(txt, 1, (255, 255, 255))
            return txt_r
        elif size == "medium":
            txt_r = self.m_txt.render(txt, 1, (255, 255, 255))
            return txt_r

    # 返回对应key的图片素材
    def get_img(self, key):
        return self.img_list[key]

    # 根据提供数值进行渲染
    def get_txt(self, num):
        return self.s_txt.render(str(num), 1, (255, 255, 255))


class Shower():
    def __init__(self):
        self.screen = None
        self.active_screen = None
        self.hero_screen = None
        self.item_screen = None
        self.img_list = None
        self.l_count = None

        # 重要的数据
        self.data = None
        self.hero = None
        self.m_item = None

    def init_shower(self, data, hero, m_item):
        pg.display.set_caption(c.ORIGIN_CAPTION)
        self.screen = pg.display.set_mode(c.SCREEN_SIZE)
        self.active_screen = self.screen.subsurface(c.ACT_RECT)
        self.hero_screen = self.screen.subsurface(c.HERO_RECT)
        self.item_screen = self.screen.subsurface(c.ITEM_RECT)
        self.img_list = ImgList()
        self.img_list.init_imglist()
        self.data = data
        self.hero = hero
        self.m_item = m_item

        self.l_count = tool.Tool.animate_count(4)

    # 设置data
    def set_data(self, data):
        self.data = data
    # size代表展示范围(w,h),img为背景模板
    def show_background(self, size, img, surface):
        # 绘制背景
        for i in range(size[0]):
            for j in range(size[1]):
                surface.blit(img, (i*c.PIXEL_GRID, j * c.PIXEL_GRID))

    def show_sta_img(self, g_pos, g_size, img, surface):
        for i in range(g_size[0]):
            for j in range(g_size[1]):
                surface.blit(img, ((g_pos[0] + i) * c.PIXEL_GRID, (g_pos[1] + j) * c.PIXEL_GRID))


    # 先绘制静态不需要经常刷新的
    def draw_sta_pane(self):
        # screen的背景
        self.show_background([c.SCREEN_W_G, c.SCREEN_H_G], self.img_list.get_img("bg_stone_s"), self.screen)
        # 一些小标题
        self.show_sta_img((c.L_G_POINTX, c.L_G_POINTY), (c.L_W_G, c.L_H_G), self.img_list.get_img("b_stone_s"), self.screen)
        # 三个子screen的外框
        hero_rect = pg.draw.rect(self.screen, c.PURE_BLACK,
                                 (c.HERO_POINTX - 1, c.HERO_POINTY - 1, c.HERO_WIDTH + 1, c.HERO_HEIGHT + 1), 2)
        item_rect = pg.draw.rect(self.screen, c.PURE_BLACK,
                                 (c.ITEM_POINTX - 1, c.ITEM_POINTY - 1, c.ITEM_WIDTH + 1, c.ITEM_HEIGHT + 1), 2)
        active_rect = pg.draw.rect(self.screen, c.PURE_BLACK,
                                   (c.ACT_POINTX - 1, c.ACT_POINTY - 1, c.ACT_WIDTH + 1, c.ACT_HEIGHT + 1), 2)
        # 三个子背景
        self.show_background([c.HERO_W_G, c.HERO_H_G], self.img_list.get_img("b_stone_s"), self.hero_screen)
        self.show_background([c.ITEM_W_G, c.ITEM_H_G], self.img_list.get_img("b_stone_s"), self.item_screen)
        self.show_background([c.ACT_W_G, c.ACT_H_G], self.img_list.get_img("b_stone_s"), self.active_screen)

        # hero的静态参数
        head_pic = pg.transform.scale(
            self.img_list.get_img("hero_down_s"),
            (40, 40)
        )
        state_rect = pg.draw.rect(self.hero_screen, c.PURE_BLACK, (2*c.PIXEL_GRID, 20, 60, 32), 1)
        self.hero_screen.blit(head_pic, (0, 0))
        self.hero_screen.blit(self.img_list.get_img("txt_state_s"), (2 * c.PIXEL_GRID, 0 * c.PIXEL_GRID))
        self.hero_screen.blit(self.img_list.get_img("txt_level_s"), (0 * c.PIXEL_GRID, 2 * c.PIXEL_GRID))
        self.hero_screen.blit(self.img_list.get_img("txt_hp_s"), (0 * c.PIXEL_GRID, 3 * c.PIXEL_GRID))
        self.hero_screen.blit(self.img_list.get_img("txt_atk_s"), (0 * c.PIXEL_GRID, 4 * c.PIXEL_GRID))
        self.hero_screen.blit(self.img_list.get_img("txt_def_s"), (0 * c.PIXEL_GRID, 5 * c.PIXEL_GRID))
        self.hero_screen.blit(self.img_list.get_img("txt_agi_s"), (0 * c.PIXEL_GRID, 6 * c.PIXEL_GRID))
        self.hero_screen.blit(self.img_list.get_img("txt_exp_s"), (0 * c.PIXEL_GRID, 7 * c.PIXEL_GRID))

        # item区的静态参数
        self.item_screen.blit(self.img_list.get_img("item_ykey_s"), (0*c.PIXEL_GRID, 0*c.PIXEL_GRID))
        self.item_screen.blit(self.img_list.get_img("item_bkey_s"), (0*c.PIXEL_GRID, 1*c.PIXEL_GRID))
        self.item_screen.blit(self.img_list.get_img("item_rkey_s"), (0*c.PIXEL_GRID, 2*c.PIXEL_GRID))
        self.item_screen.blit(self.img_list.get_img("item_coin_s"), (0*c.PIXEL_GRID, 3*c.PIXEL_GRID))

    # map为待映射的数组
    def fresh_layer(self):
        data = self.data

        h_g = len(data)
        w_g = len(data[0])

        num = next(self.l_count)
        for j in range(h_g):
            for i in range(w_g):
                if data[j][i] == c.MAP_W_STONE:
                    self.active_screen.blit(self.img_list.get_img("w_stone_s"), (i * c.PIXEL_GRID, j * c.PIXEL_GRID))
                elif data[j][i] == c.MAP_B_STONE:
                    self.active_screen.blit(self.img_list.get_img("b_stone_s"), (i * c.PIXEL_GRID, j * c.PIXEL_GRID))
                elif data[j][i] == c.MAP_UP_FLO:
                    self.active_screen.blit(self.img_list.get_img("b_stone_s"), (i * c.PIXEL_GRID, j * c.PIXEL_GRID))
                    self.active_screen.blit(self.img_list.get_img("up_floor_s"), (i * c.PIXEL_GRID, j * c.PIXEL_GRID))
                elif data[j][i] == c.MAP_DOWN_FLO:
                    self.active_screen.blit(self.img_list.get_img("b_stone_s"), (i * c.PIXEL_GRID, j * c.PIXEL_GRID))
                    self.active_screen.blit(self.img_list.get_img("down_floor_s"), (i * c.PIXEL_GRID, j * c.PIXEL_GRID))
                elif data[j][i] == c.MAP_IRON_RAIL:
                    self.active_screen.blit(self.img_list.get_img("b_stone_s"), (i * c.PIXEL_GRID, j * c.PIXEL_GRID))
                    self.active_screen.blit(self.img_list.get_img("iron_rail_s"), (i * c.PIXEL_GRID, j * c.PIXEL_GRID))
                elif data[j][i] == c.MAP_ITEM_RM:
                    self.active_screen.blit(self.img_list.get_img("b_stone_s"), (i * c.PIXEL_GRID, j * c.PIXEL_GRID))
                    self.active_screen.blit(self.img_list.get_img("item_rmf_s"), (i * c.PIXEL_GRID, j * c.PIXEL_GRID))
                elif data[j][i] == c.MAP_ITEM_RG:
                    self.active_screen.blit(self.img_list.get_img("b_stone_s"), (i * c.PIXEL_GRID, j * c.PIXEL_GRID))
                    self.active_screen.blit(self.img_list.get_img("item_rgf_s"), (i * c.PIXEL_GRID, j * c.PIXEL_GRID))
                elif data[j][i] == c.MAP_ITEM_BG:
                    self.active_screen.blit(self.img_list.get_img("b_stone_s"), (i * c.PIXEL_GRID, j * c.PIXEL_GRID))
                    self.active_screen.blit(self.img_list.get_img("item_bgf_s"), (i * c.PIXEL_GRID, j * c.PIXEL_GRID))
                elif data[j][i] == c.MAP_ITEM_YK:
                    self.active_screen.blit(self.img_list.get_img("b_stone_s"), (i * c.PIXEL_GRID, j * c.PIXEL_GRID))
                    self.active_screen.blit(self.img_list.get_img("item_ykey_s"), (i * c.PIXEL_GRID, j * c.PIXEL_GRID))
                elif data[j][i] == c.MAP_ITEM_BK:
                    self.active_screen.blit(self.img_list.get_img("b_stone_s"), (i * c.PIXEL_GRID, j * c.PIXEL_GRID))
                    self.active_screen.blit(self.img_list.get_img("item_bkey_s"), (i * c.PIXEL_GRID, j * c.PIXEL_GRID))
                elif data[j][i] == c.MAP_ITEM_RK:
                    self.active_screen.blit(self.img_list.get_img("b_stone_s"), (i * c.PIXEL_GRID, j * c.PIXEL_GRID))
                    self.active_screen.blit(self.img_list.get_img("item_rkey_s"), (i * c.PIXEL_GRID, j * c.PIXEL_GRID))
                elif data[j][i] == c.MAP_DOOR_YELLOW:
                    self.active_screen.blit(self.img_list.get_img("b_stone_s"), (i * c.PIXEL_GRID, j * c.PIXEL_GRID))
                    self.active_screen.blit(self.img_list.get_img("door_yellow_s"), (i * c.PIXEL_GRID, j * c.PIXEL_GRID))
                elif data[j][i] == c.MAP_DOOR_BLUE:
                    self.active_screen.blit(self.img_list.get_img("b_stone_s"), (i * c.PIXEL_GRID, j * c.PIXEL_GRID))
                    self.active_screen.blit(self.img_list.get_img("door_blue_s"), (i * c.PIXEL_GRID, j * c.PIXEL_GRID))
                elif data[j][i] == c.MAP_MAGMA:
                    self.active_screen.blit(
                        self.img_list.get_img("magma_d"),
                        (i * c.PIXEL_GRID, j * c.PIXEL_GRID),
                        (num*c.PIXEL_GRID, 0, c.PIXEL_GRID, c.PIXEL_GRID)
                    )
                elif data[j][i] == c.MAP_MONS_SG:
                    # self.active_screen.blit(self.img_list.get_img("b_stone_s"), (i*c.PIXEL_GRID, j*c.PIXEL_GRID))
                    self.active_screen.blit(
                        self.img_list.get_img("monster_sg_d"),
                        (i * c.PIXEL_GRID, j * c.PIXEL_GRID),
                        (num * c.PIXEL_GRID, 0, c.PIXEL_GRID, c.PIXEL_GRID)
                    )
                elif data[j][i] == c.MAP_MONS_SR:
                    self.active_screen.blit(
                        self.img_list.get_img("monster_sr_d"),
                        (i * c.PIXEL_GRID, j * c.PIXEL_GRID),
                        (num * c.PIXEL_GRID, 0, c.PIXEL_GRID, c.PIXEL_GRID)
                    )
                elif data[j][i] == c.MAP_MONS_BATF:
                    self.active_screen.blit(
                        self.img_list.get_img("monster_bf_d"),
                        (i * c.PIXEL_GRID, j * c.PIXEL_GRID),
                        (num * c.PIXEL_GRID, 0, c.PIXEL_GRID, c.PIXEL_GRID)
                    )
                elif data[j][i] == c.MAP_MONS_SKULLF:
                    self.active_screen.blit(
                        self.img_list.get_img("monster_skullf_d"),
                        (i * c.PIXEL_GRID, j * c.PIXEL_GRID),
                        (num * c.PIXEL_GRID, 0, c.PIXEL_GRID, c.PIXEL_GRID)
                    )
                elif data[j][i] == c.MAP_MONS_MUMMYF:
                    self.active_screen.blit(
                        self.img_list.get_img("monster_mummyf_d"),
                        (i * c.PIXEL_GRID, j * c.PIXEL_GRID),
                        (num * c.PIXEL_GRID, 0, c.PIXEL_GRID, c.PIXEL_GRID)
                    )
                elif data[j][i] == c.MAP_NPC_RED:
                    self.active_screen.blit(self.img_list.get_img("b_stone_s"), (i * c.PIXEL_GRID, j * c.PIXEL_GRID))
                    self.active_screen.blit(
                        self.img_list.get_img("npc_red_d"),
                        (i * c.PIXEL_GRID, j * c.PIXEL_GRID),
                        (num * c.PIXEL_GRID, 0, c.PIXEL_GRID, c.PIXEL_GRID)
                    )
                elif data[j][i] == c.MAP_NPC_BLUE:
                    self.active_screen.blit(self.img_list.get_img("b_stone_s"), (i * c.PIXEL_GRID, j * c.PIXEL_GRID))
                    self.active_screen.blit(
                        self.img_list.get_img("npc_blue_d"),
                        (i * c.PIXEL_GRID, j * c.PIXEL_GRID),
                        (num * c.PIXEL_GRID, 0, c.PIXEL_GRID, c.PIXEL_GRID)
                    )

    def fresh_hero(self, pos, direct):
        if direct == c.KEY_UP:
            self.active_screen.blit(self.img_list.get_img("b_stone_s"), (pos[0] * c.PIXEL_GRID, pos[1] * c.PIXEL_GRID))
            self.active_screen.blit(self.img_list.get_img("hero_up_s"), (pos[0] * c.PIXEL_GRID, pos[1] * c.PIXEL_GRID))
        elif direct == c.KEY_DOWN:
            self.active_screen.blit(self.img_list.get_img("b_stone_s"), (pos[0] * c.PIXEL_GRID, pos[1] * c.PIXEL_GRID))
            self.active_screen.blit(self.img_list.get_img("hero_down_s"), (pos[0] * c.PIXEL_GRID, pos[1] * c.PIXEL_GRID))
        elif direct == c.KEY_LEFT:
            self.active_screen.blit(self.img_list.get_img("b_stone_s"), (pos[0] * c.PIXEL_GRID, pos[1] * c.PIXEL_GRID))
            self.active_screen.blit(self.img_list.get_img("hero_left_s"), (pos[0] * c.PIXEL_GRID, pos[1] * c.PIXEL_GRID))
        elif direct == c.KEY_RIGHT:
            self.active_screen.blit(self.img_list.get_img("b_stone_s"), (pos[0] * c.PIXEL_GRID, pos[1] * c.PIXEL_GRID))
            self.active_screen.blit(self.img_list.get_img("hero_right_s"), (pos[0] * c.PIXEL_GRID, pos[1] * c.PIXEL_GRID))

    # hero为重要属性数据
    def fresh_hero_atr(self):
        hero = self.hero
        surface = self.hero_screen

        lv_t = self.img_list.get_txt(hero.LV)
        hp_t = self.img_list.get_txt(hero.HP)
        atk_t = self.img_list.get_txt(hero.ATK)
        def_t = self.img_list.get_txt(hero.DEF)
        agi_t = self.img_list.get_txt(hero.AGI)
        exp_t = self.img_list.get_txt(hero.EXP)
        state_t = self.img_list.get_txt(hero.STATE)

        surface.blit(state_t, (2 * c.PIXEL_GRID + 12, 1 * c.PIXEL_GRID - 5))
        surface.blit(lv_t, (2 * c.PIXEL_GRID, 2 * c.PIXEL_GRID))
        surface.blit(hp_t, (2 * c.PIXEL_GRID, 3 * c.PIXEL_GRID))
        surface.blit(atk_t, (2 * c.PIXEL_GRID, 4 * c.PIXEL_GRID))
        surface.blit(def_t, (2 * c.PIXEL_GRID, 5 * c.PIXEL_GRID))
        surface.blit(agi_t, (2 * c.PIXEL_GRID, 6 * c.PIXEL_GRID))
        surface.blit(exp_t, (2 * c.PIXEL_GRID, 7 * c.PIXEL_GRID))

    # item为所获取物品数据
    def fresh_item(self):
        m_item = self.m_item
        surface = self.item_screen

        yk_atr = self.img_list.get_txt(m_item["y_key"])
        bk_atr = self.img_list.get_txt(m_item["b_key"])
        rk_atr = self.img_list.get_txt(m_item["r_key"])
        co_atr = self.img_list.get_txt(m_item["coin"])

        surface.blit(yk_atr, (1*c.PIXEL_GRID+16, 0*c.PIXEL_GRID+16))
        surface.blit(bk_atr, (1*c.PIXEL_GRID+16, 1*c.PIXEL_GRID+16))
        surface.blit(rk_atr, (1*c.PIXEL_GRID+16, 2*c.PIXEL_GRID+16))
        surface.blit(co_atr, (1*c.PIXEL_GRID+16, 3*c.PIXEL_GRID+16))

    # 走路动作,pos位置，key方向
    def fresh_walk(self, pos, key, num):
        surface = self.active_screen

        if key == c.KEY_UP:
            surface.blit(
                self.img_list.get_img("hero_up_d"),
                (pos[0] * c.PIXEL_GRID, pos[1] * c.PIXEL_GRID),
                (num * c.PIXEL_GRID, 0, c.PIXEL_GRID, c.PIXEL_GRID)
            )
        elif key == c.KEY_DOWN:
            surface.blit(
                self.img_list.get_img("hero_down_d"),
                (pos[0] * c.PIXEL_GRID, pos[1] * c.PIXEL_GRID),
                (num * c.PIXEL_GRID, 0, c.PIXEL_GRID, c.PIXEL_GRID)
            )
        elif key == c.KEY_LEFT:
            surface.blit(
                self.img_list.get_img("hero_left_d"),
                (pos[0] * c.PIXEL_GRID, pos[1] * c.PIXEL_GRID),
                (num * c.PIXEL_GRID, 0, c.PIXEL_GRID, c.PIXEL_GRID)
            )
        elif key == c.KEY_RIGHT:
            surface.blit(
                self.img_list.get_img("hero_right_d"),
                (pos[0] * c.PIXEL_GRID, pos[1] * c.PIXEL_GRID),
                (num * c.PIXEL_GRID, 0, c.PIXEL_GRID, c.PIXEL_GRID)
            )

    # 开铁门动作
    def fresh_open(self, pos, door_type, num):
        surface = self.active_screen

        if door_type == c.MAP_IRON_RAIL:
            self.active_screen.blit(self.img_list.get_img("b_stone_s"), (pos[0] * c.PIXEL_GRID, pos[1] * c.PIXEL_GRID))
            surface.blit(
                self.img_list.get_img("iron_rail_d"),
                (pos[0] * c.PIXEL_GRID, pos[1] * c.PIXEL_GRID),
                (0, num*c.PIXEL_GRID, c.PIXEL_GRID, c.PIXEL_GRID)
            )

    # 展示战斗面板
    def fresh_atk_pane(self, mons, hero):
        surface = self.screen.subsurface(c.ATKPANE_RECT)

        # 绘制背景
        for i in range(c.ATKPANE_W_G):
            for j in range(c.ATKPANE_H_G):
                surface.blit(self.img_list.get_img("b_stone_s"), (i*c.PIXEL_GRID, j*c.PIXEL_GRID))

        # 装配属性
        mos_pic = None
        if mons.NAME == "slime-green":
            mos_pic = self.img_list.get_img("monster_sg_s")
        hero_pic = self.img_list.get_img("hero_down_s")
        name_h = self.img_list.get_txt(hero.NAME)
        hp_h = self.img_list.get_txt(hero.HP)
        atk_h = self.img_list.get_txt(hero.ATK)
        def_h = self.img_list.get_txt(hero.DEF)
        agi_h = self.img_list.get_txt(hero.AGI)
        name_m = self.img_list.get_txt(mons.NAME)
        hp_m = self.img_list.get_txt(mons.HP)
        atk_m = self.img_list.get_txt(mons.ATK)
        def_m = self.img_list.get_txt(mons.DEF)
        agi_m = self.img_list.get_txt(mons.AGI)

        # 绘制属性
        surface.blit(mos_pic, (0 + c.ATKPANE_REL, 0 + c.ATKPANE_REL))
        surface.blit(hero_pic, (12 * c.PIXEL_GRID + c.ATKPANE_REL, 0 + c.ATKPANE_REL))
        surface.blit(name_m, (2 * c.PIXEL_GRID + c.ATKPANE_REL, 0 + c.ATKPANE_REL))
        surface.blit(name_h, (10 * c.PIXEL_GRID + c.ATKPANE_REL, 0 + c.ATKPANE_REL))
        surface.blit(self.img_list.get_img("txt_vs_s"), (6 * c.PIXEL_GRID + c.ATKPANE_REL, 0 + c.ATKPANE_REL))
        surface.blit(self.img_list.get_img("txt_hp_s"),
                     (0 * c.PIXEL_GRID + c.ATKPANE_REL, 2 * c.PIXEL_GRID + c.ATKPANE_REL))
        surface.blit(self.img_list.get_img("txt_atk_s"),
                     (0 * c.PIXEL_GRID + c.ATKPANE_REL, 3 * c.PIXEL_GRID + c.ATKPANE_REL))
        surface.blit(self.img_list.get_img("txt_def_s"),
                     (0 * c.PIXEL_GRID + c.ATKPANE_REL, 4 * c.PIXEL_GRID + c.ATKPANE_REL))
        surface.blit(self.img_list.get_img("txt_agi_s"),
                     (0 * c.PIXEL_GRID + c.ATKPANE_REL, 5 * c.PIXEL_GRID + c.ATKPANE_REL))
        surface.blit(self.img_list.get_img("txt_hp_s"),
                     (7 * c.PIXEL_GRID + c.ATKPANE_REL, 2 * c.PIXEL_GRID + c.ATKPANE_REL))
        surface.blit(self.img_list.get_img("txt_atk_s"),
                     (7 * c.PIXEL_GRID + c.ATKPANE_REL, 3 * c.PIXEL_GRID + c.ATKPANE_REL))
        surface.blit(self.img_list.get_img("txt_def_s"),
                     (7 * c.PIXEL_GRID + c.ATKPANE_REL, 4 * c.PIXEL_GRID + c.ATKPANE_REL))
        surface.blit(self.img_list.get_img("txt_agi_s"),
                     (7 * c.PIXEL_GRID + c.ATKPANE_REL, 5 * c.PIXEL_GRID + c.ATKPANE_REL))

        surface.blit(hp_m, (2 * c.PIXEL_GRID + c.ATKPANE_REL, 2 * c.PIXEL_GRID + c.ATKPANE_REL))
        surface.blit(atk_m, (2 * c.PIXEL_GRID + c.ATKPANE_REL, 3 * c.PIXEL_GRID + c.ATKPANE_REL))
        surface.blit(def_m, (2 * c.PIXEL_GRID + c.ATKPANE_REL, 4 * c.PIXEL_GRID + c.ATKPANE_REL))
        surface.blit(agi_m, (2 * c.PIXEL_GRID + c.ATKPANE_REL, 5 * c.PIXEL_GRID + c.ATKPANE_REL))
        surface.blit(hp_h, (9 * c.PIXEL_GRID + c.ATKPANE_REL, 2 * c.PIXEL_GRID + c.ATKPANE_REL))
        surface.blit(atk_h, (9 * c.PIXEL_GRID + c.ATKPANE_REL, 3 * c.PIXEL_GRID + c.ATKPANE_REL))
        surface.blit(def_h, (9 * c.PIXEL_GRID + c.ATKPANE_REL, 4 * c.PIXEL_GRID + c.ATKPANE_REL))
        surface.blit(agi_h, (9 * c.PIXEL_GRID + c.ATKPANE_REL, 5 * c.PIXEL_GRID + c.ATKPANE_REL))





    # 刷洗图层
    def update(self, pos):
        self.fresh_layer()
        # self.fresh_hero(hero)
        # self.fresh_item(m_item)
        # self.fresh_hero(pos, c.KEY_UP)

        pg.time.delay(200)
        pg.display.update()