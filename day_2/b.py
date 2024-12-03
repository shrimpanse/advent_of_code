def get_input_file(file_path):
    with open(file_path, "r") as handle:
        return handle.read().splitlines()

def get_variations(report, e):
    return [
        report[:e-2] + report[e-1:],
        report[:e-1] + report[e:],
        report[:e] + report[e+1:],
    ]

def check_report(report, dampener):
    asc = None
    last = None
    save = True
    for e, entry in enumerate(report):
        if last is None:
            last = entry
            continue
        
        div = last - entry
        save &= 1 <= abs(div) <= 3
        if not save:
            if dampener:
                dampener = False
                return any([check_report(variation, dampener) for variation in get_variations(report, e)])
            break

        cur_asc = div <= 0
        if asc is None:
            # set direction
            asc = cur_asc
        else:
            # compare direction
            if cur_asc != asc:
                if dampener:
                    dampener = False
                    return any([check_report(variation, dampener) for variation in get_variations(report, e)])
                save = False
                break 
        
        last = entry
    return save

def main():
    lines = get_input_file("input.txt")
    save_counter = 0
    for line in lines:
        report = [int(l) for l in line.split(" ")]
        save = check_report(report, True)

        if save:
            save_counter += 1

    print(save_counter)
    return 0
            
    
if __name__ == '__main__':
    main()