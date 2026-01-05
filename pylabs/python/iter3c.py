class CountUp:
    def __init__(self, max):
        self.max = max
        self.current = 1
 
    def __iter__(self):
        return self
 
    def __next__(self):
 
        if self.current > self.max:
            raise StopIteration
        val = self.current
        self.current += 1
        return val
 
for num in CountUp(5):
    print(num)