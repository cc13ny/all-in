#include<stdio.h>
#include<math.h>

int power(int b, int p){
    int k;
    int result = 1;
    
    for(k = 0; k < p; k++){
          result *= b;
    }
    
    return result;
}

int main(int argc, char *argv[]){
    
    int num;
    int frac  = 1;
    int digit = 1;
    
    printf("Enter a number: ");
    scanf("%d", &num);
    
    while(1){
            frac = num/power(10,digit);
            if(frac == 0) break;
            digit += 1;
            
    }
    printf("the digit is: %d\n\n", digit);
    
    int j;
    int n1 = 0;
    for(j = 0; j< digit; j++){
          int base = power(10, j + 1);
          printf("The base is: %d\n", base);
          int fra = num/base;
          printf("The fra is: %d\n", fra);
          int mod = fmod( num, base);
          printf("The mod is: %d\n", mod);
          int quan = power(10,j);
          printf("The quan is: %d\n", quan);
          n1 += fra * quan;
          if(mod >  2 * quan - 1){
               n1 += quan;
               printf("A\n");
                 
          }
          
          if( 2 * quan > mod > quan - 1 ){
               n1 += mod - quan + 1; 
               printf("B\n"); 
               
          }
          printf("The n1 is: %d\n\n",n1);
          
    }
    
    printf("The number of ones is: %d\n", n1);
    
    getchar();
    getchar();
    return 0;

} 
