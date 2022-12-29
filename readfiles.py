import csv


def readvalue(path):
    finalfile=[]
    
    with open(path) as file:
        reader = csv.reader(file)
        for row in reader:
            finalfile.append(row[0])
    
    return finalfile
    
    
def readlist(path):
    
    finalfile=[]
    
    with open(path) as file:
        reader = csv.reader(file)
        for row in reader:
            finalfile.append(row)
            
    return finalfile
    
def readmedia(path):
    
    finalfile = []
    
    with open(path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            finalfile.append({"type": row["type"], "source": row["source"]})
    return finalfile