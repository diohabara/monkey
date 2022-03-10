class Heap:  # max heap
    def __init__(self):
        self.heap: list[int] = []

    def push(self, x: int) -> None:
        self.heap.append(x)
        current_i = len(self.heap) - 1
        # replace current value(smaller) with parent value(bigger)
        while 0 < current_i:
            parent_i = (current_i - 1) // 2  # index of current's parent
            if x <= self.heap[parent_i]:
                break
            self.heap[current_i] = self.heap[parent_i]
            current_i = parent_i
        # replace current value with x
        self.heap[current_i] = x

    def top(self) -> int:
        if self.heap:
            return self.heap[0]
        return -1

    def pop(self) -> None:
        if not self.heap:
            return
        x = self.heap.pop()  # bottom right value
        i = 0
        while i * 2 + 1 < len(self.heap):
            # bigger one is child1
            child1 = 2 * i + 1
            child2 = 2 * i + 2
            if child2 < len(self.heap) and self.heap[child1] < self.heap[child2]:
                child1 = child2
            if self.heap[child1] <= x:
                break
            self.heap[i] = self.heap[child1]
            i = child1
        self.heap[i] = x


def test_heap() -> None:
    h = Heap()
    h.push(5)
    h.push(3)
    h.push(7)
    h.push(1)
    assert h.top() == 7
    h.pop()
    assert h.top() == 5
    h.push(11)
    assert h.top() == 11
