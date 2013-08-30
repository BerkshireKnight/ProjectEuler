
def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b

    return a


def int_to_list(n):
    return [int(x) for x in str(n)]


def main():
    n = 1
    while len(int_to_list(fibonacci(n))) < 1000:
        n += 1

    print(n)


if __name__ == "__main__":
    main()
