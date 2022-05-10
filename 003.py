# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

if __name__ == "__main__":
  composite = 600851475143
  it = 2

  print(f"{composite} = ", end="")

  while it*it < composite:
      while composite % it == 0:
          composite //= it
          print(it, end=" x ")
      it += 1

  print(composite)
