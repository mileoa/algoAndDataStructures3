from typing import Optional, List


class Heap:

    def __init__(self) -> None:
        self.HeapArray: list[Optional[int]] = []

    def MakeHeap(self, a: list[int]) -> None:
        heap_size: int = 1
        self.HeapArray = [None] * heap_size
        for node in a:
            if node is None:
                continue
            if not self.Add(node):
                self.add_level()
                self.Add(node)

    def GetMax(self) -> int:
        if self.HeapArray.count(None) == len(self.HeapArray):
            return -1
        last_nonempty_element_index: int = max(
            index for index, value in enumerate(self.HeapArray) if value is not None
        )
        assert self.HeapArray[0] is not None
        max_element: int = self.HeapArray[0]
        self.HeapArray[0] = self.HeapArray[last_nonempty_element_index]
        self.HeapArray[last_nonempty_element_index] = None
        if last_nonempty_element_index == 0:
            return max_element

        current_index: int = 0
        left_child_index: int = current_index * 2 + 1
        right_child_index: int = current_index * 2 + 2
        is_balanced = False
        while (
            not is_balanced
            and left_child_index < len(self.HeapArray)
            and right_child_index < len(self.HeapArray)
        ):
            max_value: int = max(
                self.HeapArray[current_index],
                (
                    self.HeapArray[left_child_index]
                    if self.HeapArray[left_child_index] is not None
                    else self.HeapArray[current_index]
                ),
                (
                    self.HeapArray[right_child_index]
                    if self.HeapArray[right_child_index] is not None
                    else self.HeapArray[current_index]
                ),
            )
            if max_value == self.HeapArray[current_index]:
                is_balanced = True
                continue
            if (
                self.HeapArray[left_child_index] is not None
                and max_value == self.HeapArray[left_child_index]
            ):
                max_value_index: int = left_child_index
            else:
                max_value_index = right_child_index

            self.HeapArray[current_index], self.HeapArray[max_value_index] = (
                self.HeapArray[max_value_index],
                self.HeapArray[current_index],
            )

            current_index = max_value_index
            left_child_index = current_index * 2 + 1
            right_child_index = current_index * 2 + 2

        return max_element

    def Add(self, key: int) -> bool:
        if self.HeapArray.count(None) == 0:
            return False
        last_empty_element_index: int = self.HeapArray.index(None)
        self.HeapArray[last_empty_element_index] = key

        current_index: int = last_empty_element_index
        parent_index: int = (current_index - 1) // 2
        is_balanced = False
        while not is_balanced and parent_index >= 0:
            if self.HeapArray[current_index] <= self.HeapArray[parent_index]:
                is_balanced = True
                continue

            self.HeapArray[current_index], self.HeapArray[parent_index] = (
                self.HeapArray[parent_index],
                self.HeapArray[current_index],
            )

            current_index = parent_index
            parent_index = (current_index - 1) // 2

        return True

    def add_level(self) -> None:
        new_depth: int = 0
        new_size: int = 0
        while new_size <= len(self.HeapArray):
            new_depth += 1
            new_size = 2 ** (new_depth + 1) - 1
        add_size_amount: int = new_size - len(self.HeapArray)
        self.HeapArray += [None] * add_size_amount


class HeapSort:

    def __init__(self, array: List[int]) -> None:
        self.HeapObject: Heap = Heap()
        self.HeapObject.MakeHeap(array)

    def GetNextMax(self) -> int:
        return self.HeapObject.GetMax()
