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
            "door_red_s": self.get_static_img(c.DOOR_RED_IMG),
            "god_left_s": self.get_static_img(c.GOD_LEFT_IMG),
            "god_center_s": self.get_static_img(c.GOD_CENTER_IMG),
            "god_right_s": self.get_static_img(c.GOD_RIGHT_IMG),
            "item_rkey_s": self.get_static_img(c.RKEY_IMG),
            "item_bkey_s": self.get_static_img(c.BKEY_IMG),
            "item_ykey_s": self.get_static_img(c.YKEY_IMG),
            "item_coin_s": self.get_static_img(c.COIN_IMG),
            "item_rmf_s": self.get_static_img(c.RED_MEDIF_IMG),
            "item_bm_s": self.get_static_img(c.BLUE_MED_IMG),
            "item_rgf_s": self.get_static_img(c.RED_GEM_IMG),
            "item_bgf_s": self.get_static_img(c.BLUE_GEM_IMG),
            "item_agf_s": self.get_static_img(c.AGI_GEM_IMG),
            "item_rw_s": self.get_static_img(c.RETURN_WEAK_IMG),
            "item_rp_s": self.get_static_img(c.RETURN_POI_IMG),
            "item_ul_s": self.get_static_img(c.UP_LEVEL_IMG),
            "item_is_s": self.get_static_img(c.IRON_SWORD_IMG),
            "item_ss_s": self.get_static_img(c.SILVER_SWORD_IMG),
            "item_ie_s": self.get_static_img(c.IRON_EQUIP_IMG),
            "txt_state_s": self.get_sta_txt("状态：", "small"),
            "txt_level_s": self.get_sta_txt("等级：", "small"),
            "txt_hp_s": self.get_sta_txt("体力：", "small"),
            "txt_atk_s": self.get_sta_txt("攻击力：", "small"),
            "txt_def_s": self.get_sta_txt("防御力：", "small"),
            "txt_agi_s": self.get_sta_txt("敏捷：", "small"),
            "txt_exp_s": self.get_sta_txt("经验值：", "small"),
            "txt_vs_s": self.get_sta_txt("VS", "small"),
            "monster_sg_s": self.get_static_img(c.MONS_SLING_IMG),
            "monster_sr_s": self.get_static_img(c.MONS_SLINR_IMG),
            "monster_sb_s": self.get_static_img(c.MONS_SLINB_IMG),
            "monster_bf_s": self.get_static_img(c.MONS_BATF_IMG),
            "monster_bs_s": self.get_static_img(c.MONS_BATS_IMG),
            "monster_bt_s": self.get_static_img(c.MONS_BATT_IMG),
            "monster_skullf_s": self.get_static_img(c.MONS_SKULLF_IMG),
            "monster_skulls_s": self.get_static_img(c.MONS_SKULLS_IMG),
            "monster_skullt_s": self.get_static_img(c.MONS_SKULLT_IMG),
            "monster_mummyf_s": self.get_static_img(c.MONS_MUMMYF_IMG),
            "monster_nightf_s": self.get_static_img(c.MONS_NIGHTF_IMG),
            "monster_guardf_s": self.get_static_img(c.MONS_GUARDF_IMG),
            "monster_wzf_s": self.get_static_img(c.MONS_WZF_IMG),
            "monster_wzs_s": self.get_static_img(c.MONS_WZS_IMG),
            "monster_stonemf_s": self.get_static_img(c.MONS_STONEM_IMG),
            "monster_slimeh_s": self.get_static_img(c.MONS_SLIMEH_IMG),
            "arrow_r_s": self.get_static_img(c.ARROW_R_IMG),
            "magma_d": self.get_dynamic_img(c.MAGMA_IMG),
            "iron_rail_d": self.get_dynamic_img(c.IRON_RAIL_IMG),
            "hero_up_d": self.get_dynamic_img(c.HERO_UP_IMG),
            "hero_down_d": self.get_dynamic_img(c.HERO_DOWN_IMG),
            "hero_left_d": self.get_dynamic_img(c.HERO_LEFT_IMG),
            "hero_right_d": self.get_dynamic_img(c.HERO_RIGHT_IMG),
            "door_yellow_d": self.get_dynamic_img(c.DOOR_YELLOW_IMG),
            "door_blue_d": self.get_dynamic_img(c.DOOR_BLUE_IMG),
            "door_red_d": self.get_dynamic_img(c.DOOR_RED_IMG),
            "monster_sg_d": self.get_dynamic_img(c.MONS_SLING_IMG),
            "monster_sr_d": self.get_dynamic_img(c.MONS_SLINR_IMG),
            "monster_sb_d": self.get_dynamic_img(c.MONS_SLINB_IMG),
            "monster_bf_d": self.get_dynamic_img(c.MONS_BATF_IMG),
            "monster_bs_d": self.get_dynamic_img(c.MONS_BATS_IMG),
            "monster_bt_d": self.get_dynamic_img(c.MONS_BATT_IMG),
            "monster_skullf_d": self.get_dynamic_img(c.MONS_SKULLF_IMG),
            "monster_skulls_d": self.get_dynamic_img(c.MONS_SKULLS_IMG),
            "monster_skullt_d": self.get_dynamic_img(c.MONS_SKULLT_IMG),
            "monster_mummyf_d": self.get_dynamic_img(c.MONS_MUMMYF_IMG),
            "monster_nightf_d": self.get_dynamic_img(c.MONS_NIGHTF_IMG),
            "monster_guardf_d": self.get_dynamic_img(c.MONS_GUARDF_IMG),
            "monster_wzf_d": self.get_dynamic_img(c.MONS_WZF_IMG),
            "monster_wzs_d": self.get_dynamic_img(c.MONS_WZS_IMG),
            "monster_stonemf_d": self.get_dynamic_img(c.MONS_STONEM_IMG),
            "monster_slimeh_d": self.get_dynamic_img(c.MONS_SLIMEH_IMG),
            "npc_red_d": self.get_dynamic_img(c.NPC_RED_IMG),
            "npc_blue_d": self.get_dynamic_img(c.NPC_BLUE_IMG),
            "npc_yellow_d": self.get_dynamic_img(c.NPC_YELLOW_IMG)
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
        self.l_index = 0

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
    def set_layer_index(self, num):
        self.l_index = num

    # size代表展示范围(w,h),img为背景模板
    def show_background(self, size, img, surface):
        # 绘制背景
        for i in range(size[0]):
            for j in range(size[1]):
                surface.blit(img, (i*c.PIXEL_GRID, j * c.PIXEL_GRID))

        # 绘制边框
        t_rect = pg.draw.rect(surface, c.PURE_BLACK, (0, 0, size[0] * c.PIXEL_GRID, size[1] * c.PIXEL_GRID), 2)

    def show_sta_img(self, g_pos, g_size, img, surface):
        for i in range(g_size[0]):
            for j in range(g_size[1]):
                surface.blit(img, ((g_pos[0] + i) * c.PIXEL_GRID, (g_pos[1] + j) * c.PIXEL_GRID))


    # 先绘制静态不需要经常刷新的
    def draw_sta_pane(self):
        # screen的背景
        self.show_background([c.SCREEN_W_G, c.SCREEN_H_G], self.img_list.get_img("bg_stone_s"), self.screen)


    def fresh_title(self):
        # 一些小标题
        surface = self.screen.subsurface(c.L_RECT)
        self.show_background([c.L_W_G, c.L_H_G], self.img_list.get_img("b_stone_s"), surface)

        title_s = "第" + str(self.l_index) + "层"
        title_h = self.img_list.get_sta_txt(title_s, "small")
        surface.blit(title_h, (8, 8))

    # map为待映射的数组
    def fresh_layer(self):
        # 刷新背板
        self.show_background([c.ACT_W_G, c.ACT_H_G], self.img_list.get_img("b_stone_s"), self.active_screen)

        data = self.data

        h_g = len(data)
        w_g = len(data[0])

        num = next(self.l_count)
        rect_d = (num * c.PIXEL_GRID, 0, c.PIXEL_GRID, c.PIXEL_GRID)
        for j in range(h_g):
            for i in range(w_g):
                pos_r = (i * c.PIXEL_GRID, j * c.PIXEL_GRID)
                if data[j][i] == c.MAP_W_STONE:
                    self.active_screen.blit(self.img_list.get_img("w_stone_s"), pos_r)
                elif data[j][i] == c.MAP_B_STONE:
                    self.active_screen.blit(self.img_list.get_img("b_stone_s"), pos_r)
                elif data[j][i] == c.MAP_UP_FLO:
                    self.active_screen.blit(self.img_list.get_img("up_floor_s"), pos_r)
                elif data[j][i] == c.MAP_DOWN_FLO:
                    self.active_screen.blit(self.img_list.get_img("down_floor_s"), pos_r)
                elif data[j][i] == c.MAP_IRON_RAIL:
                    self.active_screen.blit(self.img_list.get_img("iron_rail_s"), pos_r)
                elif data[j][i] == c.MAP_ITEM_RM:
                    self.active_screen.blit(self.img_list.get_img("item_rmf_s"), pos_r)
                elif data[j][i] == c.MAP_ITEM_BM:
                    self.active_screen.blit(self.img_list.get_img("item_bm_s"), pos_r)
                elif data[j][i] == c.MAP_ITEM_RG:
                    self.active_screen.blit(self.img_list.get_img("item_rgf_s"), pos_r)
                elif data[j][i] == c.MAP_ITEM_BG:
                    self.active_screen.blit(self.img_list.get_img("item_bgf_s"), pos_r)
                elif data[j][i] == c.MAP_ITEM_AG:
                    self.active_screen.blit(self.img_list.get_img("item_agf_s"), pos_r)
                elif data[j][i] == c.MAP_ITEM_YK:
                    self.active_screen.blit(self.img_list.get_img("item_ykey_s"), pos_r)
                elif data[j][i] == c.MAP_ITEM_BK:
                    self.active_screen.blit(self.img_list.get_img("item_bkey_s"), pos_r)
                elif data[j][i] == c.MAP_ITEM_RK:
                    self.active_screen.blit(self.img_list.get_img("item_rkey_s"), pos_r)
                elif data[j][i] == c.MAP_DOOR_YELLOW:
                    self.active_screen.blit(self.img_list.get_img("door_yellow_s"), pos_r)
                elif data[j][i] == c.MAP_DOOR_BLUE:
                    self.active_screen.blit(self.img_list.get_img("door_blue_s"), pos_r)
                elif data[j][i] == c.MAP_DOOR_RED:
                    self.active_screen.blit(self.img_list.get_img("door_red_s"), pos_r)
                elif data[j][i] == c.MAP_GOD_LEFT:
                    self.active_screen.blit(self.img_list.get_img("god_left_s"), pos_r)
                elif data[j][i] == c.MAP_GOD_CENTER:
                    self.active_screen.blit(self.img_list.get_img("god_center_s"), pos_r)
                elif data[j][i] == c.MAP_GOD_RIGHT:
                    self.active_screen.blit(self.img_list.get_img("god_right_s"), pos_r)
                elif data[j][i] == c.MAP_ITEM_RW:
                    self.active_screen.blit(self.img_list.get_img("item_rw_s"), pos_r)
                elif data[j][i] == c.MAP_ITEM_RP:
                    self.active_screen.blit(self.img_list.get_img("item_rp_s"), pos_r)
                elif data[j][i] == c.MAP_ITEM_UL:
                    self.active_screen.blit(self.img_list.get_img("item_ul_s"), pos_r)
                elif data[j][i] == c.MAP_ITEM_IS:
                    self.active_screen.blit(self.img_list.get_img("item_is_s"), pos_r)
                elif data[j][i] == c.MAP_ITEM_SS:
                    self.active_screen.blit(self.img_list.get_img("item_ss_s"), pos_r)
                elif data[j][i] == c.MAP_ITEM_IE:
                    self.active_screen.blit(self.img_list.get_img("item_ie_s"), pos_r)
                elif data[j][i] == c.MAP_MAGMA:
                    self.active_screen.blit(self.img_list.get_img("magma_d"), pos_r, rect_d)
                elif data[j][i] == c.MAP_MONS_SG:
                    self.active_screen.blit(self.img_list.get_img("monster_sg_d"), pos_r, rect_d)
                elif data[j][i] == c.MAP_MONS_SR:
                    self.active_screen.blit(self.img_list.get_img("monster_sr_d"), pos_r, rect_d)
                elif data[j][i] == c.MAP_MONS_SB:
                    self.active_screen.blit(self.img_list.get_img("monster_sb_d"), pos_r, rect_d)
                elif data[j][i] == c.MAP_MONS_BATF:
                    self.active_screen.blit(self.img_list.get_img("monster_bf_d"), pos_r, rect_d)
                elif data[j][i] == c.MAP_MONS_BATS:
                    self.active_screen.blit(self.img_list.get_img("monster_bs_d"), pos_r, rect_d)
                elif data[j][i] == c.MAP_MONS_BATT:
                    self.active_screen.blit(self.img_list.get_img("monster_bt_d"), pos_r, rect_d)
                elif data[j][i] == c.MAP_MONS_SKULLF:
                    self.active_screen.blit(self.img_list.get_img("monster_skullf_d"), pos_r, rect_d)
                elif data[j][i] == c.MAP_MONS_SKULLS:
                    self.active_screen.blit(self.img_list.get_img("monster_skulls_d"), pos_r, rect_d)
                elif data[j][i] == c.MAP_MONS_SKULLT:
                    self.active_screen.blit(self.img_list.get_img("monster_skullt_d"), pos_r, rect_d)
                elif data[j][i] == c.MAP_MONS_MUMMYF:
                    self.active_screen.blit(self.img_list.get_img("monster_mummyf_d"), pos_r, rect_d)
                elif data[j][i] == c.MAP_MONS_NIGHTF:
                    self.active_screen.blit(self.img_list.get_img("monster_nightf_d"), pos_r, rect_d)
                elif data[j][i] == c.MAP_MONS_WZF:
                    self.active_screen.blit(self.img_list.get_img("monster_wzf_d"), pos_r, rect_d)
                elif data[j][i] == c.MAP_NPC_RED:
                    self.active_screen.blit(self.img_list.get_img("npc_red_d"), pos_r, rect_d)
                elif data[j][i] == c.MAP_NPC_BLUE:
                    self.active_screen.blit(self.img_list.get_img("npc_blue_d"), pos_r, rect_d)
                elif data[j][i] == c.MAP_NPC_YELLOW:
                    self.active_screen.blit(self.img_list.get_img("npc_yellow_d"), pos_r, rect_d)
                elif data[j][i] == c.MAP_MONS_WZS:
                    self.active_screen.blit(self.img_list.get_img("monster_wzs_d"), pos_r, rect_d)
                elif data[j][i] == c.MAP_MONS_GUARDF:
                    self.active_screen.blit(self.img_list.get_img("monster_guardf_d"), pos_r, rect_d)
                elif data[j][i] == c.MAP_MONS_STONEM:
                    self.active_screen.blit(self.img_list.get_img("monster_stonemf_d"), pos_r, rect_d)
                elif data[j][i] == c.MAP_MONS_SLIMEH:
                    self.active_screen.blit(self.img_list.get_img("monster_slimeh_d"), pos_r, rect_d)

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
    def fresh_hero_pane(self):
        # 刷新背板
        self.show_background([c.HERO_W_G, c.HERO_H_G], self.img_list.get_img("b_stone_s"), self.hero_screen)

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

        hero = self.hero
        surface = self.hero_screen
        st_img = self.img_list.get_img("b_stone_s")

        lv_t = self.img_list.get_txt(hero.LV)
        hp_t = self.img_list.get_txt(hero.HP)
        atk_t = self.img_list.get_txt(hero.ATK)
        def_t = self.img_list.get_txt(hero.DEF)
        agi_t = self.img_list.get_txt(hero.AGI)
        exp_t = self.img_list.get_txt(hero.EXP)
        state_t = self.img_list.get_txt(hero.STATE)

        surface.blit(state_t, (2 * c.PIXEL_GRID + 12, 1 * c.PIXEL_GRID - 5))
        surface.blit(st_img, (2 * c.PIXEL_GRID, 2 * c.PIXEL_GRID))
        surface.blit(lv_t, (2 * c.PIXEL_GRID, 2 * c.PIXEL_GRID))
        surface.blit(hp_t, (2 * c.PIXEL_GRID, 3 * c.PIXEL_GRID))
        surface.blit(atk_t, (2 * c.PIXEL_GRID, 4 * c.PIXEL_GRID))
        surface.blit(def_t, (2 * c.PIXEL_GRID, 5 * c.PIXEL_GRID))
        surface.blit(agi_t, (2 * c.PIXEL_GRID, 6 * c.PIXEL_GRID))
        surface.blit(exp_t, (2 * c.PIXEL_GRID, 7 * c.PIXEL_GRID))

    # item为所获取物品数据
    def fresh_item_pane(self):
        m_item = self.m_item
        surface = self.item_screen
        st_img = self.img_list.get_img("b_stone_s")

        # 刷新背板
        self.show_background([c.ITEM_W_G, c.ITEM_H_G], self.img_list.get_img("b_stone_s"), self.item_screen)

        # item区的静态参数
        self.item_screen.blit(self.img_list.get_img("item_ykey_s"), (0*c.PIXEL_GRID, 0*c.PIXEL_GRID))
        self.item_screen.blit(self.img_list.get_img("item_bkey_s"), (0*c.PIXEL_GRID, 1*c.PIXEL_GRID))
        self.item_screen.blit(self.img_list.get_img("item_rkey_s"), (0*c.PIXEL_GRID, 2*c.PIXEL_GRID))
        self.item_screen.blit(self.img_list.get_img("item_coin_s"), (0*c.PIXEL_GRID, 3*c.PIXEL_GRID))

        # 展示装备
        if m_item["atk_equip"] is None:
            pass
        else:
            if m_item["atk_equip"]["name"] == "iron-sword":
                atk_equip_pic = self.img_list.get_img("item_is_s")
            elif m_item["atk_equip"]["name"] == "silver-sword":
                atk_equip_pic = self.img_list.get_img("item_ss_s")
            surface.blit(atk_equip_pic, (3*c.PIXEL_GRID, 0*c.PIXEL_GRID))

        if m_item["def_equip"] is None:
            pass
        else:
            if m_item["def_equip"]["name"] == "iron-equip":
                def_equip_pic = self.img_list.get_img("item_ie_s")
            surface.blit(def_equip_pic, (3*c.PIXEL_GRID, 1*c.PIXEL_GRID))

        yk_atr = self.img_list.get_txt(m_item["y_key"])
        bk_atr = self.img_list.get_txt(m_item["b_key"])
        rk_atr = self.img_list.get_txt(m_item["r_key"])
        co_atr = self.img_list.get_txt(m_item["coin"])

        surface.blit(st_img, (1*c.PIXEL_GRID+16, 0*c.PIXEL_GRID+16))
        surface.blit(yk_atr, (1*c.PIXEL_GRID+16, 0*c.PIXEL_GRID+16))
        surface.blit(st_img, (1*c.PIXEL_GRID+16, 1*c.PIXEL_GRID+16))
        surface.blit(bk_atr, (1*c.PIXEL_GRID+16, 1*c.PIXEL_GRID+16))
        surface.blit(st_img, (1*c.PIXEL_GRID+16, 2*c.PIXEL_GRID+16))
        surface.blit(rk_atr, (1*c.PIXEL_GRID+16, 2*c.PIXEL_GRID+16))
        surface.blit(st_img, (1*c.PIXEL_GRID+16, 3*c.PIXEL_GRID+16))
        surface.blit(co_atr, (1*c.PIXEL_GRID+16, 3*c.PIXEL_GRID+16))



    # 走路动作,pos位置，key方向
    def fresh_walk(self, pos, key, num):
        surface = self.active_screen
        
        pos_r = (pos[0] * c.PIXEL_GRID, pos[1] * c.PIXEL_GRID)
        rect_r = (num * c.PIXEL_GRID, 0, c.PIXEL_GRID, c.PIXEL_GRID)
        if key == c.KEY_UP:
            surface.blit(self.img_list.get_img("hero_up_d"), pos_r, rect_r)
        elif key == c.KEY_DOWN:
            surface.blit(self.img_list.get_img("hero_down_d"), pos_r, rect_r)
        elif key == c.KEY_LEFT:
            surface.blit(self.img_list.get_img("hero_left_d"), pos_r, rect_r)
        elif key == c.KEY_RIGHT:
            surface.blit(self.img_list.get_img("hero_right_d"), pos_r, rect_r)

    # 负责转向
    def fresh_turn(self, pos, key):
        surface = self.active_screen
        pos_r = (pos[0] * c.PIXEL_GRID, pos[1] * c.PIXEL_GRID)
        if key == c.KEY_UP:
            surface.blit(self.img_list.get_img("hero_up_s"), pos_r)
        elif key == c.KEY_DOWN:
            surface.blit(self.img_list.get_img("hero_down_s"), pos_r)
        elif key == c.KEY_LEFT:
            surface.blit(self.img_list.get_img("hero_left_s"), pos_r)
        elif key == c.KEY_RIGHT:
            surface.blit(self.img_list.get_img("hero_right_s"), pos_r)
    # 开铁门动作
    def fresh_open(self, pos, door_type, num):
        surface = self.active_screen
        pos_r = (pos[0] * c.PIXEL_GRID, pos[1] * c.PIXEL_GRID)
        rect_c = (0, num*c.PIXEL_GRID, c.PIXEL_GRID, c.PIXEL_GRID)
        st_img = self.img_list.get_img("b_stone_s")

        if door_type == c.MAP_IRON_RAIL:
            surface.blit(st_img, pos_r)
            surface.blit(self.img_list.get_img("iron_rail_d"), pos_r, rect_c)
        elif door_type == c.MAP_DOOR_YELLOW:
            surface.blit(st_img, pos_r)
            surface.blit(self.img_list.get_img("door_yellow_d"), pos_r, rect_c)
        elif door_type == c.MAP_DOOR_BLUE:
            surface.blit(st_img, pos_r)
            surface.blit(self.img_list.get_img("door_blue_d"), pos_r, rect_c)
        elif door_type == c.MAP_DOOR_RED:
            surface.blit(st_img, pos_r)
            surface.blit(self.img_list.get_img("door_red_d"), pos_r, rect_c)


    # 展示战斗面板
    def fresh_atk_pane(self, mons, hero):
        surface = self.screen.subsurface(c.ATKPANE_RECT)

        # 绘制背景
        self.show_background([c.ATKPANE_W_G, c.ATKPANE_H_G], self.img_list.get_img("b_stone_s"), surface)

        # 装配属性
        mos_pic = None
        if mons.NAME == "slime-green":
            mos_pic = self.img_list.get_img("monster_sg_s")
        elif mons.NAME == "slime-red":
            mos_pic = self.img_list.get_img("monster_sr_s")
        elif mons.NAME == "slime-black":
            mos_pic = self.img_list.get_img("monster_sb_s")
        elif mons.NAME == "bat-first":
            mos_pic = self.img_list.get_img("monster_bf_s")
        elif mons.NAME == "bat-second":
            mos_pic = self.img_list.get_img("monster_bs_s")
        elif mons.NAME == "bat-third":
            mos_pic = self.img_list.get_img("monster_bt_s")
        elif mons.NAME == "skull-first":
            mos_pic = self.img_list.get_img("monster_skullf_s")
        elif mons.NAME == "skull-second":
            mos_pic = self.img_list.get_img("monster_skulls_s")
        elif mons.NAME == "skull-third":
            mos_pic = self.img_list.get_img("monster_skullt_s")
        elif mons.NAME == "mummy-first":
            mos_pic = self.img_list.get_img("monster_mummyf_s")
        elif mons.NAME == "wizard-first":
            mos_pic = self.img_list.get_img("monster_wzf_s")
        elif mons.NAME == "wizard-second":
            mos_pic = self.img_list.get_img("monster_wzs_s")
        elif mons.NAME == "night-first":
            mos_pic = self.img_list.get_img("monster_nightf_s")
        elif mons.NAME == "guard-first":
            mos_pic = self.img_list.get_img("monster_guardf_s")
        elif mons.NAME == "stonem-first":
            mos_pic = self.img_list.get_img("monster_stonemf_s")
        elif mons.NAME == "slimehuman-first":
            mos_pic = self.img_list.get_img("monster_slimeh_s")

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

        if mons.HP <= 0:
            # 展示战利品
            item_txt = "Get: exp: " + str(mons.ITEMS["exp"]) + ", coin:" + str(mons.ITEMS["coin"])
            surface.blit(self.img_list.get_sta_txt(item_txt, "small"),
                         (0 * c.PIXEL_GRID + c.ATKPANE_REL, 6 * c.PIXEL_GRID + c.ATKPANE_REL))

    def fresh_get_pane(self, txt):
        surface = self.screen.subsurface(c.GETPANE_RECT)

        # 刷新背板
        self.show_background([c.GETPANE_W_G, c.GETPANE_H_G], self.img_list.get_img("b_stone_s"), surface)

        # 绘制状态
        txt_i = self.img_list.get_sta_txt(txt, "small")
        surface.blit(txt_i, (0, 1*c.PIXEL_GRID))

    # 展示对话面板
    def fresh_talk_pane(self, talk_txt):
        surface = self.screen.subsurface(c.TALKPANE_RECT)
        title = self.img_list.get_sta_txt("TALK:", "small")

        # 刷新背板
        self.show_background([c.TALKPANE_W_G, c.TALKPANE_H_G], self.img_list.get_img("b_stone_s"), surface)
        pass
        # 绘制状态
        surface.blit(title, (1*c.PIXEL_GRID, 1*c.PIXEL_GRID))
        for i in range(3):
            txt_s = self.img_list.get_sta_txt(talk_txt[i], "small")
            surface.blit(txt_s, (1 * c.PIXEL_GRID, (2 + i) * c.PIXEL_GRID))

    # index指示箭头位置
    def fresh_trade_pane(self, ni_list, index):
        surface = self.screen.subsurface(c.TRAPANE_RECT)
        ni_l = len(ni_list)
        title = self.img_list.get_sta_txt("TRADE:", "small")

        # 刷新背板
        self.show_background([c.TRAPANE_W_G, c.TRAPANE_H_G], self.img_list.get_img("b_stone_s"), surface)

        # 绘制状态
        surface.blit(title, (1*c.PIXEL_GRID, 0))
        surface.blit(self.img_list.get_img("arrow_r_s"), (0*c.PIXEL_GRID, (1+index)*c.PIXEL_GRID))
        # 展示可选项
        for i in range(ni_l):
            str_item = ni_list[i]["name"] + " cost: " + ni_list[i]["cost"]+","+str(ni_list[i]["how_much"])
            txt_i = self.img_list.get_sta_txt(str_item, "small")
            surface.blit(txt_i, (1*c.PIXEL_GRID, (1+i)*c.PIXEL_GRID))




    # 刷洗图层
    def update_all(self, hero_pos, key_d):
        self.draw_sta_pane()
        self.fresh_title()
        self.fresh_hero_pane()
        self.fresh_item_pane()
        self.fresh_layer()
        self.fresh_hero(hero_pos, key_d)
        pg.display.update()