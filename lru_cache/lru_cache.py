from doubly_linked_list import DoublyLinkedList, ListNode

class LRUCache(DoublyLinkedList):
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        super().__init__()
        self.limit = limit
        self.storagedict = {}
        self.idcount = 0

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storagedict.keys():
            print("gotten key is:", key, self.storagedict[key])
            self.delete(self.storagedict[key])
            self.move_to_front(self.storagedict[key])
            return self.storagedict[key].value
        else:
            return

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key not in self.storagedict.keys():
            if len(self) == self.limit:
                dropme = self.tail
                print("dropping ", dropme)
                self.storagedict = {k:v for k, v in self.storagedict.items() if v != dropme}
                self.remove_from_tail()
            node = ListNode(value)
            node.id = key
            print("setting ", node.id)
        else:
            print(key, "already in storage")
            node = self.storagedict[key]
        self.move_to_front(node)
        self.storagedict[key] = node

cache = LRUCache(3)
cache.set('item1', 'a')
cache.set('item2', 'b')
cache.set('item3', 'c')
print(len(cache))
cache.get('item1')
print(len(cache))
