def get_phone(number):
    return number.partition(' ')[2].replace(' ', '-')


def split_third(third):
    splits = third.split("#")
    percents = format(float(splits[0][:-1]) / 100, ".3f")
    date = "-".join(splits[1].split("/")[::-1])
    return date, percents


def main(table):
    n = len(table)
    first = list()
    second = list()
    third = list()
    for i in range(n):
        elem = table[i][0]
        if elem is not None:
            first.append(get_phone(elem))
    for i in range(n):
        elem = table[i][-1]
        if elem is not None:
            res = split_third(elem)
            second.append(res[0])
            third.append(res[1])
    new_table = [first, second, third]
    new_table = [list(i) for i in zip(*new_table)]
    return new_table


main([
    ["+7 591 447-1656", None, "+7 591 447-1656", "50%#02/01/15"],
    ["+7 720 090-0945", None, "+7 720 090-0945", "77%#01/05/07"],
    ["+7 124 844-5664", None, "+7 124 844-5664", "90%#99/09/09"],
    ["+7 739 595-4033", None, "+7 739 595-4033", "16%#01/12/11"],
])
