"""Design a food ordering system where your python program will run two threads,

 + Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order
 + every 0.5 second. (hint: use time.sleep(0.5) function)

 + Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. 
 +This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started."""


# Queue
from queues import MyQueue

# Utils
import threading
import time

q = MyQueue()

def place_orders(orders):
    """Process the orders."""
    for order in orders:
        print('Placing order:', order)
        q.enqueue(order)
        time.sleep(0.5)

def serve_orders():
    time.sleep(1)
    while q.size()!=0:
        print('Serving:', q.dequeue())
        time.sleep(2)

if __name__ == "__main__":
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=place_orders, args=(orders,))
    t2 = threading.Thread(target=serve_orders)

    t1.start()
    t2.start()






