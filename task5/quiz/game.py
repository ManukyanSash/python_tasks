import random

def load_quests_from_file(questions_file):
    questions = {}
    with open(questions_file, 'r') as file:
        all_quests_list = file.readlines()
    for index, quest in enumerate(all_quests_list, 1):
        questions[index] = quest.split('. ')
    return questions   

def shuffle_answers(questions_dict, index):
    ans = questions_dict[index][1:5]
    random.shuffle(ans)
    return ans

def print_quests(questions_dict, answers, index):
    print(f"#{index}:", questions_dict[index][0])
    for ans in answers:
        print(ans[2::])
      

def check_answer(quests, shuffled_quests, quest_id, ans):
    if shuffled_quests[ans] == quests[quest_id][int(quests[quest_id][5])]:   
        return True
    return False

def load_players_from_file(players_file):
    all_players = {}
    tmp_list = []
    with open(players_file, 'r') as file:
        tmp_list = file.readlines()
    
    for pl in tmp_list:
        all_players[pl.split(" : ")[0]] = int(pl.split(" : ")[1])   
    return all_players

def input_name():
    name = ""
    while name == "":
        name = input("Please input player name: ")
    return name

def store_player_result(players_dict, players_file, player_name, score):
    players_dict[player_name] = score
    players_dict = sorted(players_dict.items(), key=lambda x:x[1], reverse=True)
    with open(players_file, 'w') as file:
        for index, player in enumerate(players_dict):
            file.write(f'{player[0]} : {player[1]} \n')