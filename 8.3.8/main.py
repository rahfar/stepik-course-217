def main():
    a, b = input(), input()
    n, m = len(a), len(b)
    d = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        d[i][0] = i
    for j in range(m + 1):
        d[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            c = 1 if a[i - 1] != b[j - 1] else 0
            d[i][j] = min(
                d[i - 1][j] + 1,
                d[i][j - 1] + 1,
                d[i - 1][j - 1] + c,
            )
    print(d[n][m])


if __name__ == "__main__":
    main()
