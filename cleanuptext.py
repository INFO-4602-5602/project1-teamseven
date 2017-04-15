import csv
with open("ZayoHackathonData_Accounts.csv", "rU") as csvfile:
    reader1 = csv.reader(csvfile)
    writerList = []
    for row in reader1:
        L=[]
        for obj in row:
            if(obj!=""):
                obj=obj.strip()
                if(obj[0] == '$'):
                    obj = obj[1:]
                    if(obj=='-'):
                        obj = 0
                    else:
                        obj=obj.replace(',','')
                        obj=(obj.split('.'))[0]
            L.append(obj)
        if('0' not in L):
                writerList.append(L)

with open("ZayoHackathonData_Accounts_cleanup.csv","wB") as writercsvfile:
    spamwriter = csv.writer(writercsvfile,delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for writer in writerList:
        stringchar = ",".join(map(str, writer))
        #print(stringchar)
        stringchar=stringchar.replace(' ','')
        spamwriter.writerow(stringchar)
