import random

class RandomIterable:
    def __iter__(self):
        return self

    def __next__(self):
        if random.choice(["go", "go", "stop"]) == "stop":
            raise StopIteration # signals "the end"
        return 1


for eggs in RandomIterable():
    print(eggs)

