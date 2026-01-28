class MyRange:
    ''' Iterator using class '''
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration

def my_range(n):
    ''' Iterator using generator function '''
    current = 0
    while current < n:
        yield current
        current += 1

for num in my_range(5):
    print(num)  