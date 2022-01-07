inversions_cnt = 0


def merge(a, b):
    global inversions_cnt
    i, j, k = 0, 0, 0
    len_a = len(a)
    len_b = len(b)
    len_result = 0
    result = [0] * (len_a + len_b)
    while len_result < len_a + len_b:
        if i < len_a and j < len_b and a[i] <= b[j]:
            result[k] = a[i]
            k += 1
            len_result += 1
            i += 1
        elif i < len_a and j < len_b and a[i] > b[j]:
            result[k] = b[j]
            k += 1
            len_result += 1
            j += 1
            inversions_cnt += len_a - i
        elif i >= len_a:
            result[k:] = b[j:]
            len_result += len_b - j
        elif j >= len_b:
            result[k:] = a[i:]
            len_result += len_a - i
    return result


def merge_sort(a, l, r):
    if l < r:
        m = (l + r) // 2
        a[l : r + 1] = merge(merge_sort(a, l, m), merge_sort(a, m + 1, r))
    return a[l : r + 1]


def main():
    global inversions_cnt
    input()
    a = list(map(int, input().split()))
    merge_sort(a, 0, len(a) - 1)
    print(inversions_cnt)


if __name__ == "__main__":
    main()
