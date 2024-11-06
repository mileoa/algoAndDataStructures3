from typing import List


def ArrayChunk(M: List[int], L: int, R: int) -> int:
    supporting_element_index: int = (R + L) // 2
    supporting_element: int = M[supporting_element_index]
    i1: int = L
    i2: int = R
    while True:
        if M[i1] < supporting_element:
            i1 += 1
            continue
        if M[i2] > supporting_element:
            i2 -= 1
            continue
        if i1 == i2 - 1 and M[i1] > M[i2]:
            M[i1], M[i2] = M[i2], M[i1]
            i1 = L
            i2 = R
            supporting_element_index = (R + L) // 2
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


def KthOrderStatisticsStep(Array: List[int], L: int, R: int, k: int) -> List[int]:
    if L > R:
        return [L, R]
    supporting_element_index: int = ArrayChunk(Array, L, R)
    if k == supporting_element_index:
        return [L, R]
    new_right_index: int = R
    new_left_index: int = L
    if supporting_element_index > k:
        new_right_index = supporting_element_index - 1
    if supporting_element_index < k:
        new_left_index = supporting_element_index + 1
    return KthOrderStatisticsStep(Array, new_left_index, new_right_index, k)
