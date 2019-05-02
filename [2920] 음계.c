/* 다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다. 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다. 
c는 1로, d는 2로, ..., C를 8로 바꾼다.

1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.

연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.*/

// array 비교하는 법을 잊어서 좀 헤맸음.
// da[8]로 설정했더니 런타임 에러가 났다. char array라 마지막에 null을 넣어줘야하므로 크기 설정 유의.

#include <stdio.h>
#include <string.h>

int main(void) {
	char da[9];

	for (int i = 0; i < 8; i++) {
		scanf("%s", &da[i]);
	}

	if (strcmp(da, "12345678") == 0) printf("ascending");
	else if (strcmp(da, "87654321") == 0) printf("descending");
	else printf("mixed");
}
