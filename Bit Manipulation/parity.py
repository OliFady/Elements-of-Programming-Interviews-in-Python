def parity(x):
    ctr = 0
    while x:
        ctr ^= x & 1
        x >>= 1
    return ctr


def optimized_parity(x):
    ctr = 0
    while x:
        ctr ^= x & 1
        x &= x - 1  # removes least significant set bit
    return ctr


def main():
    print(parity(11))
    print(optimized_parity(11))


if __name__ == "__main__":
    main()
