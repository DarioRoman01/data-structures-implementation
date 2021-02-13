"""Write a function in python that checks if paranthesis in the string are balanced or not. 
Possible parantheses are "{}',"()" or "[]". Use Stack class.
 + is_balanced("({a+b})")  --> True""" 

# Stack
from stacks import Stack

def is_balanced(string):
    """Check that the paranthesis in a strigng are balanced."""
    s = Stack()
    match_dict = {')': '(',  ']': '[',  '}': '{'}

    for char in string:
        if char in match_dict.values():
            s.push(char)

        elif char in match_dict.keys():
            if s.size() == 0:
                s.push(char)
            elif s.size() != 0 and char != s.peek():
                s.pop()
            else:
                pass
        
    if s.size() != 0:
        return print('False')
    else:
        return print('True')


if __name__ == "__main__":
    is_balanced("({a+b})")
    is_balanced("))((a+b}{")
    is_balanced("((a+b))")
    is_balanced("((a+g))")
    is_balanced("))")
    is_balanced("[a+b]*(x+2y)*{gg+kk}")

