# LRU [Least Recently Used] Cache Implementation

# Interfaces exposed
# get(k)
# put(k, v)
# delete(k)

# Cache(5): capacity
# put(1, 'a')  container: [{1: 'a'}, ]
# put(2, 'b')  container: [{1: 'a'}, {2: 'b'}]
# put(3, 'c')  container: [{1: 'a'}, {2: 'b'}, {3: 'c'}]
# put(4, 'd')  container: [{1: 'a'}, {2: 'b'}, {3: 'c'}, {4: 'd'}]
# put(5, 'e')  container: [{1: 'a'}, {2: 'b'}, {3: 'c'}, {4: 'd'}]

# put(6, 'f')  container: [{2: 'b'}, {3: 'c'}, {4: 'd'}, {6: 'f'}]
# note: {1: 'a'} is evicted as it was the oldest/least accessed item

# get(3): c     container: [{2: 'b'}, {4: 'd'}, {6: 'f'}, {3: 'c'}]
# note: as 3 is accessed recently its chances of eviction is least


class CacheStore:
    def __init__(self, capacity) -> None:
        super().__init__()
        self.capacity = capacity
