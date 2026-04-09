class MinHeap:
    def __init__(self):
        self.heap = [0]  # dummy at index 0 for easier index math

    def push(self, val: int) -> None:
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def pop(self) -> int:
        if len(self.heap) <= 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()

        root = self.heap[1]
        self.heap[1] = self.heap.pop()
        self._bubble_down(1)
        return root

    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums
        # start from last non-leaf node and bubble down
        for i in range(len(self.heap) // 2, 0, -1):
            self._bubble_down(i)

    def _bubble_up(self, index: int) -> None:
        while index > 1:
            parent = index // 2
            if self.heap[parent] <= self.heap[index]:
                break
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent

    def _bubble_down(self, index: int) -> None:
        n = len(self.heap)
        while True:
            left = 2 * index
            right = left + 1
            smallest = index

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            index = smallest