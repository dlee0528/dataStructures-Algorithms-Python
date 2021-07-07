class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    # hash function that uses MOD
    # sum all characters and divide the sum by 100, where 100 is the size of the array
    def get_hash(key):
        h=0
        for char in key:
            h += ord(char) # returns an integer representing the Unicode character
        return h % self.MAX

    def add(self, key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    def get(self,key):
        h = self.get_hash(key)
        return self.arr[h]

    # Using Python operator__ 
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False

        # Collision Handling - Chaining method
        for index, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][index] = (key,val)
                found = True
                break

        if not found:
            self.arr[h].append((key,val))

    def __getitem__(self,key):
        h = self.get_hash(key)

        # For chaining method
        for element in enumerate(self.arr[h]):
            if element[0] == key:
                return element[1]


    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None

    

if __name__ == '__main__':
    t = HashTable()
    # t.add('march 6', 130)
    # t.get('march 6')
    t["march 6"] = 100
    t["march 6"] = 200
    t["march 8"] = 300 
    t["march 9"] = 400
    t["march 10"] = 500