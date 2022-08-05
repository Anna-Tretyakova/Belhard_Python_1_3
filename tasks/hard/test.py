
class Counter:
    value: int

    def __init__(self, value = 0):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        value = self.value
        if self.value > 100:
            raise StopIteration
        self.value +=1
        return value

    def increase(num=1):
        self.value += num

    def decrease(num=1):
        self.value -= num

my_counter = Counter(10)
    for item in my_counter:
    print item













