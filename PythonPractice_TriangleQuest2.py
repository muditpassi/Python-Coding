# CORRECT SOLUTION

# n = 5
# num = [j for j in range(1, n+1)]
# num = ''.join(str(e) for e in num)
# li = []
# for i in range(n):
#     s = ''.join(num[:i+1])
#     li.append(s[:i]+s[::-1])
# print('\n'.join(li))

# ALTERNATIVE SOLUTION

for i in range(1, 10):
    print(pow(((pow(10, i) - 1) // 9), 2))
