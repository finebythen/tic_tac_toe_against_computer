# game: tic tac toe
# output and playing via terminal

import random
from typing import Dict, List


# dictionaires and lists
dict_game_board = {
    '7': ' ' , '8': ' ' , '9': ' ' ,
    '4': ' ' , '5': ' ' , '6': ' ' ,
    '1': ' ' , '2': ' ' , '3': ' ' 
}
board_keys = [key for key in dict_game_board]


# functions
def change_player(n: str) -> str:
    return "player" if n == "computer" else "computer"

def create_board(d):
    print(f"\n{dict_game_board['7']} | {dict_game_board['8']} | {dict_game_board['9']}")
    print(f"{dict_game_board['4']} | {dict_game_board['5']} | {dict_game_board['6']}")
    print(f"{dict_game_board['1']} | {dict_game_board['2']} | {dict_game_board['3']}\n")

def print_result(n):
    print(f"\nGame Over.\n **** {n} won. ****")

def pick_a_move(l: List[str]) -> str:
    if len(l) > 0:
        rand_num: int = random.randrange(0, len(l))
        return l[rand_num]

# start game
def game():
    active = "player"
    count = 0

    for i in range(10):
        if active == "player":
            create_board(dict_game_board)
            print("It's your turn, player! Which field do you choose?")

            field: str = input("Field: ")

            if dict_game_board[field] == " ":
                dict_game_board[field] = "X"
                count += 1
            else:
                print("\nThat place is already filled!\nMove to which place?")
                continue

            # checking the games score
            if count >= 5:
                if dict_game_board['7'] == dict_game_board['8'] == dict_game_board['9'] != ' ':
                    create_board(dict_game_board)
                    print_result(active)
                    break
                elif dict_game_board['4'] == dict_game_board['5'] == dict_game_board['6'] != ' ':
                    create_board(dict_game_board)
                    print_result(active)
                    break
                elif dict_game_board['1'] == dict_game_board['2'] == dict_game_board['3'] != ' ':
                    create_board(dict_game_board)
                    print_result(active)
                    break
                elif dict_game_board['1'] == dict_game_board['4'] == dict_game_board['7'] != ' ':
                    create_board(dict_game_board)
                    print_result(active)
                    break
                elif dict_game_board['2'] == dict_game_board['5'] == dict_game_board['8'] != ' ':
                    create_board(dict_game_board)
                    print_result(active)
                    break
                elif dict_game_board['3'] == dict_game_board['6'] == dict_game_board['9'] != ' ':
                    create_board(dict_game_board)
                    print_result(active)
                    break 
                elif dict_game_board['7'] == dict_game_board['5'] == dict_game_board['3'] != ' ':
                    create_board(dict_game_board)
                    print_result(active)
                    break
                elif dict_game_board['1'] == dict_game_board['5'] == dict_game_board['9'] != ' ':
                    create_board(dict_game_board)
                    print_result(active)
                    break 

            if count == 9:
                print("\nGame Over.\nIt's a Tie!")

            # change active player
            active = change_player(active)
        else:
            l_available_moves = [key for key, val in dict_game_board.items() if val == " "]
            move = pick_a_move(l_available_moves)
            dict_game_board[move] = "O"
            count += 1

            # checking the games score
            if count >= 5:
                if dict_game_board['7'] == dict_game_board['8'] == dict_game_board['9'] != ' ':
                    create_board(dict_game_board)
                    print_result(active)
                    break
                elif dict_game_board['4'] == dict_game_board['5'] == dict_game_board['6'] != ' ':
                    create_board(dict_game_board)
                    print_result(active)
                    break
                elif dict_game_board['1'] == dict_game_board['2'] == dict_game_board['3'] != ' ':
                    create_board(dict_game_board)
                    print_result(active)
                    break
                elif dict_game_board['1'] == dict_game_board['4'] == dict_game_board['7'] != ' ':
                    create_board(dict_game_board)
                    print_result(active)
                    break
                elif dict_game_board['2'] == dict_game_board['5'] == dict_game_board['8'] != ' ':
                    create_board(dict_game_board)
                    print_result(active)
                    break
                elif dict_game_board['3'] == dict_game_board['6'] == dict_game_board['9'] != ' ':
                    create_board(dict_game_board)
                    print_result(active)
                    break 
                elif dict_game_board['7'] == dict_game_board['5'] == dict_game_board['3'] != ' ':
                    create_board(dict_game_board)
                    print_result(active)
                    break
                elif dict_game_board['1'] == dict_game_board['5'] == dict_game_board['9'] != ' ':
                    create_board(dict_game_board)
                    print_result(active)
                    break 

            if count == 9:
                print("\nGame Over.\nIt's a Tie!")

            # change active player
            active = change_player(active)

    # asking for replay
    restart = input("Do want to play Again?(y/n)").lower()
    if restart == "y":
        for key in board_keys:
            dict_game_board[key] = " "

        game()

if __name__ == "__main__":
    game()
