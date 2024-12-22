#function for taken place inputs
def is_place_taken(table_list,row,col):
    if table_list[row][col] != " ":
        return True
    else:
        return False
    
#draws table
def draw_table(size,table_list,letters):
    print("    ",end="")
    for row in range(size):
        print(letters[row],end="   ")
    print()
    print("  ",end="")
    if size == 3: 
        print("------"*(size-1))
    else:
        print("-----"*(size-1))
    for row in range(size):
        print(row+1,end="")
        for col in range(size):
            print(f" | {table_list[row][col]}",end="")
        print(" | ",row+1,end="")
        print()
        print("  ",end="")
        if size == 3: 
            print("------"*(size-1))
        else:
            print("-----"*(size-1))
    print("    ",end="")
    for row in range(size):
        print(letters[row],end="   ")
    print()

def put_small_stone(table_list,player_symbol,positions):
    #changes letters to nums to define columns
    letters_to_num = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6}
    letters = ["A","B","C","D","E","F","G"]
    
    rock_pos = input(f"Player {player_symbol}, please enter the location where you want to place a small stone (like 1A): ")
    while (rock_pos not in positions):
        rock_pos = input("Invalid input try again: ")

    while True:
        try:
            rock_pos_split = []
            for i in rock_pos:
                rock_pos_split.append(i)
                if i.isdigit():
                    rock_pos_split[0] = int(rock_pos_split[0])-1
                else:
                    rock_pos_split[1] = letters_to_num[rock_pos_split[1].upper()]

            if is_place_taken(table_list,rock_pos_split[0],rock_pos_split[1]):
                raise IndexError
        except IndexError or KeyError:
            rock_pos = input("Invalid input try again: ")
            while (rock_pos not in positions):
                rock_pos = input("Invalid input try again: ")
        else:
            break

    table_list[rock_pos_split[0]][rock_pos_split[1]] = "O"

def move_big_stone(size,table_list,player_symbol,pos_player,directions):
    possible_ways_player = [[pos_player[0]+int(direction[0]),pos_player[1]+int(direction[1])] for direction in directions.values() if 0 <= pos_player[0]+int(direction[0]) < size and 0 <= pos_player[1]+int(direction[1]) < size]
    direction = input(f"Player {player_symbol}, please enter the direction you want to move your own big stone (N, S, E, W, NE, NW, SE, SW): ")
    direction = direction.upper()
    while direction not in directions:
        direction = input("Invalid input, try again: ")
        direction = direction.upper()
    new_pos = [0,0]
    while True:
        try:
            new_pos[0] = pos_player[0] + directions[direction][0]
            new_pos[1] = pos_player[1] + directions[direction][1]
            if (new_pos not in possible_ways_player) or is_place_taken(table_list,new_pos[0],new_pos[1]):
                raise IndexError
            else:
                table_list[new_pos[0]][new_pos[1]] = player_symbol
        except KeyError:
            direction = input("Invalid input, try again: ")
            while not direction.isalpha:
                direction = input("Invalid input, try again: ")
            direction = direction.upper()
        except IndexError:
            direction = input("Invalid input, try again: ")
            while not direction.isalpha:
                direction = input("Invalid input, try again: ")
            direction = direction.upper()
        else:
            break
    table_list[pos_player[0]][pos_player[1]] = " "
    table_list[new_pos[0]][new_pos[1]] = player_symbol
    return new_pos

#checks if the opponent can move
def find_winner(table_list,directions,pos_opponent,size,player_symbol):
    move = False
    possible_ways = [[pos_opponent[0]+int(direction[0]),pos_opponent[1]+int(direction[1])] for direction in directions.values() if 0 <= pos_opponent[0]+int(direction[0]) < size and 0 <= pos_opponent[1]+int(direction[1]) < size]

    for ways in possible_ways:
        if not is_place_taken(table_list,ways[0],ways[1]):
            move = True
    if not move:
        return player_symbol
    else:
        return "No winner"


#moves big stones, adds small stones and finds winner
def play(p1_symbol,p2_symbol,size,table_list,letters,directions):
    pos_p1 = [size-1,int(size/2)]
    pos_p2 = [0,int(size/2)]

    #positions for putting stones
    positions = []
    for i in range(size):
        for k in range(size):
            pos = str(i+1) + str(letters[k])
            positions.append(pos)
            pos_lower = str(i+1) + str(letters[k]).lower()
            positions.append(pos_lower)
    
    winner = "No winner"
    while winner == "No winner":
        #p1 moves stone
        pos_p1 = move_big_stone(size,table_list,p1_symbol,pos_p1,directions)
        print()
        draw_table(size,table_list,letters)
        print()
        
        #chech for is there a winner
        winner = find_winner(table_list,directions,pos_p2,size,p1_symbol)
        if winner != "No winner":
            break

        #p1 puts small stone
        put_small_stone(table_list,p1_symbol,positions)
        print()
        draw_table(size,table_list,letters)
        print()

        winner = find_winner(table_list,directions,pos_p2,size,p1_symbol)       
        if winner != "No winner":
            break

        #p2 moves stone
        pos_p2 = move_big_stone(size,table_list,p2_symbol,pos_p2,directions)
        print()
        draw_table(size,table_list,letters)
        print()

        winner = find_winner(table_list,directions,pos_p1,size,p2_symbol)
        if winner != "No winner":
            break

        #p2 puts small stone
        put_small_stone(table_list,p2_symbol,positions)
        print()
        draw_table(size,table_list,letters)
        print()

        winner = find_winner(table_list,directions,pos_p1,size,p2_symbol)
        if winner != "No winner":
            break

    print(f"Player {winner} won the game.")

def main():
    letters = ["A","B","C","D","E","F","G"]
    directions = {'N': [-1, 0], 'S': [1, 0], 'E': [0, 1],'W': [0, -1], 'NE': [-1, 1], 'NW': [-1, -1],'SE': [1, 1], 'SW': [1, -1]}
    p1_symbol = (input("Enter a capital letter to represent player 1 (except O): "))
    if p1_symbol == "i":
        p1_symbol = "I"
    else:
        p1_symbol = p1_symbol.upper()
    while (not p1_symbol.isalpha()) or p1_symbol=="O":
        p1_symbol = (input("Invalid input please try again:"))
        if p1_symbol == "i":
            p1_symbol = "I"
        else:
            p1_symbol = p1_symbol.upper()
    p2_symbol = (input("Enter a capital letter to represent player 2 (except O): "))
    if p2_symbol == "i":
        p2_symbol = "I"
    else:
        p2_symbol = p2_symbol.upper()
    while (not p2_symbol.isalpha()) or p2_symbol=="O" or p1_symbol==p2_symbol:
        p2_symbol = (input("Invalid input please try again:"))
        if p2_symbol == "i":
            p2_symbol = "I"
        else:
            p2_symbol = p2_symbol.upper()
    
    cont="Y"
    while cont.upper() == "Y":
        size = input("Enter the row/column number of the playing field (3, 5, 7): ")
        while size not in ["3","5","7"]:
            size = input("Invalid entry try again: ")
        size = int(size)
        
        table_list = [[" "]*size for i in range(size)]
        table_list[-1][int((size/2))] = p1_symbol
        table_list[0][int((size/2))] = p2_symbol
        draw_table(size,table_list,letters)
        play(p1_symbol,p2_symbol,size,table_list,letters,directions)

        cont = input("Would you like to play again(Y/N)?: ")
        while cont not in "yYnN":
            cont = input("Invalid input try again: ")
        
main()