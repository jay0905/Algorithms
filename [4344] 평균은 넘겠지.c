/* 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 
이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.*/

#include <stdio.h>

int main() {
	int C;
	double portion[1000] = { 0, };

	scanf("%d", &C);

	for (int j = 0; j < C; j++) {
		int N;
		int score[1000] = { 0, };
		int sum = 0;
		double ave = .0;

		scanf("%d", &N);

		for (int i = 0; i < N; i++) {
			scanf("%d", &score[i]);
			sum += score[i];
		}

		ave = (double)sum / N;
		int count = 0;

		for (int i = 0; i < N; i++) {
			if (score[i] > ave) count++;
		}
		portion[j] = (double)count / N * 100;
	}

	for (int j = 0; j < C; j++) {
		printf("%.3lf%%\n", portion[j]);
	}

	return 0;
}
