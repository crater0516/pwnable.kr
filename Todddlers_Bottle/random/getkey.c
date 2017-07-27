// gcc -o getkey getkey.c

#include <stdio.h>
#include <stdlib.h>

int main () {
	unsigned int random = rand();
	unsigned int key = 0;
	key = 0xdeadbeef ^ random;

	printf("%u\n", key);
	return 0;
}
