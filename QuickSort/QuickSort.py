from typing import List


def ArrayChunk(M: List[int], left, right) -> int:
    supporting_element_index: int = (right - left) // 2 + left
    supporting_element: int = M[supporting_element_index]
    i1: int = left
    i2: int = right
    while i1 <= i2:
        if M[i1] < supporting_element:
            i1 += 1
            continue
        if M[i2] > supporting_element:
            i2 -= 1
            continue
        if i1 == i2 - 1 and M[i1] > M[i2]:
            M[i1], M[i2] = M[i2], M[i1]
            i1 = left
            i2 = right
            supporting_element_index = (right - left) // 2 + left
            supporting_element = M[supporting_element_index]
            continue
        if i1 == i2 or (i1 == i2 - 1 and M[i1] < M[i2]):
            return supporting_element_index
        M[i1], M[i2] = M[i2], M[i1]
        if i1 == supporting_element_index:
            supporting_element_index = i2
            continue
        if i2 == supporting_element_index:
            supporting_element_index = i1
    return supporting_element_index


def QuickSort(array: List[int], left: int, right: int) -> None:
    if (
        left == right
        or left >= len(array)
        or right < 0
        or left < 0
        or right >= len(array)
        or left > right
    ):
        return None
    supporting_element_index: int = ArrayChunk(array, left, right)
    QuickSort(array, left, supporting_element_index - 1)
    QuickSort(array, supporting_element_index + 1, right)
    return None
