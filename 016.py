# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

if __name__ == "__main__":
    pow2100 = str(2 ** 1000)
    ans = 0
    for d in pow2100:
        ans += int(d)
    print(ans)