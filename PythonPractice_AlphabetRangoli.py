import string
n = 10
l = []
alpha = string.ascii_lowercase
for i in range(n):
    s = "-".join(alpha[i:n])
    l.append((s[::-1]+s[1:]).center(4*n-3, "-"))
print("\n".join(l[:0:-1]+l))







# n = 5
# s = list(string.ascii_lowercase)
# k = n


# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(s[k-2+j],end="")
#     k = k - 1
#     print("\r")
#
# for i in range(1,n):
#     for j in range(i,n):
#         print(s[j], end="")
#     print("\r")
#
# for i in range(1,n+1):
#     p = 1
#     for j in range(i,n+1):
#         print(" ", end="")
#     for m in range(j-i+2,n+1):
#         print(s[j-p], end="")
#         p = p + 1
#     print("\r")






# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end="")
#     print("\r")
# for i in range(1, n+1):
#     for j in range(i, n):
#         print(j, end="")
#     print("\r")
# for i in range(1, n):
#     for j in range(i, n+1):
#         if j != n:
#             print(" ", end="")
#         else:
#             print(i+1, end="")
#     print("\r")
