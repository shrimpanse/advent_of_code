import re

def get_input_file(file_path):
    with open(file_path, "r") as handle:
        return handle.read()

def main():
    start_end_pattern = r"(?:do\(\)|^)(.*?)(?:don't\(\)|$)"
    mul_pattern = r"mul\((\d{1,3},\d{1,3})\)"
    input = get_input_file("input.txt").replace("\n","")
    answer = 0

    start_end_matches = re.findall(start_end_pattern, input)
    for se_match in start_end_matches:
        print(se_match)
        matches = re.findall(mul_pattern, se_match)
        for match in matches:
            x, y = match.split(",")
            answer += int(x) * int(y)
    
    print(answer)
    return 0


if __name__ == '__main__':
    main()