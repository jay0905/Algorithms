#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

void getRanking(int **arr, int numStudents, int numSubject);
void BubbleSort(int *arr, int subject);

int main(int argc, char **argv) {
	int i, j, input;
	int subject, students;
	int **arr;
	int length = sizeof(subject);

	printf("과목 수: ");
	scanf("%d", &subject);
	printf("학생 수: ");
	scanf("%d", &students);

	arr = (int**)malloc(sizeof(int*) * subject);

	for (i = 0; i < subject; i++) {
		arr[i] = (int*)malloc(sizeof(int) * students);
	}

	for (i = 0; i < students; i++) {
		printf("학생 %d의 성적", i + 1);
		for (j = 0; j < subject; j++) {
			printf("과목 %d의 성적: ", j + 1);
			scanf("%d", &input);

			arr[i][j] = input;
		}
	}

	getRanking(arr, students, subject);

	for (i = 0; i < students; i++) {
		free(arr[i]);
	}

	free(arr);

	return 0;
}

void getRanking(int **arr, int numStudents, int numSubject) {
	int i, j, sum;
	int *average;

	average = (int *)malloc(sizeof(int) * numSubject);

	for (i = 0; i < numStudents; i++) {
		sum = 0;
		for (j = 0; j < numSubject; j++) {
			sum += arr[i][j];
		}
		average[i] = sum / numSubject;
	}

	BubbleSort(average, numSubject);

	for (i = 0; i < numStudents; i++) {
		printf("%d위 : %d 점 \n", i + 1, average[i]);
	}
}

void BubbleSort(int *arr, int subject) {
	int i, j, temp;
	
	for (i = 0; i < subject - 1; i++) {
		for (j = 0; j < subject - 1; j++) {
			if (arr[j] < arr[j + 1]) {
					temp = arr[j];
					arr[j] = arr[j + 1];
					arr[j + 1] = temp;
			}
		}
		
	}

}
