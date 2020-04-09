# 对主角提供加成、武器、装备等效果
# event主要作用于map,还需要思考如何使用
# exist指示物品是快消品，还是可持有
# name有唯一标识的常量
NA_RED_MED = "red_medicine"
NA_IRON_SW = "iron_sword"

ITEM_RED_MEDICINE = {
    "name": NA_RED_MED,
    "add_hp": 150,
    "exist": False
}
ITEM_IRON_SWORD = {
    "name": NA_IRON_SW,
    "add_atk": 10,
    "exist": True
}

