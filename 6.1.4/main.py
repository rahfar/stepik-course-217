def find(a, n, value):
    l, r = 0, n - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == value:
            return m + 1
        elif a[m] > value:
            r = m - 1
        else:
            l = m + 1
    return -1


def main():
    n, *a = map(int, input().split())
    k, *b = map(int, input().split())
    result = " ".join(str(find(a, n, value)) for value in b)
    print(result)


if __name__ == "__main__":
    main()
