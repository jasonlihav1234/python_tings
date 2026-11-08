"""
- iterable = something that can looped over, iterable if it implements __iter__() method
- __iter__() returns an iterator

- iterator = object that produces the next value ina sequence when asked, remembers position in sequence
- implements __next__(), when there are no more elements, __next__() raises StopIteration exception
"""

class CountTo:
    def __init__(self, max_value):
        self.max = max_value
    def __iter__(self):
        return CountToIterator(self.max)

class CountToIterator:
    def __init__(self, max_value):
        self.max = max_value
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration

counter = CountTo(5)

for count in counter:
    for count2 in counter:
        print(count, count2)
