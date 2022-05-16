# Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
# What is the total of all the name scores in the file?

import urllib.request

def get_names():
    req = urllib.request.Request('https://projecteuler.net/project/resources/p022_names.txt')
    content = ""
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('ascii')
    names = content.split(",")
    names = map(lambda name: name[1:-1], names)  # "javier" -> javier
    return list(names)

if __name__ == "__main__":
    names = get_names()
    names.sort()

    ans = 0
    for ix in range(len(names)):
        name_value = 0
        for c in names[ix]:
            name_value += ord(c) - ord('A') + 1
        ans += (ix + 1) * name_value
    print(ans)
