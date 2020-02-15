# import objgraph

# def filter_func(arg):
#     return type(arg) != type(type(1)) and type(arg) != type(None)

class Node():
    def __init__(self, letter=None, left_child=None, right_child=None, freq=None, code=''):
        self.letter = letter
        self.left_child = left_child
        self.right_child = right_child
        self.freq = freq
        self.code = code
    def __lt__(self, other):
        if self.freq < other.freq:
            return True
        else:
            return False
    def __gt__(self, other):
        if self.freq > other.freq:
            return True
        else:
            return False
    def __str__(self):
        return 'freq={} lc_freq_id={} rc_freq_id={}'.format(self.freq, id(self.left_child), id(self.right_child))

def gen_code(root, encoding_dict):
    if root.left_child == None and root.right_child == None:
        encoding_dict[root.letter] = root.code
        return None
    if root.left_child != None:
        root.left_child.code = root.code + '0'
        gen_code(root.left_child, encoding_dict)
    if root.right_child != None:
        root.right_child.code = root.code + '1'
        gen_code(root.right_child, encoding_dict)


def foo(s):
    freq = dict()
    priority_queue = []

    for x in s:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    
    for x in set(s):
        priority_queue.append(Node(letter=x, freq=freq[x]))

    if len(priority_queue) - 1 > 0:
        for i in range(len(priority_queue) - 1):
            minimum_index = priority_queue.index(min(priority_queue))
            node_i = priority_queue.pop(minimum_index)
            minimum_index = priority_queue.index(min(priority_queue))
            node_j = priority_queue.pop(minimum_index)
            priority_queue.append(Node(left_child=node_i, right_child=node_j, freq=(node_i.freq + node_j.freq)))
        encoding_dict = {}
        root = priority_queue[0]
        gen_code(root, encoding_dict)
        
    else:
        root = priority_queue[0]
        encoding_dict = {
            root.letter: '0'
        }
    encoded_string = s
    for letter, code in encoding_dict.items():
        encoded_string = encoded_string.replace(letter, code)
    print(len(freq.keys()), len(encoded_string))
    for letter, code in encoding_dict.items():
        print('{}: {}'.format(letter, code))
    print(encoded_string)
    # objgraph.show_refs(root, max_depth=10, filter=filter_func, filename='objgraph.png')
    return 0

def main():
    s = str(input())
    foo(s)

if __name__ == "__main__":
    main()