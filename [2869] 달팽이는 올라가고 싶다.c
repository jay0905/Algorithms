/*
땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.

달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.

달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.
*/

#include <stdio.h>

int main(void) {
	int a, b, v;
	scanf("%d %d %d", &a, &b, &v);

	printf("%d", (v - b - 1) / (a - b) + 1);
}

/*
마지막 미끄러지는 높이는 계산되지 않으므로 미리 빼둠.
딱 나눠 떨어지지 않는 경우를 고려해 -1
*/
