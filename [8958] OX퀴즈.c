/* "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 
문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.

"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오. */

// 한 배열에서 점수를 내는 것까지 해결. 여러 배열을 받으려하자 삼중 반복문이 될 것 같아서 수정(아래)
#include <stdio.h>

int main(void) {
	int n;
	char OX[80];
	int score = 0;

	scanf("%d", &n);

	scanf("%s", &OX);


	int i = 0;
	while(OX[i] != '\0'){
		if (OX[i] == 'O') {
			score++;
			for (int j = i; j > 0; j--) {
				if (OX[j - 1] == 'O') score++;
				else break;
			}
		}
		i++;
	}

	printf("%d", score); 

}

// 수정 후
// arr 배열을 뒤로 훑으며 처리하던 것을 sum, score 변수를 통해 한번에 해결하도록 바꿈

#include <stdio.h>
#include <string.h>

int main(void) {
	int n;
	char OX[80];

	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		int sum = 0;
		int score = 0;
		scanf("%s", &OX);
		for (int j = 0; j < strlen(OX); j++) {
			if (OX[j] == 'O') {
				score++;
				sum += score;
			}
			else {
				score = 0;
			}
		}
		printf("%d\n", sum);
	}
}
