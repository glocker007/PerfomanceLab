from math import gcd
n, m= map(int, input().split())
num = gcd(m - 1, n)
if (m == 1):
     print(1)
else:
     k = n//num # k * (m-1) = 0 mod n
     def mod(k, n):
          if (k%n == 0):
               return n
          else:
               return k%n
     result = ''.join([str(mod((1 + i*(m-1)), n)) for i in range(k) ])
     print(result)