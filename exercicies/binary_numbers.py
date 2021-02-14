"""Write a program to print binary numbers from 1 to 10 using Queue."""

# Queues
from queues import MyQueue


def get_binary_numbers(numbers):
    q = MyQueue()
    q.enqueue('1')
    for i in range(numbers):
        front = q.front()
        print("  ", front)
        q.enqueue(front + "0")
        q.enqueue(front + "1")

        q.dequeue()

if __name__ == "__main__":
    get_binary_numbers(10)

    

