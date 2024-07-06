def up(data):
    name=str(input("Enter old name"))
    if name in data:
        b=str(input("Enter the updation"))
        pos=data.index(name)
        data[pos]=b
        print("updation is :",data) 
    else:
        print("Name not found")   
    