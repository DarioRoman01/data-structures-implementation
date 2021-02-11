class MyArray:
    
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        """Get  element by index."""
        return self.data[index]

    def push(self, item):
        """inserts element at last position"""
        self.data[self.length] = item
        self.length += 1
        return self.data


    def pop(self):
        """delete element at last position"""
        lasitem = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return lasitem

    
    def remove(self, index):
        """Delete item by index."""
        item = self.data[index]
        self.shift_index(index)
        return item


    def shift(self):
        """deletes fist element and returns it"""
        first_item = self.data[0]
        self.shift_index(0)
        return first_item


    def unshift(self, item):
        """inserts element at first position"""
        self.unshift_index()
        self.data[0] =  item
        return self.data



    # Utilitie functions:
    
    def unshift_index(self):
        """moves items to next index."""
        i = self.length

        while i > 0:
            for e in range(i):
                self.data[i] = self.data[i - 1]
                i -= 1
        
        self.length += 1


    def shift_index(self, index):
        """moves items to previous index."""
        i = index
        while i < self.length - 1:
            for i in range(self.length - 1):
                self.data[i] = self.data[i + 1]
                i += 1

        del self.data[self.length - 1]
        self.length -= 1


if __name__ == "__main__":
    
    array = MyArray()
    array.push('jose')
    array.push('adriana')
    array.push('dario')
    array.push('diego')
    
    print(array.data)
    # should return all names

    print(array.get(2))
    # should return dario

    array.pop()
    # should delete diego

    array.remove(0)
    # should delete jose

    array.unshift('wily')
    # Should add willy in the first position of the array

    print(array.data)
    # should return only dario, adriana & willy

    array.shift()
    # Should delete willy

    print(array.data)
    # Should return only adriana and dario