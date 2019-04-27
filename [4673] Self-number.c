#include <stdio.h>

// 출력이 잘못됨. 수정 필요
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

// 다른 풀이 참고 후 새로 작성

#include <stdio.h>

int main(void) {
	int arr[10010] = {0,};
	int n, dn;

	for (int i = 1; i < 10000; i++) {
		n = i; // n은 d(n)을 계산하기 위해 사용
		dn = n; 
		while (n != 0) {
			dn += n % 10; // n에서 끝자리 수만 dn에 더함
			n /= 10; // n의 끝자리 수를 지움
		}
		if(dn <= 10000) arr[dn]++; // 배열에서 생성자가 아닌 수를 0에서 1로 만듦 
	}

	for (int i = 1; i < 10000; i++) {
		if (arr[i] == 0) printf("%d\n", i); // 배열에서 셀프넘버인 수만 출력
	}

}

