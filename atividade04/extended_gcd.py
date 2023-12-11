# recursão para calcular o GCD estendido
def extended_gcd(x, n):
  if n == 0:
    return x, 1, 0
  else:
    gcd, i, j = extended_gcd(n, x % n)
    return gcd, j, i - (x // n) * j

#  inverso modular usando o GCD estendido
def mod_inverse(x, n):
  gcd, i, _ = extended_gcd(x, n)
  if gcd == 1:
    return gcd, i % n
  else:
    return gcd, 'N'

# entrada
x, n = map(int, input().split())

# saida
gcd, inv = mod_inverse(x, n)
print(gcd, inv)