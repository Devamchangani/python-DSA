from xml.dom.minidom import Element
'''

def get_hash(key):
    sum = 0
    for c in key:
        sum += ord(c)
    print(sum % 100)

get_hash('march 6')

# ==================================  ==============================

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None]*self.MAX 

    def get_hash(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

h = HashTable()
h['march 6'] = 302
h['march 7'] = 303
h['march 8'] = 304
h['march 9'] = 305

print(h['march 7'])

del h['march 7']
print(h['march 7'])
'''
# ==========================================================================================


class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)] 

    def get_hash(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found  = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True

        if not found:
            self.arr[h] .append((key, val))
        

    def __getitem__(self, key):
        h = self.get_hash(key)
        for kv in self.arr[h]:
            if kv[0] == key:
                return kv[1]


    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, kv in enumerate(self.arr[h]):
            if kv[0] == key:
                print(f"Delete elementindex in : {index}")
                del self.arr[h][index]
        

t = HashTable()
print(t.get_hash('march 6'))
print(t.get_hash('march 17'))


t['march 6'] = 123
t['march 9'] = 163
t['march 45'] = 523
t['march 17'] = 923

print(t['march 6'])
print(t['march 17'])
print(t.arr)

t['march 17'] = 999
print(t.arr)

del t['march 17']

print(t.arr)