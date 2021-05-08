import subprocess
import os

print("Python Shell Created")
while 1:
    cmd = input(">>> ")
    if cmd == 'exit':
        break
    try:
        exec(cmd)
# execution is just for testing subprocess and os, not for any calculating purposes
    except:
        print("error")
    if cmd == 'subprocess':
        with open('output.txt', 'w') as f:
            p1 = subprocess.run(['ls', '-la'], stdout=f, text=1)

