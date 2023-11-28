# hash table

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class hash_table:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):

        index = self.hash(key)
        self.size += 1
        node = self.table[index]

        if node is None:
            self.table[index] = Node(key, value)

        else:
            while node:
                if node.key == key:
                    node.value = value
                    return
                node = node.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node

    def search(self, key):

        index = self.hash(key)
        node = self.table[index]

        while node:
            if node.key == key:
                return node.value
            node = node.next

        return None


    def remove(self, key):

        index = self.hash(key)
        previous = None
        current = self.table[index]

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current
            current = current.next

        return None