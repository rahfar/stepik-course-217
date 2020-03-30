from queue import Queue


def merge(a, b, inversions_cnt):
    i, j = 0, 0
    result = []
    while len(result) < len(a) + len(b):
        if i < len(a) and j < len(b) and a[i] <= b[j]:
            result.append(a[i])
            i += 1
        elif i < len(a) and j < len(b) and a[i] > b[j]:
            result.append(b[j])
            j += 1
            inversions_cnt += len(a[i:])
        elif i >= len(a):
            result += b[j:]
        elif j >= len(b):
            result += a[i:]
    return result, inversions_cnt


def merge_sort(a):
    q = Queue()
    inversions_cnt = 0
    for i in a:
        q.put([i])
    while q.qsize() > 1:
        tmp, inversions_cnt = merge(q.get(), q.get(), inversions_cnt)
        q.put(tmp)
    return inversions_cnt


def main():
    input()
    a = list(map(int, input().split()))
    result = merge_sort(a)
    print(result)


if __name__ == "__main__":
    main()
