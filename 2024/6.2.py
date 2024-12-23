from enum import Enum
import Input_helper

class Direction(Enum):
    UP = (-1,0)
    RIGHT = (0, 1)
    DOWN = (1,0)
    LEFT = (0,-1)

    def next(self):
        directions = [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]
        return directions[(directions.index(self) + 1) % len(directions)]


class Guard:
    def __init__(self, x, y, direction, board_x, board_y, table):
        self.x = x
        self.y = y
        self.direction = direction
        self.board_x = board_x
        self.board_y = board_y
        self.table = table
        self.count = 0


    def move(self):
        x_add, y_add = self.direction.value
        x_new = self.x + x_add
        y_new = self.y + y_add
        if self.in_board(x_new, y_new) and self.table[x_new][y_new] == "#":
            self.direction = self.direction.next()
        else:
            self.x = x_new
            self.y = y_new


    def count_field(self):
        if self.table[self.x][self.y] in {".", "^"}:
            self.table[self.x][self.y] = 1
        else:
            self.table[self.x][self.y] += 1
            if self.table[self.x][self.y] >= 5:
                self.count += 1


    def in_board(self, x, y):
        return 0 <= x < self.board_x and 0 <= y < self.board_y


def parse_data(lines):
    return [[l for l in line.replace('\n', '')] for line in lines]


def find_guard(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '^':
                return i,j
    return None


def simulation(data):
    board = data
    x_len, y_len = len(board), len(board[0])
    x,y = find_guard(board)
    guard = Guard(x, y, Direction.UP, x_len, y_len, board)
    while guard.in_board(guard.x, guard.y):
        guard.count_field()
        guard.move()
        if guard.count >= 1:
            return True
    return False


def find_obstacles(data):
    sum = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '.':
                new_data = [[d for d in data_1] for data_1 in data]
                new_data[i][j] = "#"
                if simulation(new_data):
                    sum += 1
    return sum

def main():
    get_input.get_input(6)
    file = open("input_day_6", "r")
    lines = file.readlines()
    data = parse_data(lines)
    return find_obstacles(data)


if __name__ == "__main__":
    print(main())