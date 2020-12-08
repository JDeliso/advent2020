def advent2020_1():
    input = open("./input1.txt", "r")

    input_list = []

    for line in input:
        stripped_line = line.strip()
        input_list.append(int(stripped_line))

    input.close()

    for i in input_list:
        for j in input_list:
            if i + j == 2020:
                print(i)
                print(j)
                return print(i*j)

advent2020_1()