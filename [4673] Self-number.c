#include <stdio.h>

int main(void) {
	int saved[10000];
	int num;
	
	for (int i = 0; i < 10000; i++) {
		saved[i] = i;
	}
	
	for (int i = 1; i < 10000; i++) {
		if (i < 10) {
			num = i * 2;
		}
		else if (i >= 10 && i < 100) {
			num = i + (i / 10) + (i % 10);
		}
		else if (i >= 100 && i < 1000) {
			int hundreds = i / 100;
			int tens = (i / 10) % 10;
			int units = i % 10;
			num = i + hundreds + tens + units;
		}
		
		else if (i >= 1000 && i < 10000) {
			int thousands = i / 1000;
			int hundreds = (i / 100) % 10;
			int tens = (i / 10) % 10;
			int units = i % 10;
			num = i + thousands + hundreds + tens + units;
			if (num >= 10000) break;
		}
		while (num >= 10000 && i < 10000) {
			i++;
			saved[i] = 0;
		}
		saved[num] = 0;
	}

	for (int i = 0; i < 10000; i++) {
		if (saved[i] != 0) printf("%d\n", saved[i]);
	}

}
