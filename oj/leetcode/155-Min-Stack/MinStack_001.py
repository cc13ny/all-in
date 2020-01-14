class MinStack:
    # @param x, an integer
    
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        
        if len(self.min_stack) == 0 or self.min_stack[-1] >= x:
            self.min_stack.append(x)
        

    # @return nothing
    def pop(self):
        num = self.stack.pop(-1)
        if self.min_stack[-1] == num:
            self.min_stack.pop(-1)
            
    # @return an integer
    def top(self):
        return self.stack[-1]
        
    # @return an integer
    def getMin(self):
        return self.min_stack[-1]
