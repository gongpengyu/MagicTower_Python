__author__ = "scarecrow_gpy"
# 提供一些小工具
import os
import pygame as pg
from . import constants as c

class Tool():
    def __init__(self):
        pass


    # 递归获取指定路径下的文件名，以（key,value)形式返回
    # key为文件名，value为相对路径
    @staticmethod
    def list_file(now_path, dict = {}):
        for name in os.listdir(now_path):
            dir = os.path.join(now_path, name)
            if os.path.isdir(dir):
                Tool.list_file(dir, dict)
            else:
                # 提取文件名
                data_name, _ = os.path.splitext(name)
                dict[data_name] = dir


    # 获取指定文件夹下所有文件，以key=文件名，value=path形式保存
    # 该方法只能运行于根目录下
    @staticmethod
    def get_dict_resource_path():
        re_dict = {}
        Tool.list_file("resources", re_dict)
        return re_dict

    # 获取data文件夹下所有文件的路径字典
    @staticmethod
    def get_dict_data_path():
        data_dict = {}
        Tool.list_file(os.path.join("source", "data"), data_dict)
        return data_dict

    # 生成用于切换图片的迭代器
    @staticmethod
    def animate_count(num):
        a = 0
        yield a

        while True:
            if a < num - 1:
                a += 1
            else:
                a = 0
            yield a

    @staticmethod
    def get_abs_pos(rl_pos, rl_origin):
        return [rl_origin[0]+rl_pos[0], rl_origin[1]+rl_pos[1]]

    @staticmethod
    def get_obj_absrect(rl_pos, flag="active"):
        if flag == "active":
            return [
                (rl_pos[0] + c.ACT_G_POINTX) * c.PIXEL_GRID,
                (rl_pos[1] + c.ACT_G_POINTY) * c.PIXEL_GRID,
                c.PIXEL_GRID,
                c.PIXEL_GRID
            ]

    @staticmethod
    def change_xy_pos(pos):
        return [pos[1], pos[0]]

pg.init()


if __name__ == "__main__":
    pass