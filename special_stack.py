class SpecialStack:
    def __init__(self):
        self.stack = []
        self.aux = []
        self.tos = -1
        self.atos = -1

    def push(self, ele):
        if self.atos == -1 or ele < self.aux[self.atos]:
            self.aux.append(ele)
            self.atos += 1
        self.stack.append(ele)
        self.tos += 1

    def pop(self):
        item = self.stack.pop()
        self.tos -= 1

        if item == self.aux[self.atos]:
            self.aux.pop()
            self.atos -= 1
        return item

    def get_min(self):
        return self.aux[self.atos]

obj = SpecialStack()
obj.push(9)
obj.push(8)
obj.push(3)
obj.push(17)
obj.push(4)
print(obj.pop())
print(obj.get_min())
obj.push(2)
obj.push(10)
print(obj.get_min())
print(obj.pop())
print(obj.pop())
print(obj.get_min())