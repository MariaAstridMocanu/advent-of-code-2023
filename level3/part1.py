
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
    return 1 <= index < max_index-1


def bounded_both(index_i, index_j, max_index_i, max_index_j):

    return 0 <= index_i < max_index_i-1 and 0 <= index_j < max_index_j


def has_symbol_around(schematic, i, j):
    i_bound = len(schematic) - 1
    j_bound = len(schematic[0])-1

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

    return (j < j_bound and schematic[i][j+1] != '.' and not schematic[i][j+1].isdigit()) or\
        (j > 0 and schematic[i][j - 1] != '.' and not schematic[i][j - 1].isdigit()) or \
        (i < i_bound and j < j_bound and schematic[i + 1][j + 1] != '.' and not schematic[i + 1][j + 1].isdigit()) or \
        (i < i_bound and j > 0 and schematic[i + 1][j - 1] != '.' and not schematic[i+1][j - 1].isdigit()) or \
        (i > 0 and j < j_bound and schematic[i - 1][j + 1] != '.' and not schematic[i - 1][j + 1].isdigit()) or \
        (i > 0 and j > 0 and schematic[i - 1][j - 1] != '.' and not schematic[i - 1][j - 1].isdigit()) or \
        (i < i_bound and schematic[i + 1][j] != '.' and not schematic[i + 1][j].isdigit()) or \
        (i > 0 and schematic[i - 1][j] != '.' and not schematic[i - 1][j].isdigit())


if __name__ == '__main__':
    with open('engine_schematic.txt', 'r') as engine_schematic_file:
        schematic_matrix = convert_text_to_schematic(engine_schematic_file.readlines())
        part_sum = 0
        for i, row in enumerate(schematic_matrix):
            part_number = ''
            for j, character in enumerate(row):
                if character.isdigit() and has_symbol_around(schematic_matrix, i, j):
                    temp_index = j
                    while temp_index >= 0 and row[temp_index].isdigit():
                        part_number = row[temp_index] + part_number
                        row[temp_index] = '.'
                        temp_index -= 1
                        #print(part_number)

                    if temp_index < len(row)-1:
                        temp_index = j+1
                        while temp_index < len(row) and row[temp_index].isdigit():
                            part_number = part_number + row[temp_index]
                            row[temp_index] = '.'
                            temp_index += 1
                            #print(part_number)

                    print(row)
                    print(f'ROW [{i}, {j}] : {part_number}')

                    part_sum += int(part_number)
                    part_number = ''
        print(f'SUM : {part_sum}')
