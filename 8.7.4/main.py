def main():
    n = int(input())
    a = list(map(int, input().split()))
    S = [0] * (n + 1)
    S[0] = 0
    S[1] = a[0]
    if n == 2:
        S[2] = max(a[0] + a[1], a[1])
    elif n > 2:
        S[2] = max(a[0] + a[1], a[1])
        S[3] = a[2] + max(S[2], S[1])
        i = 4
        while i <= n:
            S[i] = a[i - 1] + max(S[i - 1], S[i - 2])
            i += 1
    print(S[n])


if __name__ == "__main__":
    main()
