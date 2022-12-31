class MinHeap(object):
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def extract_min(self):
        if not self.array:
            return None
        if len(self.array) == 1:
            return self.array.pop(0)

        minimum = self.array[0]
        self.array[0] = self.array.pop(-1)
        self._bubble_down(index=0)
        return minimum

    def peek_min(self):
        return self.array[0] if self.array else None

    def insert(self, key):
        if key is None:
            raise TypeError('key cannot be none')
        self.array.append(key)
        self._bubble_up(index=len(self.array) - 1)

    def _bubble_down(self, index):
        min_child_index = self._find_smaller_child(index)
        if min_child_index == -1:
            return
        if self.array[index] > self.array[min_child_index]:
            self.array[index], self.array[min_child_index] = self.array[min_child_index], self.array[index]
            self._bubble_down(min_child_index)

    def _bubble_up(self, index):
        if index == 0:
            return
        index_parent = (index - 1) // 2
        if self.array[index] < self.array[index_parent]:
            self.array[index], self.array[index_parent] = self.array[index_parent], self.array[index]
            self._bubble_up(index_parent)

    def _find_smaller_child(self, index):
        left_child_index = index * 2 + 1
        right_child_index = index * 2 + 2
        if right_child_index >= len(self.array):
            if left_child_index >= len(self.array):
                return -1
            else:
                return left_child_index
        else:
            if self.array[left_child_index] < self.array[right_child_index]:
                return left_child_index
            else:
                return right_child_index


heap = MinHeap()
print(heap.peek_min())
heap.insert(20)
print(heap.array[0])
heap.insert(5)
heap.insert(15)
heap.insert(22)
heap.insert(3)
print(heap.peek_min())
mins = []
while heap:
    mins.append(heap.extract_min())
print(mins)
