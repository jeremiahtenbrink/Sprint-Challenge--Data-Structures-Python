from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.current == None:
            self.storage.add_to_tail(item)
            self.current = 1
            return

        if self.storage.length == self.capacity:
            node = self.storage.head

            for i in range(self.current):
                if node.next is not None:
                    node = node.next

            node.value = item
        else:
            self.storage.add_to_tail(item)

        self.current += 1
        if self.current == self.capacity:
            self.current = 0

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        node = self.storage.head
        for i in range(self.capacity):
            if node != None:
                list_buffer_contents.append(node.value)
                node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * capacity

    def append(self, item):
        self.storage[self.current] = item
        self.current += 1
        if self.current == self.capacity:
            self.current = 0

    def get(self):
        return [item for item in self.storage if item is not None]
