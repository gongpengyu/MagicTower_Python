from source.com import map
from source.com import creature

import os
if __name__ == "__main__":
    layer_path = os.path.join("..", "data", "layer.json")
    mons_path = os.path.join("..", "data", "monster.json")

    now_map = map.Map()
    now_map.layer_path = layer_path
    now_map.init_layer()
    now_layer = now_map.now_layer()
    now_mons_list = creature.CreatureList()
    now_mons_list.mons_path = mons_path
    now_mons_list.init_arlist()
    now_mons_list.init_layer_creature(now_layer)

    print("查询怪物索引号")
    print(now_mons_list.find_mons(now_map.get_now_index(), (6,2)))
    print("获取怪物对象")
    test = now_mons_list.get_mons(now_map.get_now_index(), (6,2))
    print(test)
    print("删除贵啊无对象")
