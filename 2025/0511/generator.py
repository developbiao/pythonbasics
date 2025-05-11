def my_generator(n):
    # initilize conter
    value = 0

    # loop unitl conter is less than n
    while value < n:
        # produce the current value of the counter
        yield value

        # increment the counter
        value += 1


if __name__ == "__main__":
    for value in my_generator(3):
        # print each value produced by generator
        print(value)
