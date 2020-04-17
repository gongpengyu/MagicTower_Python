import os
import json
if __name__ == "__main__":
    # 获取npc的json数据
    npc_path = os.path.join("..", "data", "npc.json")

    with open(npc_path, "rb") as f:
        file_str = f.read().decode("utf-8")
        npc_data = json.loads(file_str)
        print(npc_data["layer_0"])
        print(npc_data["layer_1"][0])
        print("test")
        # for key in layer_data:
        #     self.layer_list.append(layer_data[key])
        # self.now_index = 0