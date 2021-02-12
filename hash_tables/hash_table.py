"""Hash table implementation."""

class HashTable:
    def __init__(self):
        """Constructor."""
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]


    def get_hash(self, key):
        """Generate hash using ascii numbers."""
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX


    def __setitem__(self, key, value):
        """Add item to the table."""
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx] = (key, value)
                found = True
                break

        if not found:
            self.arr[h].append((key, value))


    def __getitem__(self, key):
        """Get the element by key."""
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
        
    def __delitem__(self, key):
        """Delete element by key."""
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
            else:
                return 'The key does not exists'

    def values(self):
        """Return a list of all the values of the table."""
        values = []
        for element in self.arr:
            for value in element:
                values.append(value[1])
        
        return values


    def keys(self):
        """Return a list of all the keys of the table."""
        keys = []
        for element in self.arr:
            for value in element:
                keys.append(value[0])

        return keys

    def items(self):
        """Return a list containing a tuple for each key value pair."""
        items = []
        for element in self.arr:
            for value in element:
                if len(element) == 0:
                    pass
                else:
                    items.append(value)
                    break

        return items

    def from_keys(self, key):
        """Return a dictionary with the specified key and value."""
        ht = {}
        h = self.get_hash(key)
        for element in self.arr:
            for value in element:
                if value[0] == key:
                    ht[key] = value[1]
                    break
        return ht

    def get(self, key):
        """Returns the value of the specified key."""
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
            else:
                return 'The key does not exists'
        

    def pop(self, key):
        """Remove element with the specified keys."""
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
            else:
                return 'The key does not exists'