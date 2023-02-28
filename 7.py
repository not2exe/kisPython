def main(a):
    b = int(a)
    c = (b << 2) & 0b111111111000000000
    d = (b << 1) & 0b000000000011111110
    c = (c | d |
         ((b & 0b100000000000000000) >> 9) |
         (b & 0b010000000000000000) >> 16)
    return hex(c)


print(main('170475'))
print(main('26231'))
print(main('235421'))
print(main('98307'))
