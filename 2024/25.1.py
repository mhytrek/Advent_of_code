from Input_helper import get_input
import re
import queue
import numpy

def parse(d):
    data = "".join(d)
    schemes = data.split("\n\n")
    keys = []
    shc = []
    for schema in schemes:
        t = schema.split("\n")
        val = [ sum([int(t[i][j] == "#") for i in range(7)]) - 1 for j in range(5)]
        if t[0][0] == ".":
            keys.append(val)
        else:
            shc.append(val)
    return keys, shc


def check_key(key, sch):
    for i in range(5):
        if sch[i] + key[i] > 5:
            return False
    return True


def check(k,s):
    sum = 0
    for sch in s:
        for key in k:
            sum += check_key(key, sch)
    return sum


def main():
    get_input(25)
    file = open("input_day_25", "r")
    lines = file.readlines()
    k, s = parse(lines)
    return check(k, s)




if __name__ == "__main__":
    print(main())
