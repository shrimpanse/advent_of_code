def get_input_file(file_path):
    with open(file_path, "r") as handle:
        return handle.read().splitlines()

def main():
    input = get_input_file("input.txt")

    array = array = [list(a) for a in input]
    h = len(array)
    w = len(array[0])

    result = 0
    for i in range(h):
        if i == 0 or i == h - 1:
            continue
        for j in range(w):
            if j == 0 or j == w - 1:
                continue
            if array[i][j] == "A":
                diag1 = f"{array[i-1][j-1]}{array[i][j]}{array[i+1][j+1]}"
                if diag1 in ["MAS", "SAM"]:
                    diag2 = f"{array[i-1][j+1]}{array[i][j]}{array[i+1][j-1]}"
                    if diag2 in ["MAS", "SAM"]:
                        # x found
                        result += 1
    print(result)

if __name__ == '__main__':
    main()