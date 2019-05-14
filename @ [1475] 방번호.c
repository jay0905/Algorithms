// 안풀린다...

#include <stdio.h>
#include <string.h>

int main(void) {
	char N[1000001];
	int set = 0;
	int num[11] = { 0 };
	scanf("%s", N);

	if ((N[0] - 48 != 6) && (N[0] - 48 != 9)) {
		set++;
	}
	num[N[0] - 48]++;

	int len = strlen(N);
	for (int i = 1; i < len; i++) {
		num[N[i] - 48]++;
		if ((N[i] - 48 == 6) || (N[i] - 48 == 9)) {
			if ((num[6] + num[9]) % 2 == 0) set++;
		}
		else {
			if(num[N[i] - 48] >= 1) set++;
		}
	}
	printf("%d", set);
}
