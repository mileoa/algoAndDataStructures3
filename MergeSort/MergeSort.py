from typing import List


def MergeSort(array: List[int]) -> List[int]:
    if len(array) == 1:
        return array
    left_array: List[int] = MergeSort(array[: len(array) // 2])
    right_array: List[int] = MergeSort(array[len(array) // 2 :])

    result: List[int] = []
    i1: int = 0
    i2: int = 0
    while i1 < len(left_array) and i2 < len(right_array):
        if left_array[i1] <= right_array[i2]:
            result.append(left_array[i1])
            i1 += 1
            continue
        result.append(right_array[i2])
        i2 += 1
    if len(left_array) > i1:
        result.extend(left_array[i1:])
    if len(right_array) > i2:
        result.extend(right_array[i2:])

    return result
