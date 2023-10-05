def parity(x):
    ctr = 0
    while x:
        ctr += x & 1
        x >>= 1
    return ctr % 2 == 1


def main():
    print(parity(15))


if __name__ == "__main__":
    main()
