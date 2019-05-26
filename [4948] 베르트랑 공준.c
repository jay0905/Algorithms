#include <stdio.h>

int main(void) {
	while (1) {
		int n, i, j, cnt = 0;
		scanf("%d", &n);
		
		for (i = n * 2; i > n; i--) {
			for (j = i - 1; j > 1; j--) {
				if (i % j == 0) break;
			}
			if (j == 1) cnt++;
		}

		printf("%d\n", cnt);
	}
}

// 이렇게 풀었더니 시간초과 떠서 에라토스테네스의 체로 바꿈

#include <stdio.h>

int n, i, j, arr[246913];

int main(void) {
	arr[0] = 1, arr[1] = 1;
	
	
	while (1) {
		int cnt = 0; // 초기화를  위해 따로 설정
		
		scanf("%d", &n);
		if (n == 0) break;


		for (i = 2; i <= n*2; i++) {
			for (j = i * 2; j <= n*2; j += i) {
				arr[j] = 1;
			}
		}

		for (i = n * 2; i > n; i--) {
			if (arr[i] == 0) cnt++;
		}

		printf("%d\n", cnt);
	}
	
}

/*
뼈대는 금방 세웠는데도 헤맸던 이유가 몇 가지 있다.
1. scanf에서 &을 안 쓰는 어이없는 실수를 저지름.
2. 배열 크기를 246912로 받음. n*2 개를 받아야하므로 1을 더해서 배열을 설정했어야했다.
3. 문제를 제대로 안 읽고 출력초과가 떠서 헤맴. 문제에서는 마지막에 0을 출력하라는 조건이 있었는데 내 마음대로 생략했다.

조급함에 가려 이런 실수를 하지 말자. 
*/
