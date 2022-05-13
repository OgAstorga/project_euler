# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Which starting number, under one million, produces the longest chain?

mem = {}
def chain_length(n):
    if n == 1:
        return 1

    if n in mem:
        return mem[n]

    if n % 2 == 0:
        ans = 1 + chain_length(n // 2)
    else:
        ans = 1 + chain_length(3 * n + 1)

    mem[n] = ans
    return ans

if __name__ == "__main__":
    ans = 1
    for i in range(1, 1000001):
        if chain_length(ans) < chain_length(i):
            ans = i
    print(ans)
