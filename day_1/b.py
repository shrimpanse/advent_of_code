import re

def get_input_file(file_path):
    l1 = []
    l2 = []
    with open(file_path, "r") as data:
        for d in data:
            pair = re.split(r'\s+', d.strip())
            l1.append(pair[0])
            l2.append(pair[1])
    return l1, l2

def main():
    list1, list2 = get_input_file("input.txt")

    answer = 0
    for l in list1:
        appearance = list2.count(l)
        answer += int(l) * appearance

    print(answer)
    return 0

if __name__ == '__main__':
    main()