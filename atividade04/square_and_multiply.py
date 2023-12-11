def square_and_multiply(x, k, n):
  # exponenciação modular usando Quadrado-e-Multiplicação
  result = 1
  x = x % n
  while k > 0:
    if k % 2 == 1:
      result = (result * x) % n
    k = k // 2
    x = (x * x) % n
  return result

# entrada
x, k, n = map(int, input().split())

# saida
result = square_and_multiply(x, k, n)
print(result)
