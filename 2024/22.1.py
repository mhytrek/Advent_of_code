from Input_helper import get_input
import re

def parse(d):
    board = [ int(b.replace("\n", "")) for b in d]
    return board


def find_num(board):
    sum = 0
    for num in board:
        for i in range(2000):
            new_num = ((num * 64) ^ num) % 16777216
            new_num = ((new_num // 32) ^ new_num) % 16777216
            new_num = ((new_num * 2048) ^ new_num) % 16777216
            num = new_num
        sum += num
    return sum



def main():
    get_input(22)
    file = open("input_day_22", "r")
    lines = file.readlines()
    board = parse(lines)
    return find_num(board)

#1337



if __name__ == "__main__":
    print(main())
