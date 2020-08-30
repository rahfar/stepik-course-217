def count_1(array: list, x: int) -> int:
    l = 0
    r = len(array) - 1
    if r < 0:
        return 0
    while l < r:
        m = (l + r) // 2
        if array[m] <= x:
            l = m + 1
        else:
            r = m
    if array[l] <= x:
        return l + 1
    else:
        return l


def count_2(array: list, x: int) -> int:
    l = 0
    r = len(array) - 1
    if r < 0:
        return 0
    while l < r:
        m = (l + r) // 2
        if array[m] < x:
            l = m + 1
        else:
            r = m
    if array[l] < x:
        return l + 1
    else:
        return l


def main():
    n, m = map(int, input().split())
    sections = [list(map(int, input().split())) for i in range(n)]
    points = list(map(int, input().split()))
    sorted_section_beginings = sorted(list(map(lambda x: x[0], sections)))
    sorted_section_endings = sorted(list(map(lambda x: x[1], sections)))
    answer = []
    for point in points:
        answer.append(
            count_1(sorted_section_beginings, point) -
            count_2(sorted_section_endings, point)
        )
    print(*answer)


if __name__ == "__main__":
    main()
