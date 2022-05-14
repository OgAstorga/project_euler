word_bank = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}

def spell(x):
    thousand = x // 1000
    x -= thousand * 1000
    thousand_str = None
    if thousand >= 1:
        thousand_str = f"{word_bank[thousand]} thousand"

    hundred = x // 100
    x -= hundred * 100
    hundred_str = None
    if hundred >= 1:
        hundred_str = f"{word_bank[hundred]} hundred"

    units_str = None
    if 1 <= x <= 19:
        units_str = word_bank[x]
    elif 20 <= x:
        teens = x // 10
        units = x % 10
        if units == 0:
            units_str = word_bank[teens * 10]
        else:
            units_str = f"{word_bank[teens * 10]}-{word_bank[units]}"

    sentence = ""
    if thousand_str is not None:
        if not hundred_str and not units_str:
            sentence += thousand_str
        else:
            sentence += f"{thousand_str}, "

    if hundred_str is not None:
        if not units_str:
            sentence += hundred_str
        else:
            sentence += f"{hundred_str} and "

    if units_str is not None:
        sentence += units_str
    
    return sentence

def count_letters(sentence):
    count = 0
    for c in sentence:
        if ord('a') <= ord(c) <= ord('z'):
            count += 1
    return count

if __name__ == "__main__":
    ans = 0
    for i in range(1, 1001):
        ans += count_letters(spell(i))
    print(ans)
