class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.instack = []
        self.outstack = []
        self.insize = 0
        self.outsize = 0
        
    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.instack.append(x)
        self.insize += 1
        
    # @return nothing
    def pop(self):
        while self.insize > 1:
            top = self.instack.pop()
            self.outstack.append(top)
            self.insize -= 1
            self.outsize += 1
        if self.insize == 1:
            self.instack.pop()
            self.insize -= 1
            while self.outsize > 0:
                top = self.outstack.pop()
                self.instack.append(top)
                self.insize += 1
                self.outsize -= 1
                
    # @return an integer
    def peek(self):
        while self.insize > 1:
            top = self.instack.pop()
            self.outstack.append(top)
            self.insize -= 1
            self.outsize += 1
        if self.insize == 1:
            res = self.instack[-1]
            while self.outsize > 0:
                top = self.outstack.pop()
                self.instack.append(top)
                self.insize += 1
                self.outsize -= 1
            return res
            
    # @return an boolean
    def empty(self):
        return self.insize == 0
