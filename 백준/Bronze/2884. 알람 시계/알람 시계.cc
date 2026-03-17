#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int main() {
	int hour, min;
	scanf("%d %d", &hour, &min);
	if (hour == 0)
		hour = 23;
	else
		hour--;

	min = (min + 60) - 45;
	if (min >= 60)
	{ hour++;
	if (hour == 24)
		hour = 0;
		min = min % 60;
	} 
	printf("%d %d", hour, min);
	return 0;
}

