from typing import List


def ArrayChunk(M: List[int]) -> int:
    supporting_element_index: int = len(M) // 2
    supporting_element: int = M[supporting_element_index]
    i1: int = 0
    i2: int = len(M) - 1
    while True:
        if M[i1] < supporting_element:
            i1 += 1
            continue
        if M[i2] > supporting_element:
            i2 -= 1
            continue
        if i1 == i2 - 1 and M[i1] > M[i2]:
            M[i1], M[i2] = M[i2], M[i1]
            i1 = 0
            i2 = len(M) - 1
            supporting_element_index = len(M) // 2
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
