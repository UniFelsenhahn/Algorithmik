'''
Erweitert die beiden Queue-Implementierungen (Dictionaries und Klassen) aus der Vorlesung, sodass auch folgende Methoden zur Verfügung stehen:

list_to_queue(self, list), welche eine Liste in eine Queue umwandelt (diese Methode kann auch noch schöner als statische Methode list_to_queue(list) realisiert werden),
queue_to_list(self), welche eine Queue in eine Liste umwandelt,
undequeue(self, value), welche ein Element am Leseende hinzufügt,
unenqueue(self), welche ein Element vom Schreibende entfernt (diese Funktion muss nicht effizient realisiert werden).
Skizziert außerdem eine Idee, wie man auch unenqueue ebenfalls in konstanter Laufzeit realisieren könnte.

'''

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

    def __init__(self):
        new_head = ListElem()
        self.head = new_head # pointer to head element of linked list
        self.end = new_head  # pointer to end element of linked list
        
    def enqueue(self,value):
        
        old_end = self.end
        old_end.update(value, ListElem())
        self.end = old_end.next

    def top(self):
        
        if self.head.value != None:
            return self.head.value
        else:
            return None

    def dequeue(self):
       
        head = self.head
        if head.value != None:
            self.head = self.head.next
            return head.value
        else:
            return None

    #------- Homework -----------#

    def list_to_queue(self, list):
        pass
        ####Hier wird Code geschrieben

    def queue_to_list(self):
        pass
         ####Hier wird Code geschrieben
    def undequeue(self, value):
        pass
         ####Hier wird Code geschrieben
    def unenqueue(self):
        pass
         ####Hier wird Code geschrieben



         
# test code
q = Queue()
q.enqueue(42)
q.enqueue(73)
print(q.top())
print(q.dequeue())
q.enqueue(55)
print(q.dequeue())
print(q.dequeue())
