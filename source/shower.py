# 负责游戏的展示
import pygame as pg
from . import constants as c

class Shower():
    def __init__(self):
        self.screen = None
        self.active_screen = None
        self.hero_screen = None
        self.item_screen = None
        # 初始化
        self.init_shower()

    def init_shower(self):
        pg.display.set_caption(c.ORIGIN_CAPTION)
        self.screen = pg.display.set_mode(c.SCREEN_SIZE)
        self.active_screen = self.screen.subsurface(c.ACT_RECT)
        self.hero_screen = self.screen.subsurface(c.HERO_RECT)
        self.item_screen = self.screen.subsurface(c.ITEM_RECT)