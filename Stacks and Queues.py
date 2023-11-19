# my Implementation for stack and queue to solve the questions
class stack:
    def __init__(self):
        self.my_stack = []

    def push(self, new_data):
        self.my_stack.append(new_data)

    def pop(self):
        return self.my_stack.pop()

    def size(self):
        return len(self.my_stack)

    def top(self):
        return self.my_stack[-1]

    def empty(self):
        if len(self.my_stack) == 0:
            return True
        else:
            return False


class queue:
    def __init__(self):
        self.my_queue = []

    def enqueue(self, new_data):
        self.my_queue.append(new_data)

    def dequeue(self):
        self.my_queue.pop(0)

    def front(self):
        return self.my_queue[-1]

    def back(self):
        return self.my_queue[0]

    def size(self):
        return len(self.my_queue)

    def empty(self):
        if len(self.my_queue) == 0:
            return True
        else:
            return False


# ----------------------------------------------------------------
# Implement a stack using two queues.

class stack_with_two_queues:
    def __init__(self):
        self.q1 = queue()
        self.q2 = queue()

    def push(self, new_data):
        self.q2.enqueue(new_data)
        while self.q1.empty() == False:
            self.q2.enqueue(self.q1.dequeue())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if self.q1.empty():
            return
        self.q1.pop()

    def top(self):
        if self.q1.empty():
            return
        return self.q1.front()

    def size(self):
        return self.q1.size()

    def empty(self):
        return self.q1.empty()


# ----------------------------------------------------------------
# Implement a queue using two stacks.

class queue_with_two_stacks:

    def __init__(self):
        self.s1 = stack()
        self.s2 = stack()

    def enqueue(self, new_data):
        while self.s1.empty() == False:
            self.s2.push(self.s1.pop())

        self.s1.push(new_data)

        while self.s2.empty() == False:
            self.s1.push(self.s2.pop())

    def dequeue(self):
        return self.s1.pop()

    def size(self):
        return self.s1.size()

    def empty(self):
        return self.s1.empty()

    def front(self):
        return self.s1.top()

    def back(self):
        while self.s1.empty() == False:
            self.s2.push(self.s1.pop())

        res = self.s2.top()

        while self.s2.empty() == False:
            self.s1.push(self.s2.pop())

        return res


# ----------------------------------------------------------------
# Function to check if a given string of parentheses is balanced.

def is_parentheses_balanced(str):
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    lst = []
    for i in str:
        if i in open_list:
            lst.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(lst) > 0) and
                    (open_list[pos] == lst[len(lst) - 1])):
                lst.pop()
            else:
                return "Unbalanced"
    if len(lst) == 0:
        return "Balanced"
    else:
        return "Unbalanced"
