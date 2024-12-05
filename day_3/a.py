import re

def get_input_file(file_path):
    with open(file_path, "r") as handle:
        return handle.read()

def main():
    pattern = r"mul\((\d{1,3},\d{1,3})\)"
    input = get_input_file("input.txt")
    answer = 0

    matches = re.findall(pattern, input)
    for match in matches:
        x, y = match.split(",")
        answer += int(x) * int(y)
    
    print(answer)
    return 0


if __name__ == '__main__':
    main()