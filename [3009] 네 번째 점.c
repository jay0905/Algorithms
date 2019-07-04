// 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

#include <stdio.h>

int main(void) {
	int x1, x2, x3, x4 = 0, y1, y2, y3, y4 = 0;
	
	scanf("%d %d", &x1, &y1);
	scanf("%d %d", &x2, &y2);
	scanf("%d %d", &x3, &y3);

	if (x1 == x2) {
		x4 = x3;
		if (y1 == y3) y4 = y2;
		else y4 = y1;
		
	}
	
	else {
		x4 = x1;
		if (y1 == y2) y4 = y3;
		else y4 = y2;
	}
	printf("%d %d", x4, y4);
}
