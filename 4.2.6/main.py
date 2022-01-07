def foo(encoded_string, decoding_dict):
    fast, slow = 0, 0
    result = ""
    while fast < len(encoded_string):
        if fast == slow:
            if encoded_string[fast] in decoding_dict:
                result += decoding_dict[encoded_string[fast]]
                fast += 1
                slow += 1
            else:
                fast += 1
        else:
            if encoded_string[slow : fast + 1] in decoding_dict:
                result += decoding_dict[encoded_string[slow : fast + 1]]
                fast += 1
                slow = fast
            else:
                fast += 1
    print(result)


def main():
    k, l = map(int, input().split())
    decoding_dict = {}
    for i in range(k):
        letter, code = input().split(sep=": ")
        decoding_dict[code] = letter
    encoded_string = input()
    foo(encoded_string, decoding_dict)


if __name__ == "__main__":
    main()
