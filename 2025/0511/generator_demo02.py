def gen_666(meet_yield):
    print("Hello")
    if meet_yield:
        print("yield!")
        yield 666
        print("back!")
    print("Bye~")
    return "over"

if __name__ == "__main__":
    g2 = gen_666(True)
    x2 = next(g2)
    print("x2:", x2)
    x3 = next(g2)
    print("x3:", x3)
