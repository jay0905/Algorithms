/*
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 
즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.
*/

// 배열 크기 때문에 계속 틀렸다고 뜨던 문제.
// s가 문자열이기 때문에 null이 들어가서 배열 크기를 21로 잡아준다
#include <stdio.h>
#include <string.h>

int main(void) {
	int t, r;
	char s[21];

	scanf("%d", &t);

	for (int i = 0; i < t; i++) {
		char p[168] = "";
		scanf("%d", &r);
		scanf("%s", s);
		for (int j = 0; j < strlen(s); j++) {
			for (int k = 0; k < r; k++) {
				p[r * j + k] = s[j];
			}
		} printf("%s\n", &p);
	}
}
}

// 다른 풀이
// p라는 새 배열을 반드시 설정해야되는지 알았는데 아니어서 다시 풀이
#include <stdio.h>

int main(void) {
	int t, r;
	char s[20];

	scanf("%d", &t);

	for (int i = t; i > 0; i--) {
		scanf("%d", &r);
		scanf(" %s", s);
		for (int j = 0; s[j] != '\0'; j++) {
			for (int k = 0; k < r; k++) {
				printf("%c", s[j]);
			}
		} printf("\n");
	}
}
