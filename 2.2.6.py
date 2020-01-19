from array import array

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        F = array('i', [0, 1])
        for i in range(2, n + 1):
            F.append(F[i-1] + F[i-2])
        return F[-1]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()