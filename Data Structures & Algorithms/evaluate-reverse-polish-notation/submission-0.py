class Node:
    def __init__(self, data, current_min):
        self.data = data
        self.current_min = current_min
        self.next = None

class MinStack:

    def __init__(self):
        self.head = None
        self._size = 0

    def push(self, data: int) -> None:
        if self.is_empty():
            current_min = data
        else:
            current_min = min(data, self.head.current_min)
        new_node = Node(data, current_min)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def is_empty(self):
        return self.head is None

    def pop(self) -> None:
        if self.is_empty():
            raise IndexError('stack is empty')
        popped_node = self.head
        self.head = self.head.next
        self._size -= 1
        return popped_node.data

    def top(self) -> int:
        if self.is_empty():
            raise IndexError('stack is empty') 
        return self.head.data

    def getMin(self) -> int:
        if self.is_empty():
            raise IndexError('stack is empty') 
        return self.head.current_min

        

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = MinStack()
        for char in tokens:
            if char not in ['+', '*', '-', '/']:
                stack.push(int(char))
            else:
                b = stack.pop()
                a = stack.pop()
                if char == '+':
                    stack.push(a+b)
                elif char == '*':
                    stack.push(a*b)
                elif char == '-':
                    stack.push(a-b)
                elif char == '/':
                    stack.push(int(a/b))
        return stack.pop()

        