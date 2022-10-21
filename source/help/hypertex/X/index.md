External URL's under X
======================
```
Date: Sat, 16 Jul 94 12:49:47 MDT
From: tanmoy@qcd.lanl.gov (Tanmoy Bhattacharya)
To: ginsparg@qfwfq.lanl.gov
Subject: more things needed
```
The script for Mosaic is not really that good right now: and we should probably think a bit more, and probably should talk to the Mosaic guys as well. That is why I do not yet want to publish it. We can put it up as an example of how it can be done within the present framework itself: not as a way in which we think these should be done.

At the minimum we need Mosaic (and any other www client) to set two environmentvariables containing respectively: (1) its own pid, and (2) The URL of the document it is calling, and should accept by \`remote control' either (a) an absolute URL, OR (b) a relative URL and a BASE HREF.  
(Instead of using an environment variable for (2), it could instead put the URL into a file and name the file in the environment. \[Does mac have environment variables? It is easy to overflow IBM PC environment space\].)

* * *

Anyway, here is how the system on nqcd works. No portability issues had been considered when writing them: I have tried to express my concerns below.

1.  There is a c-program [newpg.c](newpg.c) which takes 2 or more parameters.
    1.  **if** the first parameter is non-zero, it sets its pgid to the first parameter, **else** it sets its pgid to its pid.
    2.  it replaces itself (without changing pid's) with the program named by its second parameter and passes the rest of the arguments to it.
    3.  Note that it requires ANSI C, the header to define pid\_t, and the routines setpgid (I haven't checked to see if it exists in SYSV) and execvp.
2.  The actual Mosaic is renamed Mosaic.binary
3.  [Mosaic](/source/help/hypertex/X/Mosaic) is a script that calls the c-program (newpg) which starts the actual Mosaic. (It also provides default values to a few environment variables: only WWWBROWSER is relevant to this project). It should work on all unices unchanged provided $0 gets correctly translated, and the paths are corrected.
4.  [callmosaic](/source/help/hypertex/X/callmosaic) takes two parameters and does the following:
    1.  Ignores the second parameter. See later.
    2.  It clears the PATH environment variable, and changes the MOSAIC environment variable, if present, to `/usr/local/bin/Mosaic`. (As a result it uses absolute paths for all system programs, bringing in system dependencies). It redirects standard output to standard error. (should it?)
    3.  gets its own pgid. (call it x) Doing this from shell is extremely machine dependent. (depends on exact format of ps output! On some machines like IBM Risc stations, may be next to impossible). Should be done with a two line C program instead.
    4.  checks process with PID x to see if it exists and its identification as returned by ps contains the string \`Mosaic'. If so, goes to step 6. (There may be differences between BSD and SYSV ps calls). Probably should also check the DISPLAY environment variable, but no sure way of doing that unless one call call a process which has group kmem permissions. (Unless pstat, which is such a process gives us a way of doing it: I do not know). A less than perfect way does exist with ps -e.
    5.  checks to see if `${HOME}/.mosaicpid` exists and is readable. If so, call the `pid` in it as `x` (probably crash if file not in right format), else go to step 6.
    6.  checks to see if process with PID `x` exists and its identification as returned by ps contains the string \`Mosaic'. If so goto step 6. (BSD and SYSV ps calls may differ). (Note that it does not check to see if the DISPLAY is the same! See point 2)
    7.  Start a Mosaic passing it the first parameter; and exit when that exits. (should probably \`exec' the Mosaic instead. Should it also try a ps -x and check for an unique Mosaic on this display before it starts a new one? See point 2 about display). (The redirection of standard output to standard error stays!) (What happens if the parameter contains backquotes? Haven't checked!)
    8.  Creates `/tmp/Mosaic.x` (`x` being the aforementioned pid) and writes two lines into it (probably crashes if it cannot): the first being \`goto' and the second contains whatever came in as the first parameter. Then it signals USR1 to x, and exits. (probably should write the second parameter as a third line.) (What happens if the parameter contains backquotes? Haven't checked!)
    9.  Note that the second parameter is always ignored. (It is supposed to be the BASE HREF of the document which is calling callmosaic).