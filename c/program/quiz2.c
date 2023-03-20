#include <stdio.h>
#include "libcheckprime.h"

void main(){
  int number;
  while (1){
    printf("Type a number. : " );
    scanf("%d", &number);
    if (number == 0)
      return;
    else{
      if (isprime(number) == 1)
        printf("%d is a PRIME NUMBER.\n", number);
      else
        printf("%d is NOT a prime number.\n", number);
    }
  }
}
