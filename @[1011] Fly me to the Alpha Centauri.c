/*
그가 탑승하게 될 우주선은 Alpha Centauri라는 새로운 인류의 보금자리를 개척하기 위한 대규모 생활 유지 시스템을 탑재하고 있기 때문에, 
그 크기와 질량이 엄청난 이유로 최신기술력을 총 동원하여 개발한 공간이동 장치를 탑재하였다. 
하지만 이 공간이동 장치는 이동 거리를 급격하게 늘릴 경우 기계에 심각한 결함이 발생하는 단점이 있어서, 
이전 작동시기에 k광년을 이동하였을 때는 k-1 , k 혹은 k+1 광년만을 다시 이동할 수 있다. 
예를 들어, 이 장치를 처음 작동시킬 경우 -1 , 0 , 1 광년을 이론상 이동할 수 있으나 
사실상 음수 혹은 0 거리만큼의 이동은 의미가 없으므로 1 광년을 이동할 수 있으며, 그 다음에는 0 , 1 , 2 광년을 이동할 수 있는 것이다. 
( 여기서 다시 2광년을 이동한다면 다음 시기엔 1, 2, 3 광년을 이동할 수 있다. )
*/

// 메모리 초과
#include <stdio.h>
#include <stdlib.h>

int main() {
	int t, x, y, cnt = 1, two = 1, bb = 1, num = 1;
	scanf("%d", &t);

	while (t--) {
		int *d = { 0 };
		int cnt = 1, two = 1, bb = 1, num = 1;
		scanf("%d %d", &x, &y);
		long long dis = y - x;
		d = (int*)malloc(dis * sizeof(int));
		
		for (int i = 0; i < dis; i++) {
			if (bb > 0) {
				d[i] = cnt;
				bb--;
			}
			if (bb == 0) {
				if (two == 1) {
					bb = num;
					two++;
					cnt++;
				}
				else if (two == 2) {
					cnt++; 
					num++;
					bb = num;
					two--;
				}
			}
		}
		printf("%d\n", d[dis - 1]);
		free(d);
	}

}


