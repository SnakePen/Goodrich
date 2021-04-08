#Implement a function with signature transfer(S, T) that transfers all elements from stack 
# S onto stack T, so that the element that starts at the top of S is the first to be 
# inserted onto T, and the element at the bottom of S ends up at the top of T.
from practice.stackADT import ArrayStack
S= ArrayStack()

S.push(3)
S.push(5)
S.push(7)

while S.is_empty is False:
    print(S.pop())
print(S.top())