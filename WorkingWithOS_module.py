##1.WAP to check a whether a given file is existing or not if exists display the file data else display file doesn't exist?
##code

##import os.path
##import sys
##fn=input("Enter the file name:")
##if os.path.isfile(fn):
##    print("file exists")
##    f=open(fn,"r")
##else:
##    print("file doesn't exists")
##    sys.exit(0)
##d=f.read()
##print(d)
##f.close()
##print("Thank you")



##2.WAP to input a name and check whether it is a file or directory?
##code

##import os.path
##fd=input("Enter the name to check whether it is a file or directory:")
##if os.path.isfile(fd):
##    print("It is a file")
##else:
##    if os.path.isdir(fd):
##        print("Is a dir")
##    else:
##        print("Neither a dir nor file")



##3.WAP to input a filename check whether a given file is
##existing or not if exists display size of the file and also display the content of the file else doesn't exists?

##code

##import os.path
##
##fn=input("Enter the file name:")
##
##if os.path.exists(fn):
##    print("File exists")
##    st=os.stat(fn)
##    s=st.st_size
##    print("size of file:",s)
##    f=open(fn,"r")
##    d=f.read()
##    print(d)
##    f.close()
##else:
##    print("File is not existing")


















