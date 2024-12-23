from Input_helper import get_input
import re

def parse(d):
    board = [ list(b.replace("\n", "")) for b in d]
    return board

def find_char(char, board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == char:
                return i, j
    return None

def calculate_t(board):
    start = find_char("S", board)
    end = find_char("E", board)
    curr_x, curr_y = start
    board[curr_x][curr_y] = 0

    steps = [(1,0), (0,1), (-1,0), (0,-1)]
    sum = 0
    while curr_x != end[0] or curr_y != end[1]:
        # print(*board, sep="\n")
        # print("\n")
        for step in steps:
            now_x, now_y = curr_x + step[0], curr_y + step[1]
            if board[now_x][now_y] == "." and (now_x != curr_x or now_y != curr_y):
                sum += 1
                board[now_x][now_y] = sum
                curr_x, curr_y = now_x, now_y
                break
            elif board[now_x][now_y] == "E":
                board[now_x][now_y] = sum + 1
                return board
    return board

def calc_szyb(board):
    steps = [(2, 0), (0, 2)]
    sum = 0
    # b = {}
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != "#":
                for step in steps:
                    new_x, new_y = step[0] + i, step[1] + j
                    if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and board[new_x][new_y] != '#' :
                        a = board[new_x][new_y], board[i][j]
                        faster = abs(int(board[new_x][new_y]) -int(board[i][j])) - 2
                        # if faster > 0:
                        #     if b.get(faster) is None:
                        #         b[faster] = 1
                        #     else:
                        #         b[faster] += 1
                        if faster >= 100:
                            sum += 1
    return sum



def main():
    get_input(20)
    file = open("input_day_20", "r")
    lines = file.readlines()
    board = parse(lines)
    new_board = calculate_t(board)
    return calc_szyb(new_board)


#1337



if __name__ == "__main__":
    print(main())
