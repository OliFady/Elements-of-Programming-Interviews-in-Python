def count_bits(x):
    ctr = 0
    while x:
        ctr += x & 1
        x >>= 1
    return ctr


def main():
    print(count_bits(12))

if __name__ == "__main__":
    main()
