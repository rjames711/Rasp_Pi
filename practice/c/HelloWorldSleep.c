#include<unistd.h>
#include<stdio.h>

int main(){
int x = 0;

do{
   printf("Hello\n");
   sleep(5);
}while(x++<100);
}
