//계산기를 만들어보세요. 사용자가 1 을 누르면 +, 2 를 누르면 - 와 같은 방식으로 해서 만들면 됩니다. 
// 물론 이전의 계산 결과는 계속 누적되어야 하고, 지우기 기능도 있어야 합니다. 

// 초기화 순서 문제

#include <stdio.h>

int plus(int *a, int *b);
int minus(int *a, int *b);
int multiple(int *a, int *b);
int divide(int *a, int *b);
int reset(int *a, int *b);

int main(){
  int num1, cal, num2;
  printf("초기값을 입력하고 Enter를 누르시오.\n");
  scanf("%d", &num1);

  for(;;){
    printf("+면 1, -면 2, *면 3, /면 4, 숫자를 초기화하고 싶다면 0, 프로그램을 끝내고 싶다면 20000을 입력하시오.\n");
		scanf("%d", &cal);
    if(cal == 0){
      reset(&num1, &num2);
      printf("초기값을 다시 입력하시오.\n");
      scanf("%d\n", &num1);
    }
    else if(cal == 20000){
      break;
    }
    else{
      printf("계산할 값을 입력하시오.\n");
  		scanf("%d", &num2);
        if(cal == 1){
          printf("= %d\n", plus(&num1, &num2));
        }
        else if(cal == 2){
          printf("= %d\n", minus(&num1, &num2));
        }
        else if(cal == 3){
          printf("= %d\n", multiple(&num1, &num2));
        }
        else if(cal == 4){
          printf("= %d\n", divide(&num1, &num2));
        }
    }
  }
  printf("프로그램을 종료합니다.");
  return 0;
}



int plus(int *a, int *b){
  *a += *b;
  return *a;
}
int minus(int *a, int *b){
  *a -= *b;
  return *a;
}
int multiple(int *a, int *b){
  *a = *a * *b;
  return *a;
}
int divide(int *a, int *b){
  *a = *a / *b;
  return *a;
}
int reset(int *a, int *b){
  *a = 0;
  *b = 0;
}

// 출처: https://modoocode.com/28
