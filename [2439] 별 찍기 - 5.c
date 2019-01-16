// 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
// 하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    
    for(int i = n; i > 0; i--) {
			for(int k = i - 1; k > 0; k--) {
				printf(" ");
			}
			for(int j = 0; j < n - i + 1; j++) {
				printf("*");
			}
        printf("\n");
    }
	
	return 0;
}
