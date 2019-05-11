#include <stdio.h>
#include <string.h>

int main(void) {
	char s[101];
	int cnt = 0;

	scanf("%s", s);

	int len = strlen(s);
	for (int i = 0; i < len; i++) {
		if (s[i] == 'c') {
			if (s[i + 1] == '=' || s[i + 1] == '-') {
				cnt++;
				i++;
			}
			else cnt++;
		}
		else if(s[i] == 'd'){
			if (s[i + 1] == 'z' && s[i + 2] == '=') {
				cnt++;
				i += 2;
			}
			else if(s[i + 1] == '-'){
				cnt++;
				i++;
			}
			else cnt++;
		}
		else if (s[i] == 'l') {
			if (s[i + 1] == 'j') {
				cnt++;
				i++;
			}
			else cnt++;
		}
		else if (s[i] == 'n') {
			if (s[i + 1] == 'j') {
				cnt++;
				i++;
			}
			else cnt++;
		}
		else if (s[i] == 's') {
			if (s[i + 1] == '=') {
				cnt++;
				i++;
			}
			else cnt++;
		}
		else if (s[i] == 'z') {
			if (s[i + 1] == '=') {
				cnt++;
				i++;
			}
			else cnt++;
		}
		else cnt++;
	}
	printf("%d", cnt);
}


// 코드가 길어 수정했는데 틀렸다고 나옴. 이유를 모르겠다.
#include <stdio.h>
#include <string.h>

int main(void) {
	char s[101];
	int cnt = 0;

	scanf("%s", s);

	int len = strlen(s);
	for (int i = 0; i < len; i++) {
		if (s[i] == 'c' || s[i] == 'l' || s[i] == 'n' || s[i] == 's' || s[i] == 'z') {
			if (s[i + 1] == '=' || s[i + 1] == '-' || s[i + 1] == 'j') {
				cnt++;
				i++;
			}
			else cnt++;
		}
		else if (s[i] == 'd') {
			if (s[i + 1] == 'z' && s[i + 2] == '=') {
				cnt++;
				i += 2;
			}
			else if (s[i + 1] == '-') {
				cnt++;
				i++;
			}
			else cnt++;
		}
		else cnt++;
	}
	printf("%d", cnt);
}

// 다시 개선
#include <stdio.h>
#include <string.h>

int main(void) {
	char s[101];
	int cnt = 0;

	scanf("%s", s);

	int len = strlen(s);
	for (int i = 0; i < len; i++) {
		if (s[i] == 'c' && (s[i + 1] == '=' || s[i + 1] == '-')) i++;
		else if (s[i] == 'd') {
			if (s[i + 1] == 'z' && s[i + 2] == '=') i += 2;
			else if (s[i + 1] == '-') i++;
		}
		else if ((s[i] == 'l' || s[i] == 'n') && s[i + 1] == 'j') i++;
		else if ((s[i] == 's' || s[i] == 'z') && s[i + 1] == '=') i++;
		cnt++;
	}
	printf("%d", cnt);
}

