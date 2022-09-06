'''
两个队列实现栈
'''
import queue


class MyStack:

    def __init__(self):
        self.list1 = []
        self.list2 = []

    def push(self, x: int) -> None:
        if not self.list1:
            self.list1.append(x)
            return
        while self.list1:
            t = self.list1[0]
            self.list2.append(t)
            del self.list1[0]

        self.list1.append(x)

        while self.list2:
            t = self.list2[0]
            self.list1.append(t)
            del self.list2[0]

    def pop(self) -> int:
        if not self.list1:
            return -1
        t = self.list1[0]
        del self.list1[0]
        return t



    def top(self) -> int:
        return self.list1[0]

    def empty(self) -> bool:
        return True if len(self.list1) == 0 else False