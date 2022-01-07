def main():
    n, a = int(input()), list(map(int, input().split()))
    d, prev = [1] * n, [-1] * n
    for i in range(0, n):
        for j in range(0, i):
            if a[i] <= a[j] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
                prev[i] = j

    max_d_value = 1
    max_d_index = 0
    for ind, cur in enumerate(d):
        if max_d_value < cur:
            max_d_value = cur
            max_d_index = ind

    cur_index = max_d_index
    index_list = list()
    while cur_index != -1:
        index_list.insert(0, cur_index + 1)
        cur_index = prev[cur_index]
    print(max_d_value)
    print(*index_list)


if __name__ == "__main__":
    main()
