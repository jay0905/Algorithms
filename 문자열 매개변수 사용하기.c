// 표준 입력으로 길이 30 이하의 성과 이름 문자열이 두 개 입력됩니다. 
// 다음 소스 코드를 완성하여 전체 이름이 출력되게 만드세요(성과 이름은 붙여서 출력).

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void printFullName(char *str1, char *str2) {
	printf("%s%s", str1, str2);
}

int main()
{
    char familyName[31];
    char givenName[31];

    scanf("%s %s", familyName, givenName);

    printFullName(familyName, givenName);

    return 0;
}
