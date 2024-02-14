#include <iostream>
#include <stdio.h>

int main()
{
  int n = 0, k = 0, q = 0;
  scanf("%i %i %i", &n, &k, &q);
  int base[200002] = {0};

  for (int i = 0; i < n; i++)
  {
    int v_min = 0, v_max = 0;
    scanf("%i %i", &v_min, &v_max);
    base[v_min] += 1;
    base[v_max + 1] -= 1;
  }

  int somador = 0;
  for (int i = 0; i < 200002; i++)
  {
    somador += base[i];
    base[i] = (somador >= k) ? 1 : 0;
    base[i] += base[i - 1];
  }

  int count = 0;
  for (int i = 0; i < q; i++)
  {
    int q_min = 0, q_max = 0;
    scanf("%i %i", &q_min, &q_max);
    count = base[q_max] - base[q_min - 1];

    printf("%i\n", count);
  }
  return 0;
}
