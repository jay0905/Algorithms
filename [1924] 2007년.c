// 오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.

#include <stdio.h>

int main(void) {
	int x, y;
	int day = 0;
	scanf("%d %d", &x, &y);


	for (int i = x - 1; i > 0; i--) {
		if (i == 1 || i == 3 || i == 5 || i == 7 || i == 8 || i == 10 || i == 12) {
			day += 31;
		}
		else if (i == 4 || i == 6 || i == 9 || i == 11) day += 30;
		else day += 28;
	}
	day += y;
	int n = day % 7;

	if (n == 0) printf("SUN");
	else if (n == 1) printf("MON");
	else if (n == 2) printf("TUE");
	else if (n == 3) printf("WED");
	else if (n == 4) printf("THU");
	else if (n == 5) printf("FRI");
	else if (n == 6) printf("SAT");
}


// 개선
// if문 조건 나열이 보기 좋지 않아 배열 형태로 바꿈.
// day라는 변수가 굳이 필요하지 않기에 y로 다 표현하기로.
#include <stdio.h>

int main(void) {
	int x, y;
	int month[] = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
	scanf("%d %d", &x, &y);

	for (int i = x - 1; i > 0; i--) {
		y += month[i];
	}
	int n = y % 7;

	if (n == 0) printf("SUN");
	else if (n == 1) printf("MON");
	else if (n == 2) printf("TUE");
	else if (n == 3) printf("WED");
	else if (n == 4) printf("THU");
	else if (n == 5) printf("FRI");
	else if (n == 6) printf("SAT");
}
