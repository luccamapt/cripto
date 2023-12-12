def extended_gcd(x, n):
  if n == 0:
    return x, 1, 0
  else:
    gcd, i, j = extended_gcd(n, x % n)
    return gcd, j, i - (x // n) * j

def mod_inverse(x, n):
  gcd, i, _ = extended_gcd(x, n)
  if gcd == 1:
    return i % n
  else:
    raise ValueError("O inverso multiplicativo não existe")

def rsa_decrypt(N, E, C):
  phi_n = (N - 1)
  d = mod_inverse(E, phi_n)
  M = pow(C, d, N)
  return M

# entrada
N, E, C = map(int, input().split())

# quebra da criptografia RSA
M = rsa_decrypt(N, E, C)

# saida
print(M)
