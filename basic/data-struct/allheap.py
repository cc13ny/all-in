class Heap(object):
    def __init__(self, arr = [], isMin = True):
        self.hp = arr
        self.heapify()
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
        try:
            top = self.hp[0]
            self.hp[0] = self.hp[-1]
            self.hp.pop()
            self.siftdown(i)
        except IndexError:
            print "Pop from an empty heap is not allowed!"
        return top
    
    #def delettop(self):
    #    self.pop()
    
    #Creation
    def heapify(self):
        size = len(self.hp)
        for i in range((size - 2) / 2, -1, -1):
            self.siftdown(i)
            
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
        size = len(self.hp)
        hp = self.hp
        ext = i
        while -1 < i < size:
            l = 2 * i + 1
            r = 2 * i + 2
            if -1 < l < size and self.compare(l, ext):
                ext = l
            if -1 < r < size and self.compare(r, ext):
                ext = r
            if i == ext:
                break
            h[i], h[ext] = h[ext], h[i]
            i = ext
        self.hp = hp
        
    def siftup(self, i):
        pass

    def delete(self):
        pass

    #Util
    def compare(i, j):
        hp = self.hp
        if isMin:
            return hp[i] < hp[j]
        else:
            return hp[i] > hp[i]
    
        
    
