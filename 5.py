def main(y, z):
    n = len(y)
    return 8 * sum(
        pow(1 - pow(z[n - i], 3) - 20 * y[n - i] * y[n - i], 7)
        for i in range(1, n + 1))


print(main([0.09, -0.19],
           [0.77, -0.97]))
