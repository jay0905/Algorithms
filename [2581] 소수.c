/*
자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 
이들 소수의 합은 620이고, 최솟값은 61이 된다.
*/

#include <stdio.h>

int main(void) {
	int m, n, i, j; 
	scanf("%d %d", &m, &n);
	int total = 0, min = n;
	
	for (i = m; i <= n; i++) {
		for (j = 2; j < i; j++) {
			if (i % j == 0) break;
		}
		if (i == j) {
			total += j;
			if (j < min) min = j;
		}
	}
		
	if (total == 0) printf("-1");
	else printf("%d\n%d", total, min);

}

// 반복문 잘못 써서 한참을 헤맸다. 헷갈리지 말자. 
