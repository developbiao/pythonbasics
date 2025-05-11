def gen_666(meet_yield):
    print("Hello")
    if meet_yield:
        print("yield!")
        yield 666
        print("back!")
    print("Bye~")
    return "over"

if __name__ == "__main__":
    g1 = gen_666(False)
    x1 = next(g1)
