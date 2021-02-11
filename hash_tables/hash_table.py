"""Hash table implementation."""

class HashTable:
    def __init__(self):
        """Constructor."""
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]


    def get_hash(self, key):
        """Generate hash using ascii numbers."""
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        """Get the element by key."""
        h = self.get_hash(key)
        return self.arr[h]
        
    def __delitem__(self, key):
        """Delete element by key."""
        h = self.get_hash(key)
        self.arr[h] = None

if __name__ == "__main__":
    """Testing implementation."""
    t = HashTable()
    t['march 6'] = 130
    t['december 24'] = 235
    t['march 19'] = 190
    t['july 9'] = 209
    t['february 16'] = 938

    print(t['february 16'])
    print(t['march 19'])
    print(t['march 6'])
    del t['march 6']
    print(t['march 6'])