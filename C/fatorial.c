#include <stdio.h>

unsigned long long int i=1, ii=1, num, fat=1, somatorio;

int main (){

while(i <=  5){
    printf("Insira um n�mero: ");
    scanf("%ld", &num);

    ii = 1;
    fat = 1;

    while(ii <= num){
      fat = fat * ii;
      ii++;
    }

    printf("Fatorial: %llu\n",fat);

    somatorio = fat + somatorio;

    i++;

}
    printf("\nSomat�rio dos fatoriais: %llu\n\n", somatorio);
}
