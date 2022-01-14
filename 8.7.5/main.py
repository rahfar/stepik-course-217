def main():
    n = int(input())

    h = {1: 0}
    i = 1

    while i < n:
        if i + 1 <= n:
            if h.get(i + 1) is None:
                h[i + 1] = h[i] + 1
            else:
                h[i + 1] = min(h[i + 1], h[i] + 1)

        if 2 * i <= n:
            if h.get(2 * i) is None:
                h[2 * i] = h[i] + 1
            else:
                h[2 * i] = min(h[2 * i], h[i] + 1)

        if 3 * i <= n:
            if h.get(3 * i) is None:
                h[3 * i] = h[i] + 1
            else:
                h[3 * i] = min(h[3 * i], h[i] + 1)
        i += 1

    print(h[n])

    i = n
    res = [i]

    while i > 1:
        h_n_1 = h[i - 1]
        h_n_2 = h[i // 2] if i % 2 == 0 else float("inf")
        h_n_3 = h[i // 3] if i % 3 == 0 else float("inf")
        _min = min(h_n_1, h_n_2, h_n_3)
        if _min == h_n_1:
            i = i - 1
        elif _min == h_n_2:
            i = i // 2
        elif _min == h_n_3:
            i = i // 3
        else:
            raise Exception()
        res.insert(0, i)

    print(*res)


if __name__ == "__main__":
    main()
