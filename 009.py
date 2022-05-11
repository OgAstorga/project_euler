# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Logic:
# a is a natural number
# b = (5*10^5 - a*10^3) / (a + 10^3)
# c = 1000 - a - b

a = 0
while True:
    a += 1
    if (500000 - a * 1000) % (a + 1000) == 0:
        b = (500000 - a * 1000) // (1000 + a)
        c = 1000 - a - b
        break

print(a*b*c)
