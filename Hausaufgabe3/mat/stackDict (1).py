def empty_stack():
    '''
    construct an empty stack (LIFO) encoded as dictonary
    '''
    return {'head': {}}

def push(stack,value):
    '''
    mutate stack such that value is pushed to the stack
    '''
    new_head = {'value' : value, 'next' : stack['head']}
    stack['head'] = new_head

def top(stack):
    '''
    return jungest element in the stack
    '''
    return stack['head']['value']

def pop(stack):
    '''
    return and remove jungest element from the stack
    '''
    head = stack['head']
    if 'value' in head:
        stack['head'] = head['next']
        return head['value']
    else:
        return None

# test code
s = empty_stack()
push(s,42)
push(s,73)
print(top(s))
print(pop(s))
push(s,55)
print(pop(s))
print(pop(s))
print(pop(s))
