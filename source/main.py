# 游戏运行的主程序
import pygame as pg
from . import control

def main():
    pg.init()
    game = control.Control()
    game.main()
    pg.quit()
