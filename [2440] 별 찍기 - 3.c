// 첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제

#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);
    
    for(int i = 0; i <= n; ++i){
        for(int j = 1; j <= n - i; ++j){
            printf("*");
        }
        printf("\n");
    }
    return 0;
}
    
