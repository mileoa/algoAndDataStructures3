from typing import List, Optional


class BinarySearch:

    def __init__(self, sorted_array: List[int]) -> None:
        self.sorted_array: List[int] = sorted_array
        self.Left: int = 0
        self.Right: int = len(sorted_array) - 1
        self.search_result: str = "0"

    def Step(self, N: int) -> None:
        if self.search_result != "0":
            return None
        mid: int = (self.Left + self.Right) // 2
        if self.sorted_array[mid] == N:
            self.search_result = "+1"
            return None
        if self.sorted_array[mid] < N:
            self.Left = mid + 1
        if self.sorted_array[mid] > N:
            self.Right = mid - 1
        if self.Left - self.Right == 1:
            self.search_result = "-1"
            return None
        return None

    def GetResult(self) -> int:
        return self.search_result
