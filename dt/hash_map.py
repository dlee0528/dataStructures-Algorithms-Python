class HashTable:
    def __init__(self) -> None:
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    # hash function that uses MOD
    # sum all characters and divide the sum by 100, where 100 is the size of the array
    def get_hash(key):
        h=0
        for char in key:
            h += ord(char) # returns an integer representing the Unicode character
        return h % 100

    def add(self, key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    def get(self,key):
        h = self.get_hash(key)
        return self.arr[h]

    # Python operator__ 
    def __setItem__(self, key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getItem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]

    def __deliItem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None

    

if __name__ == '__main__':
    t = HashTable()
    t.add('march 6', 130)
    t.get('march 6')
    t['march 7'] = 200
    t['dec 7'] = 123
    t['march 7']
    t['dec 7']
