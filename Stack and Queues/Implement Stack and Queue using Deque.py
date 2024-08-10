from collections import deque

# Function to push element x to the front of the deque.
def push_front_pf(dq, x):
    dq.appendleft(x)

# Function to push element x to the back of the deque.
def push_back_pb(dq, x):
    dq.append(x)
    
# Function to return element from front of the deque.
def front_dq(dq):
    if dq:
        return dq[0]
    return -1  # Return -1 if the deque is empty
    
# Function to pop element from back of the deque.
def pop_back_ppb(dq):
    if dq:
        dq.pop()