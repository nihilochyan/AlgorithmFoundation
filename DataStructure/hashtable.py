#  the dictionary structure is same with hash table in python
class hashtable:

    __slots__ = ['table']

    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value
        pass

    def delete(self, key):
        del self.table[key]
        pass

    def search(self, key):
        return self.table[key]