# 对主角提供加成、武器、装备等效果
# event主要作用于map,还需要思考如何使用
# exist指示物品是快消品，还是可持有
# name有唯一标识的常量


ITEM_RED_MEDICINE = {
    "add_hp": 150,
    "exist": False
}
ITEM_BLUE_MEDICINE = {
    "add_hp": 400,
    "exist": False
}
ITEM_RED_GEM = {
    "add_atk": 2,
    "exist": False
}
ITEM_BLUE_GEM = {
    "add_def": 2,
    "exist": False
}
ITEM_AGI_GEM = {
    "add_agi": 1,
    "exist": False
}
ITEM_WEAK_RETURN = {
    "be_normal": True,
    "exist": False
}
ITEM_POISON_RETURN = {
    "be_normal": True,
    "exist": False
}
ITEM_IRON_SWORD = {
    "name": "iron-sword",
    "equip_class": "add_atk",
    "effect": 10,
    "exist": True
}
ITEM_SILVER_SWORD = {
    "name": "silver-sword",
    "equip_class": "add_atk",
    "effect": 20,
    "exist": True
}
ITEM_IRON_EQUIP = {
    "name": "iron-equip",
    "equip_class": "add_def",
    "effect": 10,
    "exist": True
}
ITEM_UP_LEVEL = {
    "add_lv": 1,
    "exist": False
}

