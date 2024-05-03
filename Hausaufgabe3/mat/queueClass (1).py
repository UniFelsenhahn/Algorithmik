class ListElem():

    '''
    auxiliary class to model elemnts in the linked list (verkettete Liste)
    represents simply a mutable pair of values
    '''
    def __init__(self):
        '''
        construct an empty element
        '''
        self.value = None
        self.next = None

    def update(self, value, next):
        '''
        updete an existing element with given values
        '''
        self.value = value
        self.next = next

class Queue():
    
    '''
    implementation of a queue (FIFO) by means of a linked list
    with class ListElem
    '''
    def __init__(self):
        new_head = ListElem()
        self.head = new_head # pointer to head element of linked list
        self.end = new_head  # pointer to end element of linked list
        
    def enqueue(self,value):
        '''
        add an element at the end position of the queue
        '''
        old_end = self.end
        old_end.update(value, ListElem())
        self.end = old_end.next

    def top(self):
        '''
        return oldest value in the queue
        if queue is empty return None
        '''
        if self.head.value != None:
            return self.head.value
        else:
            return None

    def dequeue(self):
        '''
        return oldest value from the queue and return it
        if queue is empty return None
        '''
        head = self.head
        if head.value != None:
            self.head = self.head.next
            return head.value
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
