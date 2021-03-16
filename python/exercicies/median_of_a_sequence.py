"""Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.
Recall that the median of an even-numbered list is the average of the two middle numbers in a sorted list."""

def calculate_median(elements):
    if elements:
        total = 0
        for i in elements:
            total += i

        median = total / len(elements)
        return round(median, 2)

def insertion_sort(elements):
    iterations = 0
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        iterations += 1

        median = calculate_median(elements[:i])
        print(f'The median in iteration {iterations} is {median}')

        while j >=0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = anchor
        

if __name__ == "__main__":
    elements = [2, 1, 5, 7, 2, 0, 5]
    insertion_sort(elements)
    print(elements)

    
