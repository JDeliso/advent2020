input = open("./input.txt", "r")

input_list = []

for line in input:
    stripped_line = line.strip()
    input_list.append(stripped_line)

input.close()

print(input_list)