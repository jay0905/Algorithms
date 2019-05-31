#include <stdio.h>
#include <string.h>

int main(void) {
	char n[100];
	int i;

	scanf("%s", &n);

	int len = strlen(n);
	for (i = 0; i < len; i++) {
		if ((i != 0) && (i % 10 == 0)) printf("\n");
		printf("%c", n[i]);
	}
}
