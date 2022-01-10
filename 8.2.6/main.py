def main():
    n, a = int(input()), list(map(int, input().split()))

    m = [0] * (
        n + 1
    )  # m[j] = index of the highest element of a in witch ends current LIS
    p = [0] * n
    l = 0  # length of current LIS

    # costruct m, p lists
    for i in range(len(a)):
        left = 1
        right = l + 1
        while left < right:
            mid = (left + right) // 2
            if a[m[mid]] >= a[i]:
                left = mid + 1
            else:
                right = mid

        new_l = left

        p[i] = m[new_l - 1]
        m[new_l] = i

        if new_l > l:
            l = new_l

    # construct solution from m, p, a
    s = [0] * l
    k = m[l]
    for i in range(len(s) - 1, -1, -1):
        s[i] = k + 1
        k = p[k]

    print(l)
    print(*s)


if __name__ == "__main__":
    main()
