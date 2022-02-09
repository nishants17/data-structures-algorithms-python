from collections import deque


# stack = deque()

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val: object) -> object:
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def reverse_string(self, ip):
        ip_list = ip.split(" ")
        for i in ip_list:
            i = i[::-1]
            print(i)
            str = ''
            str = ''+i
            self.push(i)
            a = self.pop()
        return str(a)
s = Stack()
#s.is_empty()
s.push(1)
s.push(2)
s.peek()
s.size()
s.reverse_string("We will conquere COVID-19")
#
print("Execution complete")
# print(s)
#reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"

