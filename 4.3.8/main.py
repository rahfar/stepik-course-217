# max-heap
class Priority_queue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return str(self.queue)

    def insert(self, value):
        self.queue.append(value)
        value_index = len(self.queue) - 1
        while True:
            parent_index = (value_index - 1) // 2
            if parent_index >= 0 and self.queue[parent_index] < self.queue[value_index]:
                self.queue[value_index], self.queue[parent_index] = (
                    self.queue[parent_index],
                    self.queue[value_index],
                )
                value_index = parent_index
                continue
            break

    def extract_max(self):
        max_value = self.queue[0]
        shift_node = len(self.queue) - 1
        if shift_node == 0:
            self.queue.pop()
            print(max_value)
        else:
            self.queue[0] = self.queue[shift_node]
            self.queue.pop(shift_node)
            shift_node = 0
            n = len(self.queue)
            while True:
                left_child = 2 * shift_node + 1
                right_child = 2 * shift_node + 2
                # оба ребенка существуют
                if 0 <= left_child < n and 0 <= right_child < n:
                    if (
                        self.queue[shift_node] >= self.queue[left_child]
                        and self.queue[shift_node] >= self.queue[right_child]
                    ):
                        break
                    if self.queue[left_child] < self.queue[right_child]:
                        self.queue[right_child], self.queue[shift_node] = (
                            self.queue[shift_node],
                            self.queue[right_child],
                        )
                        shift_node = right_child
                        continue
                    else:
                        self.queue[left_child], self.queue[shift_node] = (
                            self.queue[shift_node],
                            self.queue[left_child],
                        )
                        shift_node = left_child
                        continue
                # существует только левый
                elif 0 <= left_child < n and right_child >= n:
                    if self.queue[shift_node] >= self.queue[left_child]:
                        break
                    else:
                        self.queue[left_child], self.queue[shift_node] = (
                            self.queue[shift_node],
                            self.queue[left_child],
                        )
                        break
                # нет детей
                else:
                    break
            print(max_value)
        return


def main():
    queue = Priority_queue()
    n = int(input())
    for i in range(n):
        command = input()
        if command.startswith("Insert"):
            value = int(command.split()[1])
            queue.insert(value)
        elif command.startswith("ExtractMax"):
            queue.extract_max()


if __name__ == "__main__":
    main()
