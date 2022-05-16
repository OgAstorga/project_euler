# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

def factorial(x):
    ans = 1
    for i in range(1, x+1):
        ans *= i
    return ans

def nth_perm(index, elements):
    if len(elements) == 0:
        return ""

    subperm = factorial(len(elements) - 1)
    item_ix = index // subperm
    sorted_els = list(elements)
    sorted_els.sort()
    item = sorted_els[item_ix]
    elements.remove(item)
    return item + nth_perm(index - item_ix * subperm, elements)

if __name__ == "__main__":
    print(nth_perm(999999, {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}))
