import random
import string
import os

progs = """
#include <stdio.h>

int main(void){
    printf("Hello World !");
    return 0;
}
"""

text = "The Linux kernel is a free and open-source,[5][6] monolithic, modular,[7] multitasking, Unix-like  operating system kernel.[8] \n It was conceived and created in 1991 by Linus Torvalds[9] for his i386-based PC, and it was soon adopted as the kernel for the GNU operating system,[10] \n which was created as a free replacement for UNIX.[11] \n Since then, it has spawned a large number of operating system distributions, commonly also called Linux." 


for i in range(5):
    path = os.path.join(".")
    cfile = ''.join(random.choice(string.ascii_letters) for _ in range(5))
    textfile   = ''.join(random.choice(string.ascii_letters) for _ in range(5))
    bakfile    = ''.join(random.choice(string.ascii_letters) for _ in range(5))

    cfile_path  = os.path.join(path, cfile + ".c")
    textfile_path    = os.path.join(path, textfile + ".txt")
    bakfile_path     = os.path.join(path, bakfile + ".bak")

    # creating python file
    file = open(cfile_path,"w")
    file.write(progs)
    file.write("\n")
    file.close()

    # creating text file
    file = open(textfile_path,"w")
    file.write(text)
    file.write("\n")
    file.close()

    # creating bak file
    file = open(bakfile_path,"w")
    file.write(progs)
    file.write("\n")
    file.close()
