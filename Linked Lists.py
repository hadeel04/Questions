#Linked list class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


# Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

# Function to Find the middle elment of the linked list
    def Find_Middle(self):
        ptr_1step = self.head
        ptr_2step = self.head

        if self.head is not None:
            while (ptr_2step is not None and ptr_2step.next is not None):
                ptr_2step = ptr_2step.next.next
                ptr_1step = ptr_1step.next
            return ptr_1step.data

#Function to detect if a linked list has a cycle

    def has_Loop(self):
        ptr_1step = self.head
        ptr_2step = self.head
        while (ptr_1step and ptr_2step and ptr_2step.next):
            ptr_1step = ptr_1step.next
            ptr_2step = ptr_2step.next.next
            if ptr_1step == ptr_2step:
                return True
        return False


    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next


llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
llist.push(25)


if(llist.has_Loop()):
    print("Loop Found")
else:
    print("No Loop")

print(llist.Find_Middle())
print("Given Linked List")
llist.printList()
llist.reverse()
print("\nReversed Linked List")
llist.printList()



