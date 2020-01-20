def foo(n, segments):
    points_count = 0
    points = []
    i = 0
    while i < len(segments):
        points.append(segments[i][1])
        points_count += 1
        while i < len(segments) and points[-1] >= segments[i][0]:
            i += 1
    print(points_count)
    print(*points, sep=' ')
    return 0

def main():
    n = int(input())
    segments = []
    for i in range(n):
        segments.append(list(map(int, input().split())))
    sorted_segments = sorted(segments, key= lambda item: item[-1])
    foo(n, sorted_segments)

if __name__ == "__main__":
    main()