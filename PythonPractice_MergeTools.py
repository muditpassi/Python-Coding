s = "AABCAAADA"
k = 3

a = []
len_a = 0
for item in s:
    len_a += 1
    if item not in a:
        a.append(item)
    if len_a == k:
        print(''.join(a))
        a = []
        len_a = 0

# --------CORRECT SOLUTION BUT FAILS TESTCASES--------
# n = int(len(s)/k)
# s1 = [s[i:i+n] for i in range(0, len(s), n)]
# for item in s1:
#     a = []
#     for i in item:
#         if i not in a:
#             a.append(i)
#     print(''.join(str(e) for e in a))
# -----------------------------------------------------

