import re

def get_input_file(file_path):
    with open(file_path, "r") as handle:
        return handle.read().splitlines()

def find_word(array):
    res = 0
    for line in array:
        res += len(re.findall(r"(XMAS)", line))
        res += len(re.findall(r"(SAMX)", line))
    return res

def rotate_array(array):
    # explode
    array = [list(a) for a in array]
    # rotate
    array = list(zip(*array[::-1]))
    # implode
    return ["".join(a) for a in array]

def create_diagonals(array):
    # explode
    array = [list(a) for a in array]

    h = len(array)
    w = len(array[0])

    new_array = []

    for i in range(w - 1, -(h), -1):
        x = max(i, 0)
        y = max(-i, 0)

        row = []
        while x < w and y < h:            
            row.append(array[y][x])
            x += 1
            y += 1
        new_array.append(row)

    return ["".join(a) for a in new_array]


def main():
    input = get_input_file("input.txt")

    # vert
    result = find_word(input)
    
    # hor
    hor = rotate_array(input)
    result += find_word(hor)

    # diag
    diag = create_diagonals(input)
    result += find_word(diag)

    # diag rot
    diag_rot = create_diagonals(hor)
    result += find_word(diag_rot)
    
    print(result)
    return 0


if __name__ == '__main__':
    main()