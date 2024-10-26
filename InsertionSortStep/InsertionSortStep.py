from typing import List


def InsertionSortStep(array: List[int], step: int, i: int) -> None:
    subarray_to_sort: List[int] = []
    for index in range(i, len(array), step):
        subarray_to_sort.append(array[index])

    for current_index, current_element in enumerate(subarray_to_sort):
        if current_index == 0:
            continue
        for index_prev in range(current_index):
            if current_element < subarray_to_sort[index_prev]:
                subarray_to_sort.insert(index_prev, subarray_to_sort.pop(current_index))
                break

    for index in range(i, len(array), step):
        array[index] = subarray_to_sort.pop(0)
    return None
