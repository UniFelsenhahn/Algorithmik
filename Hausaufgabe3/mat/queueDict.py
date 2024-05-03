def empty_queue():
    '''
    construct an empty queue (FIFO) encoded as dictonary
    '''
    new_head = {}
    return {'head': new_head, 'end' : new_head}

def enqueue(queue,value):
    '''
    mutate queue such that value is added to the queue
    '''
    old_end = queue['end']
    old_end['next'] = {}
    old_end['value'] = value
    queue['end'] = old_end['next']

def top(queue):
    '''
    return oldest element in the queue
    '''
    return queue['head']['value']

def dequeue(queue):
    '''
    return and remove oldest element from the queue
    '''
    head = queue['head']
    if 'value' in head:
        queue['head'] = head['next']
        return head['value']
    else:
        return None

# test code
q = empty_queue()
enqueue(q, 42)
enqueue(q, 73)
print(top(q))
print(dequeue(q))
enqueue(q, 55)
print(dequeue(q))
print(dequeue(q))
