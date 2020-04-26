# 数据字典

#启动参数
ORIGIN_CAPTION = "Magic Tower"
PIXEL_GRID = 32
# 图层指示参数
L_G_POINTX = 12
L_G_POINTY = 0
L_W_G = 2
L_H_G = 1
L_RECT = (L_G_POINTX*PIXEL_GRID, L_G_POINTY*PIXEL_GRID, L_W_G*PIXEL_GRID, L_H_G*PIXEL_GRID)

# 总界面screen参数
SCREEN_G_POINTX = 0
SCREEN_G_POINTY = 0
SCREEN_W_G = 20
SCREEN_H_G = 15
SCREEN_WIDTH = SCREEN_W_G * PIXEL_GRID  # 640
SCREEN_HEIGHT = SCREEN_H_G * PIXEL_GRID  # 480
SCREEN_RECT = (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Active活动区参数
ACT_G_POINTX = 6
ACT_G_POINTY = 1
ACT_W_G = 13
ACT_H_G = 13
ACT_POINTX = ACT_G_POINTX * PIXEL_GRID
ACT_POINTY = ACT_G_POINTY * PIXEL_GRID
ACT_WIDTH = ACT_W_G * PIXEL_GRID
ACT_HEIGHT = ACT_H_G * PIXEL_GRID
ACT_RECT = (ACT_POINTX, ACT_POINTY, ACT_WIDTH, ACT_HEIGHT)

# 人物区参数
HERO_G_POINTX = 1
HERO_G_POINTY = 1
HERO_W_G = 4
HERO_H_G = 8
HERO_POINTX = HERO_G_POINTX * PIXEL_GRID
HERO_POINTY = HERO_G_POINTY * PIXEL_GRID
HERO_WIDTH = HERO_W_G * PIXEL_GRID
HERO_HEIGHT = HERO_H_G * PIXEL_GRID
HERO_RECT = (HERO_POINTX, HERO_POINTY, HERO_WIDTH, HERO_HEIGHT)
# 人物参数
HERO_STA = {
    "normal": "正常",
    "weak": "虚弱",
    "poison": "中毒"
}

# 物品区参数
ITEM_G_POINTX = 1
ITEM_G_POINTY = 10
ITEM_W_G = 4
ITEM_H_G = 4
ITEM_POINTX = ITEM_G_POINTX * PIXEL_GRID
ITEM_POINTY = ITEM_G_POINTY * PIXEL_GRID
ITEM_WIDTH = ITEM_W_G * PIXEL_GRID
ITEM_HEIGHT = ITEM_H_G * PIXEL_GRID
ITEM_RECT = (ITEM_POINTX, ITEM_POINTY, ITEM_WIDTH, ITEM_HEIGHT)

# 战斗面板参数
ATKPANE_G_POINTX = 6
ATKPANE_G_POINTY = 5
ATKPANE_W_G = 14
ATKPANE_H_G = 7
ATKPANE_REL = PIXEL_GRID/2
ATKPANE_POINTX = ATKPANE_G_POINTX * PIXEL_GRID - ATKPANE_REL
ATKPANE_POINTY = ATKPANE_G_POINTY * PIXEL_GRID - ATKPANE_REL
ATKPANE_WIDTH = ATKPANE_W_G * PIXEL_GRID
ATKPANE_HEIGHT = ATKPANE_H_G * PIXEL_GRID
ATKPANE_RECT = (ATKPANE_POINTX, ATKPANE_POINTY, ATKPANE_WIDTH, ATKPANE_HEIGHT)

# 初始面板
STPANE_G_POINTX = 7
STPANE_G_POINTY = 4
STPANE_W_G = 6
STPANE_H_G = 6
STPANE_POINTX = STPANE_G_POINTX * PIXEL_GRID
STPANE_POINTY = STPANE_G_POINTY * PIXEL_GRID
STPANE_WIDTH = STPANE_W_G * PIXEL_GRID
STPANE_HEIGHT = STPANE_H_G * PIXEL_GRID
STPANE_RECT = (STPANE_POINTX, STPANE_POINTY, STPANE_WIDTH, STPANE_HEIGHT)

# 获取物品面板
GETPANE_G_POINTX = 8
GETPANE_G_POINTY = 7
GETPANE_W_G = 6
GETPANE_H_G = 2
GETPANE_POINTX = GETPANE_G_POINTX * PIXEL_GRID
GETPANE_POINTY = GETPANE_G_POINTY * PIXEL_GRID
GETPANE_WIDTH = GETPANE_W_G * PIXEL_GRID
GETPANE_HEIGHT = GETPANE_H_G * PIXEL_GRID
GETPANE_RECT = (GETPANE_POINTX, GETPANE_POINTY, GETPANE_WIDTH, GETPANE_HEIGHT)

# 对话面板
TALKPANE_G_POINTX = 7
TALKPANE_G_POINTY = 2
TALKPANE_W_G = 8
TALKPANE_H_G = 6
TALKPANE_POINTX = TALKPANE_G_POINTX * PIXEL_GRID
TALKPANE_POINTY = TALKPANE_G_POINTY * PIXEL_GRID
TALKPANE_WIDTH = TALKPANE_W_G * PIXEL_GRID
TALKPANE_HEIGHT = TALKPANE_H_G * PIXEL_GRID
TALKPANE_RECT = (TALKPANE_POINTX, TALKPANE_POINTY, TALKPANE_WIDTH, TALKPANE_HEIGHT)
# 交易面板
TRAPANE_G_POINTX = 7
TRAPANE_G_POINTY = 8
TRAPANE_W_G = 8
TRAPANE_H_G = 5
TRAPANE_POINTX = TRAPANE_G_POINTX * PIXEL_GRID
TRAPANE_POINTY = TRAPANE_G_POINTY * PIXEL_GRID
TRAPANE_WIDTH = TRAPANE_W_G * PIXEL_GRID
TRAPANE_HEIGHT = TRAPANE_H_G * PIXEL_GRID
TRAPANE_RECT = (TRAPANE_POINTX, TRAPANE_POINTY, TRAPANE_WIDTH, TRAPANE_HEIGHT)

# 地图参数
MAP_B_STONE = 0
MAP_W_STONE = 1
MAP_MAGMA = 2
MAP_UP_FLO = 3
MAP_DOWN_FLO = 4
MAP_IRON_RAIL = 5
MAP_DOOR_YELLOW = 6
MAP_DOOR_BLUE = 7
MAP_DOOR_RED = 8
MAP_GOD_LEFT = 9
MAP_GOD_CENTER = 10
MAP_GOD_RIGHT = 11

# 30-60 为怪物区
MAP_MONS_WZF = 30
MAP_MONS_WZS = 31
MAP_MONS_SG = 40
MAP_MONS_SR = 41
MAP_MONS_SB = 42
MAP_MONS_BATF = 45
MAP_MONS_BATS = 46
MAP_MONS_BATT = 47
MAP_MONS_SKULLF = 50
MAP_MONS_SKULLS = 51
MAP_MONS_SKULLT = 52
MAP_MONS_MUMMYF = 55
MAP_MONS_SLIMEH = 56
MAP_MONS_NIGHTF = 57
MAP_MONS_GUARDF = 58
MAP_MONS_STONEM = 59
MAP_MONS_M = 60
# 61-80 为npc
MAP_NPC_RED = 61
MAP_NPC_BLUE = 62
MAP_NPC_YELLOW = 63
MAP_NPC_M = 80
# 81-100为可拾取的物品
MAP_ITEM_RM = 81
MAP_ITEM_BM = 82
MAP_ITEM_RW = 83
MAP_ITEM_RP = 84
MAP_ITEM_RG = 85
MAP_ITEM_BG = 86
MAP_ITEM_AG = 87
MAP_ITEM_YK = 89
MAP_ITEM_BK = 90
MAP_ITEM_RK = 91
MAP_ITEM_UL = 92
MAP_ITEM_IS = 93
MAP_ITEM_SS = 94
MAP_ITEM_IE = 95

MAP_ITEM_M = 100

# 键盘映射
KEY_UP =    1001
KEY_DOWN =  1002
KEY_LEFT =  1003
KEY_RIGHT = 1004
KEY_STOP = 1005

KEY_TOATK = 1009
KEY_GITEM = 1010
KEY_TRADE = 1011
KEY_TOOPEN = 1012


# 素材参数
EVE_DOWN_FLOOR = "bg-Down_floor"
EVENT_DOOR = "bg-Door01"
EVENT_LAVA = "bg-Lava01"
EVENT_OTHER = "bg-Other03"
EVENT_WALL = "bg-Wall01"
EVENT_ICE = "bg-Ice"
EVE_UP_FLOOR = "bg-Up_floor"
EVE_ACTOR = "hero-Braver01"
MONS_1 = "Monster01"
MONS_2 = "Monster02"
MONS_3 = "Monster03"
MONS_4 = "Monster04"
MONS_5 = "Monster05"
MONS_6 = "Monster06"
MONS_7 = "Monster07"
MONS_8 = "Monster08"
MONS_9 = "Monster09"
MONS_10 = "Monster10"
MONS_11 = "Monster11"
NPC_1 = "NPC01"
ITEM_01 = "Item01"
ITEM_02 = "Item02"
ITEM_05 = "Item05"
ITEM_08 = "Item08"
ITEM_10 = "Item10"
ITEM_GEM = "Item-Gem01"

BG_STONE_IMG = {
    "super": EVENT_WALL,
    "pointx": 0,
    "pointy": 0,
    "sta_rect": (0, 0, 32, 32),
    "sta_wh_g": (1, 1)
}
WHITE_STONE_IMG = {
    "super": EVENT_WALL,
    "pointx": 64,
    "pointy": 0,
    "sta_rect": (64, 0, 32, 32),
    "sta_wh_g": (1, 1)
}
BALCK_STONE_IMG = {
    "super": EVENT_ICE,
    "pointx": 0,
    "pointy": 0,
    "sta_rect": (0, 0, 32, 32),
    "sta_wh_g": (1,1)
}
MAGMA_IMG = {
    "super": EVENT_LAVA,
    "pointx": 0,
    "pointy": 0,
    "dyn_rect": (0, 0, 128, 32),
    "dyn_wh_g": (4, 1)
}
UP_FLOOR_IMG = {
    "super": EVE_UP_FLOOR,
    "pointx": 0,
    "pointy": 0,
    "sta_rect": (0, 0, 32, 32),
    "sta_wh_g": (1, 1)
}
DOWN_FLOOR_IMG = {
    "super": EVE_DOWN_FLOOR,
    "pointx": 0,
    "pointy": 0,
    "sta_rect": (0, 0, 32, 32),
    "sta_wh_g": (1, 1)
}
IRON_RAIL_IMG = {
    "super": EVENT_WALL,
    "pointx": 96,
    "pointy": 0,
    "sta_rect": (96, 0, 32, 32),
    "sta_wh_g": (1, 1),
    "dyn_rect": (96, 0, 32, 128),
    "dyn_wh_g": (1, 4)
}
GOD_LEFT_IMG = {
    "super": EVENT_OTHER,
    "pointx": 0,
    "pointy": 0,
    "sta_rect": (0, 0, 32, 32),
    "sta_wh_g": (1, 1)
}
GOD_CENTER_IMG = {
    "super": EVENT_OTHER,
    "pointx": 32,
    "pointy": 0,
    "sta_rect": (32, 0, 32, 32),
    "sta_wh_g": (1, 1)
}
GOD_RIGHT_IMG = {
    "super": EVENT_OTHER,
    "pointx": 64,
    "pointy": 0,
    "sta_rect": (64, 0, 32, 32),
    "sta_wh_g": (1, 1)
}
RETURN_WEAK_IMG = {
    "super": ITEM_02,
    "pointx": 64,
    "pointy": 0,
    "sta_rect": (64, 0, 32, 32),
    "sta_wh_g": (1, 1)
}
RETURN_POI_IMG = {
    "super": ITEM_02,
    "pointx": 96,
    "pointy": 0,
    "sta_rect": (96, 0, 32, 32),
    "sta_wh_g": (1, 1)
}
HERO_UP_IMG = {
    "super": EVE_ACTOR,
    "pointx": 0,
    "pointy": 96,
    "sta_rect": (0, 96, 32, 32),
    "sta_wh_g": (1, 1),
    "dyn_rect": (0, 96, 128, 32),
    "dyn_wh_g": (4, 1)
}
HERO_DOWN_IMG = {
    "super": EVE_ACTOR,
    "pointx": 0,
    "pointy": 0,
    "sta_rect": (0, 0, 32, 32),
    "sta_wh_g": (1, 1),
    "dyn_rect": (0, 0, 128, 32),
    "dyn_wh_g": (4, 1)
}
HERO_LEFT_IMG = {
    "super": EVE_ACTOR,
    "pointx": 0,
    "pointy": 32,
    "sta_rect": (0, 32, 32, 32),
    "sta_wh_g": (1, 1),
    "dyn_rect": (0, 32, 128, 32),
    "dyn_wh_g": (4, 1)
}
HERO_RIGHT_IMG = {
    "super": EVE_ACTOR,
    "pointx": 0,
    "pointy": 64,
    "sta_rect": (0, 64, 32, 32),
    "sta_wh_g": (1, 1),
    "dyn_rect": (0, 64, 128, 32),
    "dyn_wh_g": (4, 1)
}
DOOR_YELLOW_IMG = {
    "super": EVENT_DOOR,
    "pointx": 0,
    "pointy": 0,
    "sta_rect": (0, 0, 32, 32),
    "sta_wh_g": (1, 1),
    "dyn_rect": (0, 0, 32, 128),
    "dyn_wh_g": (1, 4)
}
DOOR_BLUE_IMG = {
    "super": EVENT_DOOR,
    "pointx": 32,
    "pointy": 0,
    "sta_rect": (32, 0, 32, 32),
    "sta_wh_g": (1, 1),
    "dyn_rect": (32, 0, 32, 128),
    "dyn_wh_g": (1, 4)
}
DOOR_RED_IMG = {
    "super": EVENT_DOOR,
    "pointx": 64,
    "pointy": 0,
    "sta_rect": (64, 0, 32, 32),
    "sta_wh_g": (1, 1),
    "dyn_rect": (64, 0, 32, 128),
    "dyn_wh_g": (1, 4)
}

MONS_SLING_IMG = {
    "super": MONS_1,
    "pointx": 0,
    "pointy": 0,
    "sta_rect": (0, 0, 32, 32),
    "sta_wh_g": (1, 1),
    "dyn_rect": (0, 0, 128, 32),
    "dyn_wh_g": (4, 1)
}
MONS_SLINR_IMG = {
    "super": MONS_1,
    "pointx": 0,
    "pointy": 32,
    "sta_rect": (0, 32, 32, 32),
    "sta_wh_g": (1, 1),
    "dyn_rect": (0, 32, 128, 32),
    "dyn_wh_g": (4, 1)
}
MONS_SLINB_IMG = {
    "super": MONS_1,
    "pointx": 0,
    "pointy": 64,
    "sta_rect": (0, 64, 32, 32),
    "sta_wh_g": (1, 1),
    "dyn_rect": (0, 64, 128, 32),
    "dyn_wh_g": (4, 1)
}
MONS_BATF_IMG = {
    "super": MONS_3,
    "pointx": 0,
    "pointy": 0,
    "sta_rect": (0, 0, 32, 32),
    "sta_wh_g": (1, 1),
    "dyn_rect": (0, 0, 128, 32),
    "dyn_wh_g": (4, 1)
}
MONS_BATS_IMG = {
    "super": MONS_3,
    "pointx": 0,
    "pointy": 32,
    "sta_rect": (0, 32, 32, 32),
    "sta_wh_g": (1, 1),
    "dyn_rect": (0, 32, 128, 32),
    "dyn_wh_g": (4, 1)
}
MONS_BATT_IMG = {
    "super": MONS_3,
    "pointx": 0,
    "pointy": 64,
    "sta_rect": (0, 64, 32, 32),
    "sta_wh_g": (1, 1),
    "dyn_rect": (0, 64, 128, 32),
    "dyn_wh_g": (4, 1)
}
MONS_MUMMYF_IMG = {
    "super": MONS_9,
    "pointx": 0,
    "pointy": 0,
    "sta_rect": (0, 0, 32, 32),
    "sta_wh_g": (1, 1),
    "dyn_rect": (0, 0, 128, 32),
    "dyn_wh_g": (4, 1)
}
MONS_SKULLF_IMG = {
    "super": MONS_2,
    "pointx": 0,
    "pointy": 0,
    "sta_rect": (0, 0, 32, 32),
    "sta_wh_g": (1, 1),
    "dyn_rect": (0, 0, 128, 32),
    "dyn_wh_g": (4, 1)
}
MONS_SKULLS_IMG = {
    "super": MONS_2,
    "pointx": 0,
    "pointy": 32,
    "sta_rect": (0, 32, 32, 32),
    "sta_wh_g": (1, 1),
    "dyn_rect": (0, 32, 128, 32),
    "dyn_wh_g": (4, 1)
}
MONS_SKULLT_IMG = {
    "super": MONS_2,
    "pointx": 0,
    "pointy": 64,
    "sta_rect": (0, 64, 32, 32),
    "sta_wh_g": (1, 1),
    "dyn_rect": (0, 64, 128, 32),
    "dyn_wh_g": (4, 1)
}
MONS_NIGHTF_IMG = {
    "super": MONS_7,
    "pointx": 0,
    "pointy": 0,
    "sta_rect": (0, 0, 32, 32),
    "sta_wh_g": (1, 1),
    "dyn_rect": (0, 0, 128, 32),
    "dyn_wh_g": (4, 1)
}
MONS_GUARDF_IMG = {
    "super": MONS_5,
    "pointx": 0,
    "pointy": 0,
    "sta_rect": (0, 0, 32, 32),
    "sta_wh_g": (1, 1),
    "dyn_rect": (0, 0, 128, 32),
    "dyn_wh_g": (4, 1)
}
MONS_WZF_IMG = {
    "super": MONS_6,
    "pointx": 0,
    "pointy": 0,
    "sta_rect": (0, 0, 32, 32),
    "sta_wh_g": (1, 1),
    "dyn_rect": (0, 0, 128, 32),
    "dyn_wh_g": (4, 1)
}
MONS_WZS_IMG = {
    "super": MONS_6,
    "pointx": 0,
    "pointy": 32,
    "sta_rect": (0, 32, 32, 32),
    "sta_wh_g": (1, 1),
    "dyn_rect": (0, 32, 128, 32),
    "dyn_wh_g": (4, 1)
}
MONS_STONEM_IMG = {
    "super": MONS_10,
    "pointx": 0,
    "pointy": 0,
    "sta_rect": (0, 0, 32, 32),
    "sta_wh_g": (1, 1),
    "dyn_rect": (0, 0, 128, 32),
    "dyn_wh_g": (4, 1)
}
MONS_SLIMEH_IMG = {
    "super": MONS_11,
    "pointx": 0,
    "pointy": 0,
    "sta_rect": (0, 0, 32, 32),
    "sta_wh_g": (1, 1),
    "dyn_rect": (0, 0, 128, 32),
    "dyn_wh_g": (4, 1)
}
NPC_RED_IMG = {
    "super": NPC_1,
    "pointx": 0,
    "pointy": 32,
    "sta_rect": (0, 32, 32, 32),
    "sta_wh_g": (1,1),
    "dyn_rect": (0, 32, 128, 32),
    "dyn_wh_g": (4, 1)
}
NPC_BLUE_IMG = {
    "super": NPC_1,
    "pointx": 0,
    "pointy": 0,
    "sta_rect": (0, 0, 32, 32),
    "sta_wh_g": (1, 1),
    "dyn_rect": (0, 0, 128, 32),
    "dyn_wh_g": (4, 1)
}
NPC_YELLOW_IMG = {
    "super": NPC_1,
    "pointx": 0,
    "pointy": 64,
    "sta_rect": (0, 64, 32, 32),
    "sta_wh_g": (1, 1),
    "dyn_rect": (0, 64, 128, 32),
    "dyn_wh_g": (4, 1)
}


YKEY_IMG = {
    "super": ITEM_01,
    "pointx": 0,
    "pointy": 0,
    "sta_rect": (0, 0, 32, 32),
    "sta_wh_g": (1, 1)
}
BKEY_IMG = {
    "super": ITEM_01,
    "pointx": 32,
    "pointy": 0,
    "sta_rect": (32, 0, 32, 32),
    "sta_wh_g": (1, 1)
}
RKEY_IMG = {
    "super": ITEM_01,
    "pointx": 64,
    "pointy": 0,
    "sta_rect": (64, 0, 32, 32),
    "sta_wh_g": (1, 1)
}
COIN_IMG = {
    "super": ITEM_05,
    "pointx": 96,
    "pointy": 0,
    "sta_rect": (96, 0, 32, 32),
    "sta_wh_g": (1, 1)
}
RED_MEDIF_IMG = {
    "super": ITEM_02,
    "pointx": 0,
    "pointy": 0,
    "sta_rect": (0, 0, 32, 32),
    "sta_wh_g": (1, 1)
}
BLUE_MED_IMG = {
    "super": ITEM_02,
    "pointx": 32,
    "pointy": 0,
    "sta_rect": (32, 0, 32, 32),
    "sta_wh_g": (1, 1)
}
RED_GEM_IMG = {
    "super": ITEM_GEM,
    "pointx": 0,
    "pointy": 0,
    "sta_rect": (0, 0, 32, 32),
    "sta_wh_g": (1, 1)
}
BLUE_GEM_IMG = {
    "super": ITEM_GEM,
    "pointx": 0,
    "pointy": 0,
    "sta_rect": (32, 0, 32, 32),
    "sta_wh_g": (1, 1)
}
AGI_GEM_IMG = {
    "super": ITEM_GEM,
    "pointx": 64,
    "pointy": 0,
    "sta_rect": (64, 0, 32, 32),
    "sta_wh_g": (1, 1)
}
UP_LEVEL_IMG = {
    "super": ITEM_10,
    "pointx": 0,
    "pointy": 0,
    "sta_rect": (0, 0, 32, 32),
    "sta_wh_g": (1, 1)
}
IRON_SWORD_IMG = {
    "super": ITEM_08,
    "pointx": 0,
    "pointy": 0,
    "sta_rect": (0, 0, 32, 32),
    "sta_wh_g": (1, 1)
}
SILVER_SWORD_IMG = {
    "super": ITEM_08,
    "pointx": 32,
    "pointy": 0,
    "sta_rect": (32, 0, 32, 32),
    "sta_wh_g": (1, 1)
}
IRON_EQUIP_IMG = {
    "super": ITEM_08,
    "pointx": 64,
    "pointy": 64,
    "sta_rect": (64, 64, 32, 32),
    "sta_wh_g": (1, 1)
}
ARROW_R_IMG = {
    "super": ITEM_10,
    "pointx": 96,
    "pointy": 32,
    "sta_rect": (96, 32, 32, 32),
    "sta_wh_g": (1, 1)
}

# 颜色参数
ALICE_BLUE = (100, 181, 191)
PURE_BLACK = (0,     0,   0)
PURE_WHITE = (255, 255, 255)