class Npc():
    def __init__(self, t_dict):
        self.talk_word = t_dict["talk_w"]
        self.have_item = t_dict["items"]

    def to_talk(self):
        # 对获得文本处理
        speak_list = self.talk_word.split("#")
        # 循环输出
        for x in speak_list:
            print(x)