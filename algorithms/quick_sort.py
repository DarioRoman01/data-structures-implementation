"""Quick sort implementation with lomuto partition"""

def swap(a, b, arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def partition(elements, end):
    """Lomuto partition implementation."""
    pivot_index = end
    pivot = elements[pivot_index]
    p_index = 0
    
    while elements[p_index] != pivot:
        while elements[p_index] < pivot:
            p_index += 1
        
        i = p_index
        while elements[i] > pivot:
            i += 1
        
        if i > p_index:
            swap(p_index, i, elements)

    return p_index


def quick_sort(elements):
    """Quick sort with lomuto partition."""
    if elements:
        pi = partition(elements, len(elements) - 1)
        for i in range(pi):
            partition(elements, pi - i)


if __name__ == "__main__":
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]
    
    for elements in tests:
        quick_sort(elements)
        print(f'sorted array: {elements}')

    
    