#include <stdio.h>
#include <unistd.h>
int main(){
//printf("Hello, World!\n");
write(2,"This is write", 13);
return 0;
}
