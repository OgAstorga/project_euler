# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

if __name__ == "__main__":
    # This problem builds a pascal triangle, position 20x20 = (40 choose 20)
    # (40 choose 20) = 40! / 2 * 20! = (21 * ... * 40) / (1 * ... * 20)

    ans = 1
    for n in range(21, 41):
        ans *= n
    for n in range(1, 21):
        ans //= n

    print(ans)
