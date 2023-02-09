import game

quests_file = "quests"
players_file = "players_list"
quests_dict = game.load_quests_from_file(quests_file)
players_dict = game.load_players_from_file(players_file) 

if __name__ == "__main__":
    player_name = game.input_name()
    rigth_answers_count = 0
    for index, quest in enumerate(quests_dict, 1):
        answers = game.shuffle_answers(quests_dict, index)
        game.print_quests(quests_dict, answers, index)
        player_ans = 0
        while player_ans <= 0 or player_ans > 4:
            player_ans = int(input("Please, input number between 1 and 4: "))
        if game.check_answer(quests_dict, answers, index, player_ans - 1):
            print("Correct answer !")
            rigth_answers_count += 1
        else:
            print("Incorrect answer !")
            print(f"Correct answer was {quests_dict[index][int(quests_dict[index][5])][2::]}")
        print("-----------------")        
    print(f"The number of correct answers is {rigth_answers_count}")    
    game.store_player_result(players_dict, players_file, player_name, rigth_answers_count)