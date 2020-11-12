import math
import csv

with open('Std.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)
data=file_data[0]
print(len(data))
def mean(data):
    n = len(data)
    total =0 
    for x in data: 
        total += x 
    mean = total / n 
    return mean


squaredList=[]

for number in data:
    a=int(number)-mean(data)
    a=a**2
    squaredList.append(a)
    
sum=0

for i in squaredList:
    sum=sum+i

result=sum/len(data)-1

std=math.sqrt(result)

print(std)