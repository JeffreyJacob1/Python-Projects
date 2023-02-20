class Hashtable:
    def __init__(self):
        self.size = 0
        self.dic = {}

    def add(self, key, value):
        self.dic[key] = value
        self.size += 1
    
    def get(self, key):
        return self.dic[key]
    
    def get_size(self):
        return self.size
    
    def remove(self, value):
        # if value is equal to data remove it
        for k, v in self.dic.items():
            if v == value:
                del self.dic[k]
                self.size -= 1
                return

    def is_empty(self):
        return self.size == 0

# driver code
h = Hashtable()
data = ['goat', 'pig', 'chicken', 'dog', 'lion', 'tiger', 'cow', 'cat']

for i in range(len(data)):
    h.add(data[i], i)

for key in data:
    print(h.get(key))

n = h.get_size()

for i in range(n):
    h.remove(i)

print(h.is_empty())
