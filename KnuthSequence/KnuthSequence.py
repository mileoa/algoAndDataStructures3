from typing import List


def KnuthSequence(array_size: int) -> List[int]:
    if array_size == 0:
        return [1]
    sequence: List[int] = []
    n = 1
    while array_size >= n:
        sequence.append(n)
        n = n * 3 + 1
    sequence.reverse()
    return sequence
