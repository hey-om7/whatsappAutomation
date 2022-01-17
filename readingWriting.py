def read(name:str):
    with open(name) as f:
        contents = f.read()
        f.close()
        return contents.split(", ")

def write(name:str,text:str):
    file1 = open(name,"w+")
    text=text.replace("'","")
    file1.write(text[1:-1])
    file1.close()

def saveNos(userList):
    set1=set(read("previousNumbers.txt"))
    set2=set(userList)
    if(len(set1)>1):
        set3=set1.union(set2)
    else:
        set3=set2
    write("previousNumbers.txt",str(set3))
