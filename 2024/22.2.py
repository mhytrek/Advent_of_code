from Input_helper import get_input

def parse(d):
    board = [ int(b.replace("\n", "")) for b in d]
    return board


def find_num(board):
    sum = []
    for num in board:
        list = []
        list.append(num % 10)
        for i in range(2000):
            new_num = ((num * 64) ^ num) % 16777216
            new_num = ((new_num // 32) ^ new_num) % 16777216
            new_num = ((new_num * 2048) ^ new_num) % 16777216
            num = new_num
            list.append(num % 10)
        r = []
        for l in range(1, len(list)):
            r.append(list[l] - list[l-1])
        sum.append((r, list))
    return sum


def find_sum(list):
    dict_all = {}
    for l, val in list:
        dict = {}
        for i in range(3,len(l)):
            key = (l[i-3], l[i-2], l[i-1], l[i])
            getd = dict.get(key)
            if getd is None:
                if key == (-2,1,-1,3):
                    print(val[i+1])
                dict[key] = 1
                if dict_all.get(key) is None:
                    dict_all[key] = val[i+1]
                else:
                    dict_all[key] += val[i + 1]
    return max(dict_all.values())


def main():
    get_input(22)
    file = open("input_day_22", "r")
    lines = file.readlines()
    board = parse(lines)
    l = find_num(board)
    return find_sum(l)



if __name__ == "__main__":
    print(main())
