import random

PLAYER_NUM = 2
card_type = 4
action_list = ["抽卡", "协会", "建造", "赞助商"]
card_list = ["动物", "抽卡", "协会", "建造", "赞助商"]
map_list = ["1.观测塔", "2.户外营地", "3.银湖", "4.商业港口", "5.主题餐厅", "6.研究院", "7.冰激凌甜品店", "8.好莱坞山"]

def print_action():
    action_list = ["抽卡", "协会", "建造", "赞助商"]
    result = random.sample(range(1,5), 4)
    return result

def print_card():
    card_num = 4
    action_list = ["动物", "抽卡", "协会", "建造", "赞助商"]
    result = random.sample(range(1,21), 3 * PLAYER_NUM)
    return result

def print_map():
    map_list = ["1.观测塔", "2.户外营地", "3.银湖", "4.商业港口", "5.主题餐厅", "6.研究院", "7.冰激凌甜品店", "8.好莱坞山"]
    result = random.sample(range(1,9), 2 * PLAYER_NUM)
    return result

if __name__ == "__main__":
    map = print_map()
    card = print_card()
    action = []
    print(map)
    print(card)
    for i in range(PLAYER_NUM):
        action.append(print_action())

    for i in range(PLAYER_NUM):
        print("玩家%d:" % i)
        print("你的特殊行动卡牌是：")
        for j in card[i*3:i*3+3]:
            print(card_list[int((j-1)/card_type)] + str(1 + (j-1) % card_type))
        print("")
        
        print("你的地图是：")
        for j in map[i*2:i*2+2]:
            print(map_list[j-1])
        print("")
        
        print("你的行动顺序是：")
        for i in action[i]:
            print(action_list[i-1])
        print("")
