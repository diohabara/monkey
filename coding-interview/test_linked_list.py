from typing import Optional


class Node:
    def __init__(self, x: int) -> None:
        self.val = x
        self.next: Optional[Node] = None


class LinkedList:
    def __init__(self) -> None:
        """
        Initialize your data structure here.
        Time: O(1)
        Space: O(1)
        """
        self.head: Optional[Node] = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list.
        If the index is invalid, return -1.
        Time: O(N)
        Space: O(1)
        """
        if index < 0 or self.size <= index:
            return -1
        cur = self.head
        for _ in range(index):
            if not cur:
                raise Exception("Error: accessing None")
            cur = cur.next
        if not cur:
            raise Exception("Error: accessing None")
        return cur.val

    def add_at_head(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        Time: O(N)
        Space: O(1)
        """
        self.add_at_index(0, val)

    def add_at_tail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        Time : O(1)
        Space: O(1)
        """
        self.add_at_index(self.size, val)

    def add_at_index(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list,
            the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        Time: O(N)
        Space: O(1)
        """
        if self.size < index:
            return

        cur = self.head
        new_node = Node(val)

        if index <= 0:
            new_node.next = cur
            self.head = new_node
        else:
            for _ in range(index - 1):
                if not cur:
                    raise Exception("Error: accessing None")
                cur = cur.next
            if not cur:
                raise Exception("Error: accessing None")
            # new, cur -> next
            new_node.next = cur.next  # new -> next
            cur.next = new_node  # cur -> new -> next
        self.size += 1

    def delete_at_index(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        Time: O(N)
        Space: O(1)
        """
        if index < 0 or self.size <= index:
            return

        cur = self.head
        if index == 0:
            if not self.head:
                raise Exception("Error: accessing None")
            self.head = self.head.next
        else:
            for _ in range(index - 1):
                if not cur:
                    raise Exception("Error: accessing None")
                cur = cur.next
            if not cur or not cur.next:
                raise Exception("Error: accessing None")
            cur.next = cur.next.next
        self.size -= 1


def test_linked_list() -> None:
    linked_list = LinkedList()
    linked_list.add_at_head(0)
    expected0 = 0
    actual0 = linked_list.get(0)
    assert actual0 == expected0
    linked_list.add_at_head(2)
    linked_list.add_at_tail(1)
    expected1 = 1
    actual1 = linked_list.get(2)
    assert actual1 == expected1
    linked_list.delete_at_index(2)
    expected2 = 2
    actual2 = linked_list.get(0)
    assert actual2 == expected2
