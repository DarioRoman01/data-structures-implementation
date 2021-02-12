"""Hash table implementation."""

class HashTable:
    def __init__(self):
        """Constructor."""
        self.MAX = 3
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


if __name__ == "__main__":
    """Testing implementation."""
    t = HashTable()
    t["march 6"] = 130
    t["march 17"] = 204
    t["march 24"] = 210
    t["march 30"] = 207
    print(t.arr[0])
    