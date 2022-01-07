from array import array


def fib_mod(n, m):
    period = array("Q", [0, 1])
    flg = False
    i = 2
    if n == 1 or n == 2:
        return 1
    while not flg and i <= n:
        period.append((period[-2] + period[-1]) % m)
        if period[:2] == period[-2:]:
            period = period[:-2]
            flg = True
        i += 1
    if flg:
        return period[n % len(period)]
    else:
        return period[-1]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
