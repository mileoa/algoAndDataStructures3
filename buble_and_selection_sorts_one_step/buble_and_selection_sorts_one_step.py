from typing import List, Tuple


def find_min_el_and_index(array: List[int], start: int = 0) -> Tuple[int, int]:
    min_el_index: int = start
    min_el: int = array[start]
    for index, el in enumerate(array):
        if index < start + 1:
            continue
        if el < min_el:
            min_el_index = index
            min_el = el
    return (min_el_index, min_el)


def SelectionSortStep(array: List[int], i: int) -> None:
    if i + 1 >= len(array):
        return None
    next_min_el: int
    next_min_el_index: int
    next_min_el_index, next_min_el = find_min_el_and_index(array, i + 1)
    array[i], array[next_min_el_index] = next_min_el, array[i]
    return None


def BubbleSortStep(array: List[int]) -> bool:
    was_switch: bool = False
    for i, el in enumerate(array):
        if i == len(array) - 1:
            continue
        if el > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], el
            was_switch = True
    return was_switch
