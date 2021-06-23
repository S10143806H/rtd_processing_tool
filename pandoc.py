# test
import sys
import subprocess
import os
from os import listdir

os.chdir("docx")

filelist = os.listdir()
#print(filelist)

for i in filelist:
	front = i.split(".")
	subprocess.run(["pandoc","--extract-media","./"+front[0],"-f","docx","-t","rst",i,"-o",front[0]+".rst"])

