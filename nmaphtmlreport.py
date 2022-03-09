import os
import sys
import subprocess
print("\n Welcome to Nmap automation. Which scan would you like to run?")
command = 'nmap'
target = input ("Enter target:")
filename = input("Enter file name:")
outputfilename = input("enter output filename with .html:")

choice = ''

while choice !='q':
    print("\n[1] Enter 1 to do TCP SYN SCAN.")
    print("\n[2] Enter 2 to do -A SCAN.")
    print("\n[3] Enter q to quit.")
    choice = input("\nWhat would you like to do ")

    if choice =='1':
        print ('processing.....')
        file_ = open('nmap_output.txt', 'w+')
        subprocess.run([command, '-sS', target, '-oX', filename ], stdout=file_)
        print ('completed')
        file_.close()
        f = open(outputfilename, 'w+')
        subprocess.run(['xsltproc', filename,], stdout=f)
        f.close()
        print('Your HTML report', outputfilename, 'is ready the below location')
        A = subprocess.run(["pwd"])
        break

    elif choice == '2':
#else:
        print ('processing.....')
        file_ = open('nmap_output.txt', 'w+')
        subprocess.run([command, '-A', '-Pn', target, '-oX', filename ], stdout=file_)
        print ('completed')
        file_.close()
        f = open(outputfilename, 'w+')
        subprocess.run(['xsltproc', filename,], stdout=f)
        f.close()
        print('Your HTML report', outputfilename, 'is ready the below location')
        subprocess.run(["pwd"])
        break
#print('Your HTML report', outputfilename, 'is ready the below location')

