import math


def foo(n):
    # k = math.floor((-1+math.sqrt(1+8*n)/2))
    k = 1
    flg = True
    ans = []
    while flg:
        if n - k < 0:
            flg = False
            ans[-1] += n
            k -= 1
        else:
            ans.append(k)
            n -= k
            k += 1
    print(k)
    print(*ans, sep=" ")
    return 0


def main():
    n = int(input())
    foo(n)


if __name__ == "__main__":
    main()
