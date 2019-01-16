#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>

#ifndef EXIT_FAILURE
 #define EXIT_FAILURE 1
#endif

#define abrt() return EXIT_FAILURE

int main(int argc, char *argv[])
{
 pid_t pgid, pid=0; int arg1;

 if (argc < 3) {
  fprintf(stderr,"Usage: %s pgid command args\n",argv[0]);
  abrt();
 }

 if(sscanf(argv[1],"%d",&arg1)!=1) {
  fprintf(stderr,"Usage: %s pgid command args\n",argv[0]);
  abrt();
 }
 pgid = arg1;

 if (setpgid(0,pgid)) {
  fprintf(stderr,"Error changing pgid\n");
  abrt();
 }

 if(execvp(argv[2],&argv[2])) {
  fprintf(stderr,"Error execvping\n");
  abrt();
 }

 return 0; /* Impossible */
}
