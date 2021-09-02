list1=[["harry",2],["carry",4],["marry",5],["jarry",7],["cherry",3]]

#print(list1[0],list1[1])
#for item in list1:
    #print(item)

'''dict1=dict(list1)
print(dict1)

for item,toffee in dict1.items():
    print(item,toffee)'''

list=[3,5,8,6,4,5,77,88,44,66,int,float]

for item in list:
    if str(item).isnumeric() and item>6:
        print(item)