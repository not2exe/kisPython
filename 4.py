def main(n):
    if n == 0:
        return -0.31
    else:
        return 9 + 37 * main(n - 1) + 82 * (main(n - 1) - 1)


print(main(1))
print(main(5))
print(main(7))
print(main(3))
print(main(8))
