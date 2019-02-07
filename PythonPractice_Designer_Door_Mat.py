n = 40
m = n * 3
li = []
s1 = ''.join("WELCOME").center(m, '-')

for i in range(1, n//2 + 1):
    s = []
    s = ''.join((".|.")*(2 * i - 1)).center(m, '-')
    li.append(s)
print('\n'.join(li[:] + ["WELCOME".center(m, '-')] + li[::-1]))
