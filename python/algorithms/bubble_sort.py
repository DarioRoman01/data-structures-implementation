"""Bubble sort implementation."""

from algorithms import time_it

@time_it
def bubble_sort(elements, key):
    size = len(elements)

    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            current = elements[j][key]
            following = elements[j + 1][key]

            if current > following:
                elements[j],elements[j+1] = elements[j+1],elements[j]
                swaped = True

        if not swapped:
            break

if __name__ == "__main__":
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
    bubble_sort(elements, key='transaction_amount')
    print(elements)
