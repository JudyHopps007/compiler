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
                   }else if (select == 3){
            newResult2 = addition(c, d);
       }else{
            newResult2 = subtraction(c, d);
       }
       state = false;
}
return newResult2
}
