# def sum_above_threshold(numbers: list[int], threshold) -> int: 
#     sum = 0 
#     for i in numbers: 
#         if i > threshold: 
#             sum = sum +i 
#     return sum

def rotate_left(elements: list, k: int) -> list: 
    n = len(elements)
    k = k % n  
    elements[:] = elements[k:] + elements[:k]  
    return elements