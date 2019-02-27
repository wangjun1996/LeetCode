# Runtime: 60 ms, faster than 46.58%    最小栈
# Memory Usage: 14.9 MB, less than 9.18%
# 思路：使用数组实现，数组元素为(x, curMin),每次入栈时将待插入值x和当前栈内最小值curMin插入栈中

class MinStack:
    def __init__(self):
        self.q = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.q.append((x, curMin))

    # @return nothing
    def pop(self):
        self.q.pop()

    # @return an integer
    def top(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[-1][0]

    # @return an integer
    def getMin(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[-1][1]

if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.q)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.q)
    print(minStack.top())
    print(minStack.getMin())
    print(minStack.q)

