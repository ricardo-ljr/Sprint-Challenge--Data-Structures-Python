from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * capacity

    def append(self, item):
        self.storage[self.current] = item

        if self.current >= self.capacity - 1:
            self.current = 0
        else:
            self.current += 1

    def get(self):
        return [item for item in self.storage if item is not None]


# Ring Buffer with Doubly Linked List
# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.current = 0
#         self.storage = DoublyLinkedList()

#     def append(self, item):
#         if self.current == 0:
#             if not self.storage.head:
#                 self.storage.add_to_tail(item)
#             else:
#                 self.storage.head.value = item
#         else:
#             i = 0
#             current_node = self.storage.head
#             while i < self.current:
#                 if not current_node.next:
#                     self.storage.add_to_tail(item)
#                 else:
#                     current_node = current_node.next
#                     i += 1
#             current_node.value = item

#         self.current += 1

#         if self.current >= self.capacity:
#             self.current = 0

#     def get(self):
#         list_contents = []

#         start_node = self.storage.head
#         list_contents.append(start_node.value)
#         while start_node.next is not None:
#             start_node = start_node.next
#             list_contents.append(start_node.value)
#         return list_contents
