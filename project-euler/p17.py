l1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
l2 = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


bre = True # use 'and'
low = 1
high = 1000


def in_words(n):
    if 0 <= n <= 19:
        return l1[n]
    if 20 <= n <= 99:
        return f"{l2[n // 10]}{'-' + l1[n % 10] if n % 10 else ''}"
    if 100 <= n <= 999:
        b = " and " if bre else ' '
        return f"{l1[n // 100]} hundred{((b + in_words(n % 100)) if
                n % 100 else '')}"
    if n == 1000:
        return "one thousand"
    else:
        raise ValueError


count = 0
for n in range(low, high + 1):
    word = in_words(n)
    count += len(word.replace(" ", "").replace("-", ""))

print(count)
