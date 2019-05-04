#include <stdio.h>
#include <string.h>

int main(void) {
	int n = 1;
	char str[1000000];

	scanf("%[^\n]s", &str);

	for (int i = 0; i < strlen(str); i++) {
		if (str[i] == ' ') n++;
	}
	
	if (str[0] == ' ') n--;
	if (str[strlen(str) - 1] == ' ') n--; 

	printf("%d", n);
}
