/* 
• typedef struct { int x, y; } Point;: Define uma estrutura chamada Point para representar pontos na curva elíptica.

• int extended_gcd(int x, int n, int *i, int *j): Função para calcular o GCD estendido.

• int mod_inverse(int x, int n): Função para calcular o inverso modular.

• Point ecc_add(Point P, Point Q, int a, int p): Função para adição de pontos na curva elíptica.

• Point ecc_multiply(Point G, int n, int a, int p): Função para multiplicação de ponto por escalar.

• int main(): Função principal.

• O loop while (1) lê os casos de teste até que n seja igual a zero.

• Point result = ecc_multiply((Point){Xg, Yg}, n, a, p);: Chama a função ecc_multiply para obter o resultado.

• printf("%d %d\n", result.x, result.y);: Imprime as coordenadas do ponto resultante. */



#include <stdio.h>

typedef struct {
  int x, y;
} Point;

int extended_gcd(int x, int n, int *i, int *j) {
  if (n == 0) {
    *i = 1;
    *j = 0;
    return x;
  }
  else {
    int gcd = extended_gcd(n, x % n, i, j);
    int temp = *i;
    *i = *j;
    *j = temp - (x / n) * (*j);
    return gcd;
  }
}

int mod_inverse(int x, int n) {
  int i, j;
  int gcd = extended_gcd(x, n, &i, &j);
  if (gcd == 1)
    return (i % n + n) % n;
  else
    return -1; // O inverso multiplicativo não existe
}

Point ecc_add(Point P, Point Q, int a, int p) {
  Point R;
  if (P.x == 0 && P.y == 0)
    return Q;
  else if (Q.x == 0 && Q.y == 0)
    return P;
  else if (P.x == Q.x && P.y != Q.y) {
    R.x = 0;
    R.y = 0;
    return R;
  }
  else {
    int lam;
    if (P.x != Q.x)
      lam = ((Q.y - P.y) * mod_inverse(Q.x - P.x, p)) % p;
    else if (P.y != 0)
      lam = ((3 * P.x * P.x + a) * mod_inverse(2 * P.y, p)) % p;
    else {
      R.x = 0;
      R.y = 0;
      return R;
    }

    R.x = (lam * lam - P.x - Q.x) % p;
    R.y = (lam * (P.x - R.x) - P.y) % p;

    return R;
  }
}

Point ecc_multiply(Point G, int n, int a, int p) {
  Point R = {0, 0};
  for (int i = 0; i < sizeof(int) * 8; i++) {
    if ((n & 1) == 1)
      R = ecc_add(R, G, a, p);
    G = ecc_add(G, G, a, p);
    n >>= 1;
  }
  return R;
}

int main() {
  int n, a, p, Xg, Yg;
  while (1) {
    scanf("%d", &n);
    if (n == 0)
      break;
    scanf("%d %d %d %d", &a, &p, &Xg, &Yg);

    Point result = ecc_multiply((Point){Xg, Yg}, n, a, p);

    printf("%d %d\n", result.x, result.y);
  }

  return 0;
}
