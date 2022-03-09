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
        print ("\nprocessing.....")
        file_ = open('nmap_output.txt', 'w+')
        subprocess.run([command, '-sS', target, '-oX', filename ], stdout=file_)
        print ("\ncompleted")
        file_.close()
        f = open(outputfilename, 'w+')
        subprocess.run(['xsltproc', filename,], stdout=f)
        f.close()
        print('Your HTML report', outputfilename, 'is ready the below location')
        print("\n====================================")
        subprocess.run(["pwd"])
        print('====================================')
        break

    elif choice == '2':
        print ("\nprocessing.....")
        file_ = open('nmap_output.txt', 'w+')
        subprocess.run([command, '-A', '-Pn', target, '-oX', filename ], stdout=file_)
        print ("\ncompleted")
        file_.close()
        f = open(outputfilename, 'w+')
        subprocess.run(['xsltproc', filename,], stdout=f)
        f.close()
        print('Your HTML report', outputfilename, 'is ready the below location')
        print("\n====================================")
        subprocess.run(["pwd"])
        print('====================================')
        break
