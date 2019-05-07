// 시간 초과 나옴
#include <stdio.h>
#include <string.h>

int main(void) {
	char s[1000000];
	int atoz[26] = { 0 };

	scanf("%s", s);

	for (int i = 0; i < strlen(s); i++) {
		if (s[i] >= 97) atoz[s[i] - 97]++;
		else atoz[s[i] - 65]++;
	}

	int max[3] = {atoz[0], 0, 0};

	for (int i = 1; i < 26; i++) {
		if (atoz[i] == max[0]) max[2]++;
		else {
			if (atoz[i] > max[0]) {
				max[0] = atoz[i];
				max[1] = i;
				max[2] = 0;
			}
		}
	}

	if (max[2] > 0) printf("?");
	else printf("%c", max[1] + 65);

}
