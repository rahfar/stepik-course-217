def main():
    n = int(input())
    A = list(map(int, input().split()))
    D = list()
    for i in range(0, n):
        D.append(1)
        for j in range(0, i):
            if A[i] % A[j] == 0 and D[j] + 1 > D[i]:
                D[i] = D[j] + 1
    if D:
        print(max(D))
    else:
        print(0)


if __name__ == "__main__":
    main()
