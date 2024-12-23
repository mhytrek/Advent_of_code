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
    path = [(curr_x, curr_y), (end[0], end[1])]
    while curr_x != end[0] or curr_y != end[1]:
        for step in steps:
            now_x, now_y = curr_x + step[0], curr_y + step[1]
            if board[now_x][now_y] == "." and (now_x != curr_x or now_y != curr_y):
                sum += 1
                board[now_x][now_y] = sum
                path.append((now_x, now_y))
                curr_x, curr_y = now_x, now_y
                break
            elif board[now_x][now_y] == "E":
                board[now_x][now_y] = sum + 1
                return board, path
    return board, path

def calc_szyb(path, board):
    sum = 0
    # b = {}
    for i in range(len(path)-1):
        for j in range(i + 1, len(path)):
            x,y = abs(path[i][0] - path[j][0]), abs(path[i][1] - path[j][1])
            if x + y <= 20:
                faster = abs(int(board[path[i][0]][path[i][1]]) - int(board[path[j][0]][path[j][1]])) - x - y
                # if faster >= 50:
                #     if b.get(faster) is None:
                #         b[faster] = 1
                #     else:
                #         b[faster] += 1
                if faster >= 100:
                    sum += 1
    # print(b)
    return sum



def main():
    get_input(20)
    file = open("input_day_20", "r")
    lines = file.readlines()
    board = parse(lines)
    new_board, path = calculate_t(board)
    return calc_szyb(path,new_board)





if __name__ == "__main__":
    print(main())
