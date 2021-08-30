## Queue

- is a Linear DS
- the behaviour is First In First Out (LIFO)
- Uses front and rear pointers to perform enqueue() and dequeue() operations


### Operations
- enqueue(): 
    - add a new element to the rear side of the queue
    - if size of queue exceeds causes **OverflowError**
    - complexity: O(1)

- dequeue(): 
    - process element from the front side of the queue
    - if no element exists in queue causes **UnderflowError**
    - complexity: O(1)


### Implementations
    1. Array
    2. Linked List


### Applications
    1. BFS traversal
    2. Playlist of songs


### Drawback:
- space wastage
![queue space wastage](https://media.geeksforgeeks.org/wp-content/uploads/20210208123954/cq4.jpeg)
- The first 2 positions are vacant
- 2 Solutions, 
    - shifting elements to front (costly)
    - circular queue

----

### Types
1. Circular Queue:
- considers array as circular
- queue empty:
    
        front == rear == -1

- queue full:
    
        (front == 0 and rear == max-1) or (front == rear+1)


2. Deque:
- insertion and deletion at both ends

- 4 operations:
    - enq_rear(): same as circular queue
    - deq_front(): same as circular queue
    - enq_front()
    - deq_rear()

- Implementation:
1. Using Dynamic Array
2. Doubly LL

- Applications:
1. Used for PQ
2. maintaing a Playlist of songs
- Next song is played from front of the queue (i.e. playlist)
- "add to queue": add song to the queue (append) 
- "play next": adds song to the front of the queue (appendleft)
3. https://stackoverflow.com/a/15038243/7477462


3. Priority Queue:
- implemented using heap DS

- Applications:
1. Dijkstra's shortest path using PQ
