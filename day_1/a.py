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
    list1 = sorted(list1)
    list2 = sorted(list2)

    answer = 0
    for i in range(len(list1)):
        answer += abs(int(list1[i]) - int(list2[i]))

    print(answer)

    return 0

if __name__ == '__main__':
    main()