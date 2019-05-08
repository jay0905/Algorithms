/*
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
단, 대문자와 소문자를 구분하지 않는다.
*/

// 시간 초과 나왔던 이유
// for 문에서 i < strlen(s)로 i 범위를 지정했는데, 여기서 매 차례 계산을 하게 되어 문제가 생김
// int len = strlen(s)로 위에 선언해주어 문제 해결
#include <stdio.h>
#include <string.h>

int main(void) {
	char s[1000001]; // null 문자를 포함할 수 있게 1 더 크게 선언
	int atoz[26] = { 0 };

	scanf("%s", s);

	int len = strlen(s);
	for (int i = 0; i < len; i++) {
		if (s[i] >= 97) atoz[s[i] - 97]++;
		else atoz[s[i] - 65]++;
	}

	int max = atoz[0];
	int index = 0;
	int isSame = 0;

	for (int i = 1; i < 26; i++) {
		if (atoz[i] == max) isSame++;
		else {
			if (atoz[i] > max) {
				max = atoz[i];
				index = i;
				isSame = 0;
			}
		}
	}

	if (isSame > 0) printf("?");
	else printf("%c", index + 65);

}
