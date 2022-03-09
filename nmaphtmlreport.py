import os
import sys
import subprocess
command = 'nmap'
target = input ("Enter target:")
filename = input("Enter file name:")
outputfilename = input("enter output filename with .html:")
print ('processing.....')
file_ = open('nmap_output.txt', 'w+')
subprocess.run([command, '-A', '-Pn', target, '-oX', filename ], stdout=file_)
print ('completed')
file_.close()
f = open(outputfilename, 'w+')
subprocess.run(['xsltproc', filename,], stdout=f)
f.close()
