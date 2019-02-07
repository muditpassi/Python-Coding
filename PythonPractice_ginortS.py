import re

s = "Sorting1234"

s1 = re.findall(r'[a-z]', s)
s1 = ''.join(str(e) for e in s1)
s2 = re.findall(r'[A-Z]', s)
s2 = ''.join(str(e) for e in s2)
s3 = re.findall(r'\d', s)
s4 = []
s5 = []
main_s = []
final = ""
for i in s3:
    if int(i) % 2 != 0:
        s4.append(i)
    else:
        s5.append(i)
s4.sort()
s4 = ''.join(str(e) for e in s4)
s5.sort()
s5 = ''.join(str(e) for e in s5)
main_s.extend([s1, s2, s4, s5])
st = ''.join(str(e) for e in main_s)

print(st)
