#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>
#include <time.h>
#include <string.h>
#include <ctype.h>
#include<fcntl.h> //新加入头文件 added
#include<queue>
#include<string>
#define Length 1024 //added

typedef struct dir_point
{
    char *filename;
    struct dir_point *next;
}H,*HLink;
char copypath[1024];//记录路径
void filecopy(const char *filename)
{
    int fdw,fdr,len;
    char str[Length];
    strcat(copypath, "/");
		strcat(copypath, "target.txt");
    fdr=open(filename,O_RDONLY);
    printf("\nGet stat on %s\n", filename);
    if(fdr)
        len=read(fdr,str,Length);
    else
    {
        printf("read file error");
        exit(0);
    }
    fdw=open(copypath,O_CREAT|O_RDWR);
    write(fdw,str,len);
    close(fdr);
    close(fdw);
}



static int get_file_size_time(const char* filename)
{
struct stat statbuf;
   char cmpname[1024];//比较名
   strcpy(cmpname,copypath);
   strcat(cmpname, "/");
   strcat(cmpname, "source.txt");
  // HLink p;
   //p=(HLink)malloc(sizeof(H));
	if(stat(filename, &statbuf) == -1)
	{
		printf("Get stat on %s Error: %s\n", filename, strerror(errno));
		return -1;
	}
	if(S_ISDIR(statbuf.st_mode))
		{
		   // p=H->next;
		   // strcpy(p->filename,filename);
		   // H=p;
    }
    //return 1;
	if(S_ISREG(statbuf.st_mode))
		{
         printf("%ssize:%ldbytes\tmodifiedat%s",filename,statbuf.st_size,ctime(&statbuf.st_mtime));
        if(strcmp(filename,cmpname)==0)
        {
           filecopy(filename);
           printf("/n1/n");
        }
    }
	return 0;
}
int main(int argc, char **argv)
{
	DIR *dirp;
	struct dirent *direntp;
	int stats;
	char path[1024];
  queue<string> dir_file

   // HLink H;
	//H=(HLink)malloc(sizeof(H));

    //HLink head;
    //head=H;
	//strcpy(H->filename,argv[1]);
  //printf("************%s**************",H->filename);

	if(argc != 2)
	{
		printf("Usage:%s filename\n\a", argv[0]);
		exit(1);
	}
	/*if(((stats=get_file_size_time(argv[1])) == 0) || (stats == -1))
		exit(1);*/
   dir_file.push(argv[1]);
   while(!dir_file.empty())
 {
	if((dirp=opendir(dir_file.front().c_str()))==NULL)
	{
		printf("Open Directory %s Error: %s\n", argv[1], strerror(errno));
		exit(0);
	}
	while((direntp = readdir(dirp)) != NULL)
	{
		memset(path, 0, 1024);
		strcpy(path, argv[1]);
    strcpy(copypath,path);
		strcat(path, "/");
		strcat(path, direntp->d_name);
		/*if(get_file_size_time(path) == -1)
			break;*/
   struct stat statbuf;
   char cmpname[1024];//比较名
   strcpy(cmpname,copypath);
   strcat(cmpname, "/");
   strcat(cmpname, "source.txt");
  // HLink p;
   //p=(HLink)malloc(sizeof(H));
	if(stat(path, &statbuf) == -1)
	{
		printf("Get stat on %s Error: %s\n", filename, strerror(errno));
		return -1;
	}
	if(S_ISDIR(statbuf.st_mode))
		{
		   // p=H->next;
		   // strcpy(p->filename,filename);
		   // H=p;
       dir_file.push(path);
    }
    //return 1;
	if(S_ISREG(statbuf.st_mode))
		{
         printf("%ssize:%ldbytes\tmodifiedat%s",filename,statbuf.st_size,ctime(&statbuf.st_mtime));
        if(strcmp(filename,cmpname)==0)
        {
           filecopy(filename);
           printf("/n1/n");
        }
    } 
	}
	closedir(dirp);
  dir_file.pop();
	}
  exit(1);
	return 0;
}
