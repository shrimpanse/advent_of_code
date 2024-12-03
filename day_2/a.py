

def get_input_file(file_path):
    with open(file_path, "r") as handle:
        return handle.read().splitlines()

def main():
    lines = get_input_file("input.txt")
    save_counter = 0
    for line in lines:
        report = [int(l) for l in line.split(" ")]
        asc = None
        last = None
        save = True
        for entry in report:
            if last is None:
                last = entry
                continue
            
            div = last - entry
            save &= 1 <= abs(div) <= 3
            if not save:
                print(line, "\nERROR", f"Difference was {div}", f"{last} -> {entry}")
                break

            cur_asc = div <= 0
            if asc is None:
                # set direction
                asc = cur_asc
            else:
                # compare direction
                if cur_asc != asc:
                    save = False
                    print(line, "\nERROR", f"Direction changed: {asc} -> {cur_asc}")
                    break 
            
            last = entry

        if save:
            save_counter += 1

    print(save_counter)
    return 0
            
    

if __name__ == '__main__':
    main()