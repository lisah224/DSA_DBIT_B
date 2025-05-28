class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop() if not self.is_empty() else None
    
    def peek(self):
        return self.stack[-1] if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.stack) == 0

 #Example usage
s = Stack()
s.push(10)
s.push(20)
print(s.pop()) 
print(s.peek())