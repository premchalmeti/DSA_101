#include<stdio.h>
#define N 3


void print_mat(int mat[][N]) {
    for(int r=0; r<N; r++){
        for(int c=0; c<N; c++){
            printf("%2d ", mat[r][c]);
        }
        printf("\n");
    }
}

void rota_mat(int mat[][N]) {
    for(int rr=0; rr<(N/2); rr++){
        for(int cc=rr; cc<(N-rr-1); cc++){
            int aux = mat[rr][cc];

            mat[rr][cc] = mat[cc][N-rr-1];
            mat[cc][N-rr-1] = mat[N-rr-1][N-cc-1];
            mat[N-rr-1][N-cc-1] = mat[N-cc-1][rr];
            mat[N-cc-1][rr] = aux;
        }
    }
}


int main(){
    int mat[N][N] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    printf("Before rotation\n");
    print_mat(mat);

    rota_mat(mat);
    printf("After rotation\n");
    print_mat(mat);

    return 0;
}
