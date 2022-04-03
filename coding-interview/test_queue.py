class Queue:
    def __init__(self, k: int = 100):
        self.items = [0] * k
        self.head = 0  # points to front
        self.count = 0  # how many items are in
        self.capacity = k

    def enqueue(self, item: int) -> None:
        if self.count == self.capacity:
            raise Exception("queue is full!")
        self.items[(self.head + self.count) % self.capacity] = item
        self.count += 1

    def dequeue(self) -> None:
        if self.count == 0:
            raise Exception("queue if empty!")
        self.head = (self.head + 1) % self.capacity
        self.count -= 1

    def front(self) -> int:
        if self.count == 0:
            raise Exception("queue is empty!")
        return self.items[self.head]

    def is_empty(self) -> bool:
        return self.count == 0


def test_queue() -> None:
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    expected1 = 1
    actual1 = q.front()
    assert actual1 == expected1
    q.dequeue()
    expected2 = 2
    actual2 = q.front()
    assert actual2 == expected2
    q.dequeue()
    assert q.is_empty()
