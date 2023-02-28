import math


def main(z):
    if z < 47:
        res = 17 * pow(math.log10(z), 6) + z + pow(z, 7) / 54
    elif 47 <= z < 91:
        res = 60 * pow(z * z - 1 - z, 4)
    else:
        res = pow(z, 6)
    return res


print(main(45))
print(main(34))
print(main(106))
print(main(142))
print(main(115))