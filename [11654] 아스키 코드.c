// 알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

// 아스키 코드로 출력하려면 형식 지정자로 %d를 사용하면 된다.
#include <stdio.h>
#include <string.h>

int main(void) {
	char input;
	scanf("%c", &input);

	printf("%d", input);
}
