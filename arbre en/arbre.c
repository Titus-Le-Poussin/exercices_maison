#include <stdio.h>

int main()
{
    int LineNum;

    printf("how many line: \n");
    scanf("%d", &LineNum);


    if (LineNum < 0){
        printf("c'est trop petit");
        return 0;
    }
    if (LineNum > 30){
        printf("c'est trop grand");
        return 0;
    }

    for (int i = 1 ; i <= LineNum; i++) {

        for (int k = 1; k <= LineNum - i; k++){
            printf(" ");
            }



        for (int j = 2; j <= 2 * i; j++){
            printf("*");

            }
        
        printf("\n");
    }

        if (LineNum > 0){
            for (int l = 0; l < LineNum - 1; l++){
                printf(" ");
            }
            printf("||");
        }
    


    return 0;

    }
