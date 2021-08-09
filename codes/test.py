import re
def func(s, t):
    match = re.search(t, s)
    if match:
        return ('%d,%d' % (match.start(), match.end()))
    else:
        return None

s = 'I am Julia'
t = 'rushdi'
print(func(s, t))
