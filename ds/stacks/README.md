## Stacks

- is a Linear DS
- the behaviour is Last In First Out (LIFO)
- top pointer is used to keep track of top most element


### Operations
- push(): 
    - add a new element on top of stack
    - if size of stack exceeds causes **OverflowError**
    - complexity: O(1)

- pop(): 
    - remove element at top of stack
    - if no element exists in stack causes **UnderflowError**
    - complexity: O(1)


### Implementations
    1. Array
    2. Linked List


### Applications
    1. function call states are maintained using stack (often demonstrated in recursion)
    2. Polish notation (infix, prefix, postfix) evaluation
    3. DFS traversal
