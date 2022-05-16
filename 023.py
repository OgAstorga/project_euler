# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot
# be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def sum_divisors(n):
    sumd = 1
    div = 2
    while div*div <= n:
        if n % div == 0:
            sumd += div
            if div * div != n:
                sumd += n // div
        div += 1
    return sumd

if __name__ == "__main__":
    abundant = set()
    for i in range(1, 28124):
        if sum_divisors(i) > i:
            abundant.add(i)

    ans = 0
    for i in range(1, 28124):
        sum2 = False
        for j in abundant:
            if j + 12 > i:
                break

            if (i - j) in abundant:
                sum2 = True
                break
        if not sum2:
            ans += i
    print(ans)
