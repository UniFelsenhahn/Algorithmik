class Queue():
    
    '''
    implementation of a queue (FIFO) by means of a linked list encoded
    with nested dictionaries
    '''
    def __init__(self):
        new_head = {}
        self.head = new_head # pointer to head element of linked list
        self.end  = new_head # pointer to end element of linked list
        
    def enqueue(self,value):
        '''
        add an element at the end position of the queue
        '''
        old_end = self.end
        old_end['next'] = {}
        old_end['value'] = value
        self.end = old_end['next']


    def top(self):
        '''
        return oldest value in the queue
        if queue is empty return None
        '''
        if 'value' in self.head:
            return self.head['value']
        else:
            return None
        
    def dequeue(self):
        '''
        return oldest value from the queue and return it
        if queue is empty return None
        '''
        head = self.head
        if 'value' in head:
            self.head = head['next']
            return head['value']
        else:
            return None

# test code
q = Queue()
q.enqueue(42)
q.enqueue(73)
print(q.top())
print(q.dequeue())
q.enqueue(55)
print(q.dequeue())
print(q.dequeue())
