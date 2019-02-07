import string
n = 10
l = []
alpha = string.ascii_lowercase
for i in range(n):
    s = "-".join(alpha[i:n])
    l.append((s[::-1]+s[1:]).center(4*n-3, "-"))
print("\n".join(l[:0:-1]+l))

