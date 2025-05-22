#include <stdio.h>

int main() {
    int height;

    printf("Quelle est la hauteur du sapin ? 🎄\n");
    scanf("%d", &height);

    for (int LineNum = 1; LineNum <= height; LineNum++) {
        // Affichage du feuillage
        for (int j = 0; j < height - LineNum; j++) {
            printf(" ");
        }
        for (int k = 0; k < 2 * LineNum - 1; k++) {
            printf("*");
        }
        printf("\n");
    }

    // Affichage du tronc avec IF
    if (height > 0) {
        for (int j = 0; j < height - 1; j++) {
            printf(" ");
        }
        printf("||\n");
    }

    return 0;
}
