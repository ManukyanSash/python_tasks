def init_matrix():
    return [['.' for i in range(3)] for j in range(3)]

def select_player(player_bool):
    player_dict = {0: "0",
                   1: "X"}
    return player_dict[player_bool]

def draw(matrix):
    for row in matrix:
        print(*row, sep=" ")
        
def move(matrix, current_player, cell):
    cell_to_index = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),        
    }
    if cell < 0 or cell > 9: 
        print("Please, input number between 1 and 9: ") 
        return   
    row = cell_to_index[cell][0]
    col = cell_to_index[cell][1]
    if matrix[row][col] != '.':
        print("Please, select an empty box ! ")
        return
    matrix[row][col] = current_player
    global is_X
    is_X = not is_X

def check_win(matrix, current_player):
    wining_variants = (matrix[0][0] + matrix[0][1] + matrix[0][2],
                       matrix[1][0] + matrix[1][1] + matrix[1][2],
                       matrix[2][0] + matrix[2][1] + matrix[2][2],
                       matrix[0][0] + matrix[1][0] + matrix[2][0],
                       matrix[0][1] + matrix[1][1] + matrix[2][1],
                       matrix[0][2] + matrix[1][2] + matrix[2][2],
                       matrix[0][0] + matrix[1][1] + matrix[2][2],
                       matrix[0][2] + matrix[1][1] + matrix[2][0]) 
    for vars in wining_variants:
        if vars == 3 * current_player:
            print(f"{current_player} wins !!!")
            global end_game
            end_game = not end_game
            return 
    for row in matrix:
        if '.' in row:
            return
    print("Draw !!!")      
           
if __name__ == "__main__":
    end_game = False
    is_X = True
    matrix = init_matrix()
    draw(matrix)
    while not end_game:
        current_player = select_player(is_X)
        cell = int(input("Please, input number between 1 and 9: "))
        move(matrix, current_player, cell)
        draw(matrix)
        check_win(matrix, current_player)
