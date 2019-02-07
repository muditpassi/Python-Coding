s = "banana"
s = s.upper()
l1 = []
l2 = []

# -----------------CORRECT SOLUTION BUT FAILS FEW TESTCASES---------------------------
# for i in range(len(s)):
#     if s[i] in ('A', 'E', 'I', 'O', 'U'):
#         for j in range(i, len(s)):
#             s1 = ''.join(s[i:j+1])
#             l1.append(s1)
#     else:
#         for j in range(i, len(s)):
#             s1 = ''.join(s[i:j+1])
#             l2.append(s1)
# if len(l2) > len(l1):
#     print("Stuart ", len(l2))
# elif len(l1) > len(l2):
#     print("Kevin ", len(l1))
# else:
#     print("Draw")
# ------------------------------------------------------------------------------------

for i in range(len(s)):
    if s[i] in ('A', 'E', 'I', 'O', 'U'):
        for j in range(i, len(s)):
            s1 = ''.join(s[i:j+1])
            l1.append(s1)
    else:
        for j in range(i, len(s)):
            s1 = ''.join(s[i:j+1])
            l2.append(s1)

Stuart = {}
Kevin = {}
count1 = 0
count2 = 0

for item in l2:
    if item in Stuart:
        Stuart[item] += 1
    else:
        Stuart[item] = 1

for word, val in Stuart.items():
    count2 += val

for item in l1:
    if item in Kevin:
        Kevin[item] += 1
    else:
        Kevin[item] = 1

for word, val in Kevin.items():
    count1 += val

if count1 > count2:
    print("Kevin", count1)
elif count2 > count1:
    print("Stuart", count2)
else:
    print("Draw")
