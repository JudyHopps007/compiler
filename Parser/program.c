#include <stdio.h>
#include <stdbool.h>

int addition(int a, int b){
int result = a + b;
return result;
}
int subtraction(int a, int b){
int result = a - b;
return result;
}
float multiplication(float a, float b){
int result = a * b;
return result;
}
float division(float a, float b){
int result = a / b;
return result;
}
char boolCheck(int a){
    char mychar;
   if(a == 1){
      mychar = 'T';
      return mychar;
   }
   else{
      mychar = 'F';
      return mychar;
    }
}

void main(){
bool state = true;
   int c = 3;
int d = 5;
float e = 6.0;
float f = 12.0;
float newResult1;
int newResult2;

int select = 3;
while (state){
       if(select == 1){
            newResult1 = division(f, e);
       }else if (select == 2){
            newResult1 = multiplication(f, e);
       }else if (select == 3){
            newResult2 = addition(c, d);
       }else{
            newResult2 = subtraction(c, d);
       }

}
}}
