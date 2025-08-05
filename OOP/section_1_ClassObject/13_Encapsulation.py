class Counter:
    def __init__(self):
        self.current = 0
    def increment(self):
        self.current += 1
    def value(self):
        return self.current
    def reset(self):
        self.current = 0

counter = Counter()
counter.increment()
counter.increment()
counter.current = -999

print(counter.value())