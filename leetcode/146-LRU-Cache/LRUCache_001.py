class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.tb = {}
        self.capacity = capacity
        self.freq = {}
        self.tm = 0

    # @return an integer
    def get(self, key):
        if key in self.tb:
            self.freq[key] = self.tm
            self.tm += 1
            return self.tb[key]
        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):

        if len(self.tb) == self.capacity and key not in self.tb:
            minkey = min(self.freq, key=self.freq.get)
            del self.tb[minkey]
            del self.freq[minkey]

        self.freq[key] = self.tm
        self.tb[key] = value
        self.tm += 1
