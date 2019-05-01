/* "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 
문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.

"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오. */
// 한 스트링의 점수를 내는 것까지 해결

#include <stdio.h>

int main(void) {
	int n;
	char arr[80];
	int score = 0;

	// scanf("%d", &n);
	scanf("%s", &arr);

	int i = 0;
	while(arr[i] != '\0'){
		if (arr[i] == 'O') {
			score++;
			for (int j = i; j > 0; j--) {
				if (arr[j - 1] == 'O') score++;
				else break;
			}
		}
		i++;
	}

	printf("%d", score); 

}
