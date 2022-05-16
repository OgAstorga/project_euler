# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# Evaluate the sum of all the amicable numbers under 10000.

def sum_divisors(n):
    sumd = 1
    div = 1
    while div*div <= n:
        div += 1
        if n % div == 0:
            sumd += div
            sumd += n // div
    return sumd

if __name__ == "__main__":
    divsums = {}
    for i in range(1, 10001):
        divsums[i] = sum_divisors(i)

    ans = 0
    for i in range(1, 10001):
        if divsums[i] in divsums and i != divsums[i] and divsums[divsums[i]] == i:
            print(i, divsums[i])
            ans += i
    print(ans)
