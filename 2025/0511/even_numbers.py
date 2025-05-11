# -*- encoding: utf-8 -*-

class EvenNumbers:
    def __iter__(self):
        self.n = 2 # Start from the first even number
        return self

    def __next__(self):
        x = self.n
        self.n += 2 # Increment by 2 to get the next even number
        return x

# Create an instance of EvenNUbmers
event = EvenNumbers()
it = iter(event)

# Print the first fiven even numbers
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
