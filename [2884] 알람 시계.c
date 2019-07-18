#include <stdio.h>

int main(void) {
	int h, m;
	scanf("%d %d", &h, &m);

	if (m >= 45) m -= 45;
	else if (h == 0) {
		h = 23;
		m = 60 - (45 - m);
	}
	else
	{
		h--;
		m = 60 - (45 - m);
	}

	printf("%d %d", h, m);
}
