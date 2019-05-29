#include <stdio.h>

int main(void) {
	int n, total = 0;
	long long num;

	scanf("%d", &n);
	scanf("%lld", &num);

	for (int i = n; i > 0; i--) {
		total += num % 10;
		num /= 10;
	}
	printf("%d", total);
}
