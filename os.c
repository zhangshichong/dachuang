#include <unistd.h>
#include <signal.h>
#include <sys/param.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <utmp.h>

void init_daemon()
{
	int pid;
	int i;
	if (pid = fork()) exit(0);
	else if (pid < 0) exit(1);

	setsid();

	if(pid = fork()) exit(0);
	else if (pid < 0) exit(1);

	for (int i = 0; i != NOFILE; ++i)
		close(i);
	chdir("~/os");
	umask(0);
	return;
}
int main()
{
	FILE *fp;
	time_t t;
	init_daemon();
	int t1;
	struct timeval tv;
	int cnt = 0;
	while(1)
	{
		sleep(5);
		cnt++;
		struct utmp *u;
		if ((fp = fopen("log.txt", "w")) >= 0) {
			while((u = getutent())) {
				if (u->ut_type == USER_PROCESS)
					fprintf(fp, "%d %s %s\n", u->ut_type, u->ut_user, asctime(localtime(&u->ut_tv)));
			}
		//	time(&t);
		//	fprintf(fp, "record time %s\n", asctime(localtime(&t)));
			endutent();
			fclose(fp);
		}
		int pid;
		while(pid = fork());
		int j = 1;
		if (pid == 0) {
			execlp("python", "python", "window.py", NULL);

		}
	}
	return 0;
}
