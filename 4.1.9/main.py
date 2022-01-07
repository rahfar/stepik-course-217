def foo(n, W, items):
    max_amaount = 0
    W_current = W
    i = 0
    while W_current > 0 and len(items) > 0:
        if items[0][1] > W_current:
            max_amaount += (items[0][0] / items[0][1]) * W_current
            W_current -= W_current
        else:
            max_amaount += items[0][0]
            W_current -= items[0][1]
        items.pop(0)
    print("{0:.3f}".format(max_amaount))
    return 0


def main():
    n, W = map(int, input().split())
    items = []
    for i in range(n):
        items.append(list(map(int, input().split())))
    sorted_items = sorted(items, key=lambda item: -1 * item[0] / item[1])
    foo(n, W, sorted_items)


if __name__ == "__main__":
    main()
