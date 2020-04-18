#include<stdio.h>
#define size 1000


void print_mat(int arr[], int cols){
	for(int col=0; col<cols; col++){
		printf("%d ", arr[col]);
	}
	printf("\n");
}

int search(int arr[], int cols, int elem){
	for(int col=0; col<cols; col++){
		if(arr[col] == elem){
			return col;
		}
	}
	return -1;
}


int main(){
	int t, n, arr[size], x;

	scanf("%d", &t);

	while(t--){
		scanf("%d", &n);
		for(int c=0; c<n; c++){
			scanf("%d", &arr[c]);
		}

		scanf("%d", &x);

		printf("%d\n", search(arr, n, x));

		print_mat(arr, n);
	}

	return 0;
}
