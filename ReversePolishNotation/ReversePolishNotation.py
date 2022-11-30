from tokenize import Double


string = "6 6 * 2 7 * - 2 /"
A = string.split( )
stack = []
for i in A:
#times operation
    if i == "*":
        a = stack.pop()
        b = stack.pop()
        stack.append(int(b) * int(a))
# subtract operation
    elif i == "-":
        a = stack.pop()
        b = stack.pop()
        stack.append(int(b) - int(a))
#division operation
    elif i == "/":
        a = stack.pop()
        b = stack.pop()
        stack.append(int(b)//int(a))
#plus operation
    elif i == "+":
        a = stack.pop()
        b = stack.pop()
        stack.append(int(b)+int(a))
#number
    else:
        stack.append(int(i))

print(stack)
