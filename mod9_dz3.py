class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end or self.start % 2 != 0:
            raise StopIteration
        else:
            result = self.start
            self.start += 2
            return result

en = EvenNumbers(10, 25)
for i in en:
    print(i)