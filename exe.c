#include <stdio.h>
#include <unistd.h>

int main()
{
	if (execlp("python", "python", "window.py", NULL) == -1)
		perror("Error Executing Command\n");
	return 0;
}
