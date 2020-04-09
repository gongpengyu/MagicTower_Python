from source.com import map
import os

if __name__ == "__main__":
    test_path = os.path.join("..", "data", "layer.json")
    map = map.Map()
    map.layer_path = test_path

    map.now_layer()

    map.init_layer()
    print(map.now_index)

    map.now_layer()
    print(map.now_index)

    map.pre_layer()
    print(map.now_index)

    map.next_layer()
    print(map.now_index)
    # print(os.path.realpath(".."))