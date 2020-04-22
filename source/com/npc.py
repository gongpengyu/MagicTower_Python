import os
import json
class NpcList():
    def __init__(self):
        self.npc_path = os.path.join("source", "data", "npc.json")
        self.data_list = None
        self.now_npc = None

        self.init_list()


    def init_list(self):
        with open(self.npc_path, "rb") as f:
            data_str = f.read().decode("utf-8")
            self.data_list = json.loads(data_str)
            print("test")

    def set_npc(self, index, pos):
        s_index = "layer_" + str(index)
        layer_data = self.data_list[s_index]
        for x in layer_data:
            if x["pos"][0] == pos[0] and x["pos"][1] == pos[1]:
                self.now_npc = x

    def talk(self):
        word = self.now_npc["word"]
        for x in word:
            print(x)

    # item_price为含有商品价格的dict
    def trade(self, item_price, hero):
        if item_price["cost"] == "coin":
            if hero.ITEMS["coin"] < item_price["how_much"]:
                return False
            else:
                hero.ITEMS["coin"] -= item_price["how_much"]
                hero.use_trade_item(item_price["name"])
                return True
        elif item_price["cost"] == "exp":
            if hero.EXP < item_price["how_much"]:
                return False
            else:
                hero.EXP -= item_price["how_much"]
                hero.use_trade_item(item_price["name"])
                return True

    # n_items为物品，step为上涨价格
    def up_price(self, n_items, step):
        for x in n_items:
            x["how_much"] += step

