/*
우리나라 고유의 윷놀이는 네 개의 윷짝을 던져서 배(0)와 등(1)이 나오는 숫자를 세어 도, 개, 걸, 윷, 모를 결정한다. 
네 개 윷짝을 던져서 나온 각 윷짝의 배 혹은 등 정보가 주어질 때 도(배 한 개, 등 세 개), 개(배 두 개, 등 두 개), 걸(배 세 개, 등 한 개), 윷(배 네 개), 모(등 네 개) 중 어떤 것인지를 결정하는 프로그램을 작성하라.
*/

#include <stdio.h>

int main(void) {
	int a[4];

	for (int j = 3; j > 0; j--) {
		int num = 0;
		scanf("%d %d %d %d", &a[0], &a[1], &a[2], &a[3]);

		for (int i = 0; i < 4; i++) {
			if (a[i] == 1) num++;
		}

		switch (num) {
		case 0:
			printf("D\n");
			break;
		case 1:
			printf("C\n");
			break;
		case 2:
			printf("B\n");
			break;
		case 3:
			printf("A\n");
			break;
		case 4:
			printf("E\n");
			break;
		}
		
	}
}
