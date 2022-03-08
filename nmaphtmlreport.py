import os
import sys
import subprocess
command = 'nmap'
target = input ("Enter target:")
filename = input("Enter file name:")
print ('processing.....')
file_ = open('nmap_output.txt', 'w+')
subprocess.run([command, '-A', '-Pn', target, '-oX', filename ], stdout=file_)
print ('completed')
file_.close()
f = open('nmap_output.html', 'w+')
subprocess.run(['xsltproc', filename,], stdout=f)
f.close()
