"""1 Write a function in python that can reverse a string using stack data structure. Use Stack class.
 + reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW """

# Stack
from stacks import Stack

def reverse_string(string):
    """Return a string backwards."""
    s = Stack()
    reverse_text = ''
    for char in string:
         s.push(char)
    
    s.container.reverse()
    for i in s.container:
        reverse_text += i  

    print(reverse_text)

if __name__ == "__main__":
    reverse_string('We will conquere COVID-19')