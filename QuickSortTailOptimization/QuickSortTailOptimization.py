from typing import List
from collections import deque


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


def QuickSortTailOptimization(array: List[int], left: int, right: int) -> None:
    if len(array) == 0:
        return None
    return QuickSortTailOptimization_recursive(array, left, right, deque())


def QuickSortTailOptimization_recursive(
    array: List[int], left: int, right: int, stack: deque
) -> None:
    supporting_element_index: int = ArrayChunk(array, left, right)
    next_left: int = supporting_element_index + 1
    next_right: int = supporting_element_index - 1
    if left != next_right and left < next_right:
        stack.append((left, next_right))
    if right != next_left and right > next_left:
        stack.append((next_left, right))
    if len(stack) == 0:
        return None
    return QuickSortTailOptimization_recursive(array, *stack.pop(), stack)
