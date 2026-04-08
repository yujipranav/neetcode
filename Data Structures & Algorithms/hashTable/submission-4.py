class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * self.capacity

    def hash_function(self, key: int) -> int:
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash_function(key)
        head = self.table[index]

        if head is None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            # update if key exists, else append
            cur = head
            while cur:
                if cur.key == key:
                    cur.value = value
                    return
                if cur.next is None:
                    break
                cur = cur.next
            cur.next = Node(key, value)
            self.size += 1

        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hash_function(key)
        node = self.table[index]

        while node:
            if node.key == key:
                return node.value
            node = node.next

        return -1

    def remove(self, key: int) -> bool:
        index = self.hash_function(key)
        node = self.table[index]
        prev = None

        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.table[index] = node.next
                self.size -= 1
                return True
            prev, node = node, node.next

        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity

        for head in self.table:
            node = head
            while node:
                index = node.key % new_capacity
                if new_table[index] is None:
                    new_table[index] = Node(node.key, node.value)
                else:
                    cur = new_table[index]
                    while cur.next:
                        cur = cur.next
                    cur.next = Node(node.key, node.value)
                node = node.next  # advance unconditionally

        self.capacity = new_capacity
        self.table = new_table