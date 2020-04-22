import os
import json
class Map():
    def __init__(self):
        self.layer_path = os.path.join("source", "data", "layer.json")
        self.layer_list = []
        # now_index指示当前图层索引号
        self.now_index = None

        # 初始化
        self.init_layer()

    # 获取当前图层索引
    def get_now_index(self):
        return self.now_index

    # 将所有json中数据转换成layer_list
    def init_layer(self):
        with open(self.layer_path, "r") as f:
            layer_data = json.load(f)
            for key in layer_data:
                self.layer_list.append(layer_data[key])
            self.now_index = 10

    # 获取上一层地图数据
    def pre_layer(self):
        if self.now_index == 0:
            return None
        else:
            self.now_index -= 1
            return self.layer_list[self.now_index]

    # 获取下一图层数据
    def next_layer(self):
        if self.now_index == len(self.layer_list)-1:
            return None
        else:
            self.now_index += 1
            return self.layer_list[self.now_index]

    # 获取当前图层信息
    def now_layer(self):
        # print("now_layer:", self.now_index)

        if self.now_index is None:
            print(type(self.now_layer))
            print("now_index is None")
        else:
            return self.layer_list[self.now_index]

    # 修改当前图层信息,pos指示图层下标(h_x,w_y);
    # value修改的值
    def update_layer(self, pos, value):
        now_layer = self.now_layer()
        now_layer[pos[0]][pos[1]] = value

    # 获取当前图层某点value,
    def get_value_nowlayer(self, pos):
        now_layer = self.now_layer()
        return now_layer[pos[0]][pos[1]]
