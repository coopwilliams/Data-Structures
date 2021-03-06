"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        print(self, self.next, self.prev)
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        if self.prev and not self.next:
            self.prev.next = None
        if self.next and not self.prev:
            self.next.prev = None

        def insert_node_before(self, node):
            self.prev, node.next = node, self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        def count_tail(node):
            if node == None:
                return 0
            if node.id:
                print(node.id)
            if node.next == None:
                return 1
            else:
                return 1 + count_tail(node.next)
        return count_tail(self.head)

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        if self.head == None:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            self.head.insert_before(value)
            self.head = self.head.prev

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.tail == self.head:
            if self.head == None:
                return None
            else:
                result = self.head.value
                self.head = None
                self.tail = None
        else:
            result = self.head.value
            temp = self.head.next
            self.head.next.prev = None
            self.head = temp
        return result

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if self.tail == None:
            self.tail = ListNode(value)
            self.head = self.tail
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.tail == self.head:
            if self.tail == None:
                return None
            else:
                result = self.tail.value
                self.head = None
                self.tail = None
        else:
            print('removing from tail')
            result = self.tail.value
            temp = self.tail.prev
            self.tail.prev.next = None
            self.tail = temp
        return result

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        self.delete(node)
        if self.head:
            self.head.prev, node.next = node, self.head
        else:
            self.head = node
        node.prev = None

    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        node.delete()
        if node == self.tail:
            print("removing tail")
            self.remove_from_tail()
        if node == self.head:
            self.remove_from_head()

    """Returns the highest value currently in the list"""
    def get_max(self):
        def check_tail(node, highest):
            if node.value != None:
                if node.next != None:
                    return max(node.value, highest, check_tail(node.next, highest))
                else:
                    return max(node.value, highest)
            else:
                return highest
        return check_tail(self.head, self.head.value)

mynode = ListNode(5)
dll = DoublyLinkedList(mynode)
