def unique_number(x):
    ctr = 0
    for num in x:
        ctr ^= num
    return ctr


def main():
    print(unique_number([1, 1, 2, 2, -12, 3, 3, 4, 4, 5, 5, 6, 6]))


if __name__ == "__main__":
    main()
