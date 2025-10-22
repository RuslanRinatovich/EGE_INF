from math import ceil, log2

lk = ceil((12 * 6) / 8)
np = ceil(log2(1000) / 8)
dp = 60
print(lk + np + dp)
