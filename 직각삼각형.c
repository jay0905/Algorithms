//for 연산자를 이용해서 직각삼각형 만들기
//1. 값을 입력받아 입력값만큼 줄 수를 가진 직각삼각형 출력
//2. 별 수는 2개씩 늘어남

#include <stdio.h>

int main() {
	int n;
	scanf("%d",&n);
	
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < i * 2 + 1; j++) {
			printf("*");
		}
		printf("\n");
	}
  return 0;
}
