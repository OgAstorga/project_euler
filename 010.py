# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

length = 2000000
sieve = [True] * (length + 1)

for i in range(2, 1 + length//2):
  for j in range(2, 1 + length//i):
    sieve[i*j] = False

ans = 0
for i in range(2, length+1):
  if sieve[i]:
    ans += i

print(ans)
