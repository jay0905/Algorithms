/*
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, 
aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.
*/

#include <stdio.h>
#include <string.h>

int main(void) {
	int N;
	int count = 0; // 그룹 단어 개수

	scanf("%d", &N);
	
	for (int i = N; i > 0; i--) {
		int atoz[26] = { 0 }; // 그룹 단어 확인을 위해 알파벳 배열 선언
		char s[101] = "";

		scanf("%s", &s);
		count++; // 그룹 단어가 아닐 경우 --하기 위해 미리 ++
		atoz[s[0] - 'a']++; 

		int len = strlen(s);
		for (int j = 1; j < len; j++) {
			if (s[j - 1] != s[j]) atoz[s[j] - 'a']++; // 바로 앞 자리 알파벳과 다를 경우에만 그 자리 알파벳 숫자 ++
			if (atoz[s[j] - 'a'] >= 2) { // 알파벳 숫자가 2보다 클 경우 그룹 단어가 아니기 때문에 count--
				count--;
				break; // 그룹 단어가 아니면 더 할 필요 없기 때문에 break;
			}
		}
	}
	printf("%d", count); 
}
