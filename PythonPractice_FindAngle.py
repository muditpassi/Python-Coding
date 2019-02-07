# from math import acos, degrees
import math
ab = 1
bc = 10
# # ac = (ab**2 + bc**2)**(1/2)
# # am = ac/2
# # bm = (ab**2 + am**2)**(1/2)
# # print(round(degrees(acos((bm**2 + am**2 - bc**2)/(2 * bm * am)))))
# ac = math.hypot(ab, bc)
# mc = ac/2
# bm = math.sqrt((bc**2 - mc**2))
print(round(math.degrees(math.atan2(ab, bc))))
