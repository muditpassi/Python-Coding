number = 36
w = len(str(bin(number)).replace('0b', ''))
for i in range(1, number + 1):
    d = str(i)
    o = str(oct(i)).replace('0o', '')
    h = str(hex(i)).replace('0x', '').upper()
    b = str(bin(i)).replace('0b', '')
    print(d.rjust(w), o.rjust(w), h.rjust(w), b.rjust(w), sep=' ')
