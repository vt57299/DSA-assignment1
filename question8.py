# reverse a string using a stack data structure

def rev_str(string):
    stack = []
    for i in string:
        stack.append(i)
    
    rev_string = ""
    for i in range(len(stack)):
        rev_string += stack.pop()
        # print(rev_string)
    return rev_string

s = "hi there"
print(rev_str(s))