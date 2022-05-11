# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

from math import sqrt, ceil

def is_prime(n):
  it = 2
  while it*it <= n:
    while n % it == 0:
      n //= it
      return False
    it += 1

  return True

if __name__ == "__main__":
  # 3 is the 2nd prime.
  candidate = 3
  count = 2

  while True:
    candidate += 2
    count += is_prime(candidate)
    if count == 10001:
      break

  print(candidate)
