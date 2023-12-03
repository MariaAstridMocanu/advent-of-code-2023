def convert_text_to_schematic(text):
    schematic = []
    schematic_line = []
    for line in text:
        for letter in line.rstrip():
            schematic_line.append(letter)
        schematic.append(schematic_line)
        schematic_line = []
    return schematic


def bounded(index, max_index):
    return 1 <= index < max_index - 1


def bounded_both(index_i, index_j, max_index_i, max_index_j):
    return 0 <= index_i < max_index_i - 1 and 0 <= index_j < max_index_j


def has_digit_around(schematic, i, j):
    # print((bounded(j, j_bound) and schematic[i][j + 1] != '.' and not schematic[i][j + 1].isdigit()))
    # print((bounded(j, j_bound) and schematic[i][j - 1] != '.' and not schematic[i][j - 1].isdigit()))
    # print((bounded_both(i, j, i_bound, j_bound) and schematic[i + 1][j + 1] != '.' and not schematic[i + 1][j + 1].isdigit()))
    # print((bounded_both(i, j, i_bound, j_bound) and schematic[i + 1][j - 1] != '.' and not schematic[i + 1][j - 1].isdigit()))
    # print((bounded_both(i, j, i_bound, j_bound) and schematic[i - 1][j + 1] != '.' and not schematic[i - 1][j + 1].isdigit()))
    # print((bounded_both(i, j, i_bound, j_bound) and schematic[i - 1][j - 1] != '.' and not schematic[i - 1][j - 1].isdigit()))
    # print((bounded(i, i_bound) and schematic[i + 1][j] != '.' and not schematic[i + 1][j].isdigit()))
    # print((bounded(i, i_bound) and schematic[i - 1][j] != '.' and not schematic[i - 1][j].isdigit()))

    # print((bounded(j, j_bound) and schematic[i][j+1] != '.' and not schematic[i][j+1].isdigit()) or\
    #     (bounded(j, j_bound) and schematic[i][j - 1] != '.' and not schematic[i][j - 1].isdigit()) or \
    #     (bounded_both(i, j, i_bound, j_bound) and schematic[i+1][j + 1] != '.' and not schematic[i+1][j + 1].isdigit()) or \
    #     (bounded_both(i, j, i_bound, j_bound) and schematic[i+1][j - 1] != '.' and not schematic[i+1][j - 1].isdigit()) or \
    #     (bounded_both(i, j, i_bound, j_bound) and schematic[i - 1][j + 1] != '.' and not schematic[i - 1][j + 1].isdigit()) or \
    #     (bounded_both(i, j, i_bound, j_bound) and schematic[i - 1][j - 1] != '.' and not schematic[i - 1][j - 1].isdigit()) or \
    #     (bounded(i, i_bound) and schematic[i + 1][j] != '.' and not schematic[i + 1][j].isdigit()) or \
    #     (bounded(i, i_bound) and schematic[i - 1][j] != '.' and not schematic[i - 1][j].isdigit()))

    i_bound = len(schematic) - 1
    j_bound = len(schematic[0]) - 1
    return (j < j_bound and schematic[i][j + 1].isdigit()) or \
        (j > 0 and schematic[i][j - 1].isdigit()) or \
        (i < i_bound and schematic[i + 1][j + 1].isdigit()) or \
        (i < i_bound and schematic[i + 1][j - 1].isdigit()) or \
        (i > 0 and j < j_bound and schematic[i - 1][j + 1].isdigit()) or \
        (i > 0 and j > 0 and schematic[i - 1][j - 1].isdigit()) or \
        (i < i_bound and schematic[i + 1][j].isdigit()) or \
        (i > 0 and schematic[i - 1][j].isdigit())


def create_number(j, row):
    temp_index = j
    part_number_temp = ''
    while temp_index >= 0 and row[temp_index].isdigit():
        part_number_temp = row[temp_index] + part_number_temp
        row[temp_index] = '.'
        temp_index -= 1

    if temp_index < len(row) - 1:
        temp_index = j + 1
        while temp_index < len(row) and row[temp_index].isdigit():
            part_number_temp = part_number_temp + row[temp_index]
            row[temp_index] = '.'
            temp_index += 1
    return part_number_temp


def return_numbers_around(schematic, i, j):
    i_bound = len(schematic) - 1
    j_bound = len(schematic[0]) - 1
    part_number_list = []
    if j < j_bound and schematic[i][j + 1].isdigit():
        row = schematic[i]
        part_number_list.append(create_number(j+1, row))
    if j > 0 and schematic[i][j - 1].isdigit():
        row = schematic[i]
        part_number_list.append(create_number(j-1, row))
    if i < i_bound and schematic[i + 1][j + 1].isdigit():
        row = schematic[i + 1]
        part_number_list.append(create_number(j+1, row))
    if i < i_bound and schematic[i + 1][j - 1].isdigit():
        row = schematic[i + 1]
        part_number_list.append(create_number(j-1, row))
    if i > 0 and j < j_bound and schematic[i - 1][j + 1].isdigit():
        row = schematic[i - 1]
        part_number_list.append(create_number(j+1, row))
    if i > 0 and j > 0 and schematic[i - 1][j - 1].isdigit():
        row = schematic[i - 1]
        part_number_list.append(create_number(j-1, row))
    if i < i_bound and schematic[i + 1][j].isdigit():
        row = schematic[i + 1]
        part_number_list.append(create_number(j, row))
    if i > 0 and schematic[i - 1][j].isdigit():
        row = schematic[i - 1]
        part_number_list.append(create_number(j, row))
    part_number_temp = ''
    return part_number_list


if __name__ == '__main__':
    with open('engine_schematic.txt', 'r') as engine_schematic_file:
        schematic_matrix = convert_text_to_schematic(engine_schematic_file.readlines())
        gear_sum = 0
        for i, row in enumerate(schematic_matrix):
            part_number = ''
            for j, character in enumerate(row):
                if character == "*":
                    if has_digit_around(schematic_matrix, i, j):
                        print(i, " ", j)
                        print(return_numbers_around([rows[:] for rows in schematic_matrix], i, j))
                        gear_numbers = return_numbers_around([rows[:] for rows in schematic_matrix], i, j)
                        if len(gear_numbers) == 2:
                            gear_sum += (int(gear_numbers[0]) * int(gear_numbers[1]))
                        else:
                            print("NOT A GEAR:", gear_numbers)
        for line in schematic_matrix:
            print(line)
        print("GEAR SUM", gear_sum)