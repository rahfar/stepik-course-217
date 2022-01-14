def main():
    W, n = tuple(map(int, input().split()))
    w = list(map(int, input().split()))

    d = [[0 for _ in range(n + 1)] for _ in range(W + 1)]
    for i in range(W + 1):
        d[i][0] = 0
    for j in range(n + 1):
        d[0][j] = 0

    for j in range(1, n + 1):
        for i in range(1, W + 1):
            d[i][j] = d[i][j - 1]
            if w[j - 1] <= i:
                d[i][j] = max(d[i][j], d[i - w[j - 1]][j - 1] + w[j - 1])

    print(d[W][n])


if __name__ == "__main__":
    main()
