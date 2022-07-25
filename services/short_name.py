

def short_name(name) -> str:
    name_split = name.split(" ")
    if len(name_split) > 1:
        return name_split[0][0] + name_split[-1][0]
    else:
        return name_split[0][0] + name_split[0][1]


def increment_in_file(file_name):
    with open(file_name, "r") as f:
        number = int(f.read())
    with open(file_name, "w") as f:
        f.write(str(number + 1))
    return number + 1


def get_counter_from_file(file_name):
    with open(file_name, "r") as f:
        number = int(f.read())
    return number