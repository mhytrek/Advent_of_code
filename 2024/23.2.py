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
    for key in n_list.keys():
        n_list[key].append(key)
    return n_list


def find_three(n_list):
    biggest = 0
    list_b = []
    for a in n_list.keys():
        neigh_a = n_list[a]
        mask = [i for i in range(2**len(neigh_a)-1)]
        for m in mask:
            l = [a]
            clique = set(neigh_a)
            for i in range(len(neigh_a)-1):
                if m % 2 == 1:
                    if neigh_a[i] in clique:
                        clique = clique.intersection(set(n_list[neigh_a[i]]))
                        l.append(neigh_a[i])
                    else:
                        continue
                m //= 2
            if len(l) > biggest:
                biggest = len(l)
                list_b = l

    str = ""
    for a in sorted(list_b):
        str += a + ","
    return str[:-1]







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
