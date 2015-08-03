class Heap(object):
    def __init__(self, isMin = True):
        self.hp = []
        self.isMin = isMin
    #Location
    def parent(self, i):
        return (i - 1) / 2
    def left(self, i):
        return 2 * i + 1
    def right(self, i):
        return 2 * i + 2
    #Basic
    def peek(self):
        return self.hp[0]
    def push(self, num):
        pass
    def pop(self):
        pass
    #def delettop(self):
    #    self.pop()
    
    #Creation
    def heapify(self, arr):
        pass
    def merge(self):
        pass
    def meld(self):
        pass

    #Inspection
    def size(self):
        return len(self.hp)
    def empty(self):
        return len(self.hp) == 0
    #Internal
    def updatekey(self):
        pass
        
    def siftdown(self, i):
        pass
    def siftup(self, i):
        pass
    def delete(self):
        pass
    
        
    
