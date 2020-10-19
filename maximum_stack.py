class MaxStack:
    stack = []
    max_element = 0
    # def __init__(self):

    def push(self, val):
        if val > self.max_element:
            delta = 2 * val - self.max_element
            self.max_element = val
            val = delta
        self.stack.append(val)

    def pop(self):
        item = self.stack.pop()
        if item <= self.max_element:
            return item
        else:
            max = self.max_element
            self.max_element = 2 * self.max_element - item
            return max


    def max(self):
        return self.max_element

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
s.push(4)
s.push(5)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2
