#include<stdio.h>

/*Calculate the power*/
int power(int b, int p){
    int k, result;
    for(k = 0, result = 1; k < p; k++) result *= b;
    return result;   
}

int main(int argc, char *argv[]){
    /* Input the number */
    int num;
    
    printf("Enter a number: ");
    scanf("%d", &num);
    
    /* Calculate the number of 1's */
    int j = 0, n0, n1 = 0;
    int base, fra = 1, mod, quan;
    
    while(fra != 0){
          base = power(10, j + 1);
          printf("The base is: %d\n", base);
          fra = num/base;
          printf("The fra is: %d\n", fra);
          mod = num - base * fra;
          printf("The mod is: %d\n", mod);
          quan = power(10,j);
          printf("The quan is: %d\n", quan);
          n0 = n1;
          n1 += fra * quan;
          if(mod >  2 * quan - 1){
               n1 += quan;
               printf("A: %d\n", quan);
          }
          else if( mod > quan - 1 ){
               n1 += mod - quan + 1; 
               printf("B: %d\n", mod - quan + 1); 
          }
          printf("The diff is: %d\n", n1 - n0);
          printf("The n1 is: %d\n\n",n1);
          j++;
    }
    
    printf("The number of ones is: %d\n", n1);

    getchar();
    getchar();
    return 0;
} 
