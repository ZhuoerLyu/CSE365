
#include<stdio.h>
#include<stdlib.h>
int main(int argc, char* argv[])
{   
    int i;
    printf("%d\n",argc-1);
    for(i = argc; i > 1; i-- )
    {
        printf("%s ",argv[i-1]);
    }
    printf("\n");
    return 0;

}
