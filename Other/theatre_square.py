import math
n, m, a = map(float, raw_input().split())

print int( math.ceil(n/a) * math.ceil(m/a) )
