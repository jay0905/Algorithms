#include <stdio.h>

int main(void) {
	int N, temp;
	scanf("%d", &N);
	int sort[1000];

	for (int i = 0; i < N; i++) {
		int num;
		scanf("%d", &num);
		sort[i] = num;
	}

	for (int i = 0; i < N; i++) {
		for (int j = i + 1; j < N; j++) {
			if (sort[i] > sort[j]) {
				temp = sort[i];
				sort[i] = sort[j];
				sort[j] = temp;
			}
		}
	}

	for (int i = 0; i < N; i++) {
		printf("%d\n", sort[i]);
	}
}
