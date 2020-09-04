# Algorithms 4th edition Linked List problems (pg 164)

class Node:
    def __init__(self, data=None):
        self.value = data
        self.next = None

class LinkedList:
    def __init__(self,data=None):
        self.head = Node(data)
        self.tail = Node()

    def insert(self, data):
        node = self.head
        while node.next != None:
            node = node.next
        node.next = Node(data)
        self.tail = node.next


    def insert_range(self,data):
        prev_node = self.head
        for n in range(data):
            new_node = Node(n)
            new_node.next = self.head
            prev_node.next = new_node
            prev_node = node
            print("inserted",new_node.value,"with prev node of",prev_node.value)

    def delete(self, k: int):
        if k == 0 and self.head.next:
            self.head = self.head.next
            return True
        node = self.head
        counter = 1
        while node.next != None:
            if counter == k:
                node.next = node.next.next
                return True
            counter += 1
            node = node.next
        return False

    def find(self, key: str):
        node = self.head
        while node.next != None:
            if node.value == key:
                print("Found!")
                return True
            node = node.next
        return False


    def max(self):
        current_max = 0
        node = self.head
        while node.next != None:
            if node.value == None:
                node = node.next
                continue
            if node.value > current_max:
                current_max = node.value
            node = node.next
        if node.value > current_max:
            current_max = node.value
        return current_max

    def max_recursive(self, current_node=None, current_max=0):
        if current_node == None:
            current_node = self.head
        if current_node.next == None:
            if current_node.value > current_max:
                current_max = current_node.value
            # print("max found is",current_max)
            return current_max
        if current_node.value > current_max:
            current_max = current_node.value
        current_max = self.max_recursive(current_node.next,current_max)
        return current_max


    def print(self):
        node = self.head
        while node.next != None:
            print(node.value)
            node = node.next
        print(node.value)

class CircularLinkedList:
    def __init__(self,data=None):
        self.head = Node(data)

    def insert_range(self,data):
        prev_node = self.head
        for n in range(data):
            if prev_node.value == None:
                prev_node.value = n
                continue
            new_node = Node(n)
            prev_node.next = new_node
            new_node.next = self.head
            prev_node = new_node

    def delete(self, k: int):
        if k == 0 and self.head.next:
            self.head = self.head.next
            return True
        node = self.head
        counter = 1
        while node.next != None:
            if counter == k:
                node.next = node.next.next
                return True
            counter += 1
            node = node.next
        return False

    def delete_every_k(self, k: int):
        if k == 0 and self.head.next:
            self.head = self.head.next
            return True
        node = self.head
        prev_node = node
        counter = 0
        list_length = LL.len() - 1
        while list_length != 1: # node.next != self.head # for i in range(LL.len() // k * k): # while LL.len() != 1: # node.next != self.head:
            counter += 1
            if list_length == 1:
                print("last node standing! inner")
                print(node.value)
                break
            if counter % k == 0:
                prev_node.next = node.next
                node = node.next
                list_length -= 1
                counter = 0
                continue
            prev_node = node
            node = node.next
        print("last node standing! outer",node.value)
        self.head = node
        # print(node.value)

    def len(self):
        length = 1
        node = self.head
        while node.next != self.head:
            length += 1
            node = node.next
        return length


    def find(self, key: str):
        node = self.head
        while node.next != None:
            if node.value == key:
                print("Found!")
                return True
            node = node.next
        return False


    def print(self):
        node = self.head
        prev_node = node
        while node.next != self.head:
            print(node.value)
            node = node.next
            prev_node = node
            if node == prev_node:
                break
        # print(node.value)
        # print("---")

# Problem 1.3.19 - remove the last node in a linked list.
print("-"*25)
print("Problem 1.3.19")
# ---------------------------------------------------------------------------
node1 = Node(4)
node2 = Node("hello")
node1.next = node2
node3 = Node(1.1)
node2.next = node3


node = node1
prev_node = node
while node.next != None:
    prev_node = node
    print("prev node is",prev_node.value)
    node = node.next
    print("now is changing to",node.value,"with next of ",node.next)
node = prev_node
print("prev node is",node.value,"setting next to None...")
node.next = None
print("prev node's next now is ",node.next)

# ---------------------------------------------------------------------------
# Problem 1.3.20 - define a delete() to remove a specific item in a linked list if it exists.
print("-"*25)
print("Problem 1.3.20")
# ---------------------------------------------------------------------------
LL = LinkedList()
LL.insert(4)
LL.insert(33)
LL.insert(100)
LL.print()
print("---")
print(LL.delete(0))
print("---")
LL.print()
LL.insert("eeeee")
print("---")
LL.print()

# Problem 1.3.21 - define find() - boolean - see above
print(LL.find(1))
print(LL.find(4))


# ---------------------------------------------------------------------------
# Problem 1.3.27 - define a max() to find the max in the LL.
print("-"*25)
print("Problem 1.3.27")
# ---------------------------------------------------------------------------
LL = LinkedList()
LL.insert(1)
LL.insert(33)
LL.insert(100)
print("max is ",LL.max())

# ---------------------------------------------------------------------------
# Problem 1.3.28- define a recursive max() to find the max in the LL.
print("-"*25)
print("Problem 1.3.28")
# ---------------------------------------------------------------------------
LL = LinkedList(5)
LL.insert(1)
LL.insert(33)
LL.insert(105555)
print("recursive max is ",LL.max_recursive())


# ---------------------------------------------------------------------------
# Problem 1.3.37 - define a recursive max() to find the max in the LL.
print("-"*25)
print("Problem 1.3.37")
# ---------------------------------------------------------------------------

LL = CircularLinkedList()
LL.insert_range(9)
LL.delete_every_k(2)
LL.print()
# LL.delete_every_k(2)
# LL.print()