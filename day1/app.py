input = open("./input.txt", "r")

input_list = []

for line in input:
    stripped_line = line.strip()
    input_list.append(int(stripped_line))

input.close()

def advent2020_1():

    for i in input_list:
        for j in input_list:
            if i + j == 2020:
                print(i)
                print(j)
                return print(i*j)

advent2020_1()

def advent2020_2():

    for i in input_list:
        for j in input_list:
            for k in input_list:
                if i + j + k == 2020:
                    print(i)
                    print(j)
                    print(k)
                    return print(i*j*k)

advent2020_2()


