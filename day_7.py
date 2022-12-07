def process(data):
    current_path = ""
    sizes_dict_keys = []
    sizes_dict_vals = []
    directories = []
    for line in data:
        if line[0] == "$":
            # print(line)
            # print(current_path)
            if line.split(" ")[1] == "cd":
                operand = line.split(" ")[2]
                if operand[0] == "/":
                    current_path += operand
                elif ".." in operand:
                    path = current_path.split("/")
                    path.pop(-1)
                    current_path = "/".join(path)
                else:
                    current_path = current_path.rstrip("/")
                    current_path += "/" + operand
                if current_path not in directories:
                    directories.append(current_path)
        else:
            if line.split(" ")[0] != "dir":
                sizes_dict_keys.append("/" + current_path + "/" + line.split(" ")[1])
                sizes_dict_vals.append(int(line.split(" ")[0]))
    return sizes_dict_keys,sizes_dict_vals,directories


def solve_p1(data):
    sizes_dict_keys, sizes_dict_vals, directories = process(data)
    cooldict = dict(zip(sizes_dict_keys, sizes_dict_vals))
    bigtotal = 0
    for directory in directories:
        temp = list(filter(lambda a: directory in a, sizes_dict_keys))
        tot = 0
        for each in temp:
            tot += cooldict[each]
        if tot <= 100000:
            bigtotal += tot
    return bigtotal


def solve_p2(data):
    sizes_dict_keys, sizes_dict_vals, directories = process(data)
    cooldict = dict(zip(sizes_dict_keys, sizes_dict_vals))
    disk_space = 70000000 - sum(sizes_dict_vals)
    bigtotal = 999999999999999999
    for directory in directories:
        temp = list(filter(lambda a: directory in a, sizes_dict_keys))
        tot = 0
        for each in temp:
            tot += cooldict[each]
        if disk_space + tot >= 30000000:
            if bigtotal > tot:
                bigtotal = tot
    return bigtotal
