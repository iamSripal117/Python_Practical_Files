##Read the data from csv file and write in json file 
##without using object in json

##import csv
##import json
##with open('C:\\Users\\Sridhar Rakkireddy\\OneDrive\\Documents\\emps.txt',"r")as f:
##    r = csv.reader(f)
##    next(r)
##    data =[]
##    for row in r:
##        data.append({'Eid':row[0],'En':row[1],'Sal':row[2]})
##with open("C:\\Users\\Sridhar Rakkireddy\\OneDrive\\Documents\\emps.json",'w') as f:
##    json.dump(data,f,indent=4)





##Read the data from csv file and write in json file 
##with using "object" in json


import csv
import json
with open('C:\\Users\\Sridhar Rakkireddy\\OneDrive\\Documents\\emps.txt',"r")as f:
    r = csv.reader(f)
    next(r)
    data ={"EmpDetails":[]}
    for row in r:
        data["EmpDetails"].append({'Eid':row[0],'En':row[1],'Sal':row[2]})
with open("C:\\Users\\Sridhar Rakkireddy\\OneDrive\\Documents\\emps.json",'w') as f:
    json.dump(data,f,indent=4)
