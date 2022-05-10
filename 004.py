# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_6d_palindrome(x):
    if not (100000 <= x <= 999999):
        return False

    digits = []
    while x > 0:
        digits.append(x%10)
        x //= 10

    return digits[0] == digits[5] and \
           digits[1] == digits[4] and \
           digits[2] == digits[3]

if __name__ == "__main__":
  ans = 0
  for i in range(100, 1000):
      for j in range(i, 1000):
          if is_6d_palindrome(i*j):
              ans = max(ans, i*j)

  print(ans)
