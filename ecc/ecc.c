/* 
INTRODUÇÃO A CRIPTOGRAFIA

     .--------.
    / .------. \
   / /        \ \
   | |        | |
  _| |________| |_
.' |_|        |_| '.
'._____ ____ _____.'
|     .'____'.     |
'.__.'.'    '.'.__.'
'.__  |  ECC |  __.'
|   '.'.____.'.'   |
'.____'.____.'____.'
'.________________.'


Guilherme Milani de Oliveira - 771016
Lucca Marques Almeida Paes Teles - 771034



SOBRE O PROGRAMA

• typedef struct { int x, y; } Point;: Define uma estrutura chamada Point para representar pontos na curva elíptica.

• int extended_gcd(int x, int n, int *i, int *j): Função para calcular o GCD estendido.

• int mod_inverse(int x, int n): Função para calcular o inverso modular.

• Point ecc_add(Point P, Point Q, int a, int p): Função para adição de pontos na curva elíptica.

• Point ecc_multiply(Point G, int n, int a, int p): Função para multiplicação de ponto por escalar.

• int main(): Função principal.

  • O loop while (1) lê os casos de teste até que n seja igual a zero.

  • Point result = ecc_multiply((Point){Xg, Yg}, n, a, p);: Chama a função ecc_multiply para obter o resultado.

  • printf("%d %d\n", result.x, result.y);: Imprime as coordenadas do ponto resultante. 
  */


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
  if (x < 0)
    x = x + n;
  int i, j;
  int gcd = extended_gcd(x, n, &i, &j);
  if (gcd == 1)
    return (i % n + n) % n;
  else
    return -1; // O inverso multiplicativo não existe
}

Point ecc_add(Point G, Point Q, int a, int p) {
  Point R;
  if (Q.x == 0 && Q.y == 0)
    return G;
  else if (G.x == 0 && G.y == 0)
    return Q;
  else if (Q.x == G.x && Q.y != G.y) {
    R.x = 0;
    R.y = 0;
    return R;
  }
  else {
    int lam;
    if (Q.x != G.x || Q.y != G.y)
      lam = ((G.y - Q.y) * mod_inverse(G.x - Q.x, p)) % p;
    else if (Q.y != 0)
      lam = ((3 * Q.x * Q.x + a) * mod_inverse(2 * Q.y, p)) % p;

    R.x = (lam * lam - Q.x - G.x) % p;
    R.y = (lam * (Q.x - R.x) - Q.y) % p;

    if (R.x <  0)
      R.x = p + R.x;

    if (R.y <  0)
      R.y = p + R.y;

    return R;
  }
}

Point ecc_multiply(Point G, int n, int a, int p) {
  Point R = {0, 0};
  for (int i = 0; i < sizeof(int) * 8; i++) {
    if (n & 1)
      R = ecc_add(G, R, a, p);
    G = ecc_add(G, G, a, p);
    n >>= 1;
    printf ("LOOP %d  R - %d %d\n", i, R.x, R.y);
    printf ("LOOP %d  G - %d %d\n", i, G.x, G.y);
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

    printf("FINAL %d %d\n", result.x, result.y);
  }

  return 0;
}
