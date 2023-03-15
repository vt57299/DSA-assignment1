# Evaluate a postfix expression using stack

'''A postfix expression is a mathematical notation in which operators follow their operands. 
It is also known as Reverse Polish Notation (RPN). 
In postfix notation, the order of operations is determined by the position of the operator 
and its operands rather than by the use of parentheses or operator precedence.

For example, the infix expression 3 + 4 * 5 can be written in postfix notation as 3 4 5 * +. 
In this expression, * comes after its two operands 4 and 5, indicating that they should be multiplied first. 
Then + comes after its two operands 3 and the result of 4 * 5, indicating that they should be added.'''

def postfixEX(expression):
    stack = []                                    # creating empty stack
    temp = ''                                     # Empty string

    for char in expression:
        if char.isdigit():                        # If character is int type adding it to temp empty string
            temp += char                          # and if it's more than one digit adding whole digit in temp
        
        elif char.isspace():                      
            if temp:                              
                stack.append(int(temp))           # If character is space appending temp string to stack  
                temp = ""                         # Also, making temp empty again

        else:
            if temp:
                stack.append(int(temp))
                temp = ''           
            
            num2 = stack.pop()                    # Popping the last element of stack
            num1 = stack.pop()                    # popping 2nd last element of stack

            if char == "+":
                stack.append(num1+num2)

            elif char == "-":
                 stack.append(num1-num2)

            elif char == "/":
                 stack.append(num1/num2)

            elif char == "*":
                 stack.append(num1*num2)

            elif char == "%":
                stack.append(num1%num2)

            elif char == "**":
                stack.append(num1**num2)
                
            else:
                raise ValueError("invalid character in expression!!!")
    return stack.pop()



# --------------------------------Do enter expression with space---------------------------
s = "10 2 444 * +"
print(postfixEX(s))