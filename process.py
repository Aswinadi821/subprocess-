import subprocess

cmd ="program1.c"

subprocess.call(['gcc',cmd])
subprocess.call('./a.out')
