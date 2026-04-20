##1.Creating a zip file by storing required files in it
##code

##from zipfile import *
##
##f=ZipFile("file.zip","w",ZIP_DEFLATED)
##f.write("C:\\hlooo.txt")
##f.write("C:\\emps.txt")
##f.close()          


##2.To view files that are stored in zipped folder?
##code

##from zipfile import *
##f=ZipFile("file.zip","r",ZIP_STORED)
##files=f.namelist()
##for file in files:
##    print(file)
##f.close()    


##3.To "extract all" files from zipped folder into another folder
##code

##from zipfile import *
##f=ZipFile("C:\\Users\\Sridhar Rakkireddy\\OneDrive\\Desktop\\Python Practical Files\\file.zip","r",ZIP_STORED)
##f.extractall("C:\\abc")
##f.close()


##4.to extract specific file from the zip file to another folder?
##code

from zipfile import *
f=ZipFile("C:\\Users\\Sridhar Rakkireddy\\OneDrive\\Desktop\\Python Practical Files\\file.zip","r",ZIP_STORED)
f.extract("hlooo.txt","C:\\abc")
f.close()
