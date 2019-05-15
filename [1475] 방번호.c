/*
다솜이는 은진이의 옆집에 새로 이사왔다. 다솜이는 자기 방 번호를 예쁜 플라스틱 숫자로 문에 붙이려고 한다.

다솜이의 옆집에서는 플라스틱 숫자를 한 세트로 판다. 한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다. 
다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최솟값을 출력하시오. (6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)
*/

#include <stdio.h>
#include <string.h>

int main(void) {
	char N[1000001];
	int num[10] = { 0 }; 
	scanf("%s", &N);

	int len = strlen(N);
	for(int i = 0; i < len; i++){
		num[N[i] - 48]++;
	}

	if ((num[6] + num[9]) % 2 == 0) {
		num[6] = (num[6] + num[9]) / 2;
		num[9] = 0;
	}
	else if ((num[6] + num[9]) % 2 == 1) {
		num[6] = (num[6] + num[9]) / 2 + 1;
		num[9] = 0;
	}

	int max = num[0];
	for (int i = 1; i < 10; i++) {
		if (num[i] > max) max = num[i];
	}

	printf("%d", max);
}

// 개선
#include <stdio.h>
#include <string.h>

int main(void) {
	char N[1000001];
	int num[10] = { 0 }; 
	scanf("%s", &N);

	int len = strlen(N);
	for(int i = 0; i < len; i++){
		num[N[i] - '0']++;
	}

	num[6] = (num[6] + num[9] + 1) / 2; // 이렇게 표현하면 케이스를 나누지 않고도 처리할 수 있다
	num[9] = 0; // 9는 쓸모없으므로 0으로 만듦

	int max = num[0];
	for (int i = 1; i < 10; i++) {
		if (num[i] > max) max = num[i];
	}

	printf("%d", max);
}

