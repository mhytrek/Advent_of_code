from Input_helper import get_input
import re

def parse(d):
    connections = [ b.replace("\n", "").split("-") for b in d]
    return connections


def neighbour_list(connections):
    n_list = dict()
    for p, l in connections:
        if n_list.get(p) is not None:
            n_list[p].append(l)
        else:
            n_list[p] = [l]

        if n_list.get(l) is not None:
            n_list[l].append(p)
        else:
            n_list[l] = [p]
    return n_list


def find_three(n_list):
    suma = 0
    t_2 = 0
    t_3 = 0
    for k in n_list.keys():
        if "t" in k[:1]:
            neighbours = n_list[k]
            for i in range(len(neighbours)-1):
                for j in range(i+1,len(neighbours)):
                    if n_list.get(neighbours[i]) is not None and neighbours[j] in n_list.get(neighbours[i]):
                        suma += 1
                        if "t" in neighbours[i][:1] and "t" in neighbours[j][:1]:
                            t_3 += 1
                        elif "t" in neighbours[i][:1] or "t" in neighbours[j][:1]:
                            t_2 += 1
    print(suma, t_2, t_3)
    return suma - (t_2 // 2) - ((t_3 // 3)*2)


def main():
    get_input(23)
    file = open("input_day_23", "r")
    lines = file.readlines()
    board = parse(lines)
    n_list = neighbour_list(board)
    return find_three(n_list)




if __name__ == "__main__":
    print(main())


#2298 too high
#2298
#4596
