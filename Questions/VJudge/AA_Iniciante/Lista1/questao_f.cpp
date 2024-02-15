#include <stdio.h>

int main()
{
    int t = 0, n = 0, q = 0;
    scanf("%i", &t);
    long degraus[n];
    long testes[q-1];
    
    long soma = 0, p1 = 0, p2 = 0;
    for(int i = 0; i < t; i++){
        scanf("%i %i", &n, &q);
        
        for(int j = 0; j < n; j++){
            scanf("%i", &degraus[j]);
        }
        for(int j = 0; j < n; j++){
            scanf("%i", &testes[j]);
        }
        
        for(int j = 0; j < n; j++){
            printf("%i ", degraus[j]);
        }
        printf("\n");
        for(int j = 0; j < q; j++){
            printf("%i ", testes[j]);
        }
        printf("\n");

        while (p2 < q){
            if(p2 != 0 && testes[p2-1] > testes[p2]){
                p1 = 0;
                soma = 0;
            }
            while(degraus[p1] <= testes[p2]){
                soma += degraus[p1];

                if (p1 < n-1){
                    p1 ++;
                }else{
                    break;
                }
            }
            printf("%i ", soma);
            p2 ++;
        }
        printf("\n");

        
    }
    return 0;
}
