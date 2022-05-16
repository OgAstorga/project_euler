# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

if __name__ == "__main__":
    ix, a, b, c = (2, 1, 1, 0)
    while True:
        c = b
        b = a
        a = b + c
        ix += 1
        if len(str(a)) >= 1000:
            break
    print(ix)
