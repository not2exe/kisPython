def main(b, n, a, m, y):
    res = 1
    for k in range(1, n + 1):
        res *= sum(pow(j * j - 17 * k - pow(k, 3), 3)
                   + k for j in range(1, b + 1))
    return res + sum(sum(sum(pow(46 * y * y - 59 * k - 1, 5)
                             + 51 * pow(c * c - j * j * j - k, 6)
                             for j in range(1, a + 1))
                         for c in range(1, m + 1))
                     for k in range(1, b + 1))


print(main(3, 8, 3, 6, 0.41))
print(main(2, 2, 3, 2, -0.04))
print(main(4, 4, 3, 2, -0.25))
print(main(4, 2, 7, 2, -0.69))
print(main(6, 6, 8, 5, -0.08))
