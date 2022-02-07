import csv
from pysat.solvers import Glucose3

try:
    k = input("please input k:")
    k = int(k)
except ValueError:
    print("not a number")

rows = []
rows1 = []
with open("test.csv",'r') as inFile:
    csvreader = csv.reader(inFile)
    count = 1
    for row in csvreader:
        if count > k:
            temp = row[0].split()
            rows1.append(temp)
        else:
            temp = row[0].split()
            rows.append(temp)
        count += 1
        

        

ans = []
#original values should be present
for i,temp in enumerate(rows):
    for j,temp1 in enumerate(temp):
        if int(temp1) != 0:
            ans.append([int(str(1)+str(i+1)+str(j+1)+(temp1))])

for i,temp in enumerate(rows1):
    for j,temp1 in enumerate(temp):
        if int(temp1) != 0:
            ans.append([int(str(2)+str(i+1)+str(j+1)+(temp1))])

#atleast one value and adding i and j value for position 
# 
 

b = []
for i in range(1,k*k+1):
    for j in range(1, k*k+1):
        for temp in range(1, k*k+1):
            b.append(int(str(1)+str(i)+str(j)+str(temp)))
        ans.append(b)
        b = []

b = []
for i in range(1,k*k+1):
    for j in range(1, k*k+1):
        for temp in range(1, k*k+1):
            b.append(int(str(2)+str(i)+str(j)+str(temp)))
        ans.append(b)
        b = []

#atmost one value
for i in range(1,k*k+1):
    for j in range(1,k*k+1):
        for p in range(1,k**2+1):
            for q in range(p+1, k**2+1):
                b = []
                b.append(-1*int(str(1)+str(i)+str(j)+str(p)))
                b.append(-1*int(str(1)+str(i)+str(j)+str(q)))
                ans.append(b)

for i in range(1,k*k+1):
    for j in range(1,k*k+1):
        for p in range(1,k**2+1):
            for q in range(p+1, k**2+1):
                b = []
                b.append(-1*int(str(2)+str(i)+str(j)+str(p)))
                b.append(-1*int(str(2)+str(i)+str(j)+str(q)))
                ans.append(b)



#block clause
b = []
for temp in range(1,k*k+1):
    for i in range(1, k*k+1,k):
        for j in range(1,k*k+1,k):
            x = i
            while(x<i+k):
                y = j
                while(y<j+k):
                    
                    b.append(int(str(1)+str(x)+str(y)+str(temp)))
                    y += 1
                x +=1
            ans.append(b)
            b=[]

b = []
for temp in range(1,k*k+1):
    for i in range(1, k*k+1,k):
        for j in range(1,k*k+1,k):
            x = i
            while(x<i+k):
                y = j
                while(y<j+k):
                    
                    b.append(int(str(2)+str(x)+str(y)+str(temp)))
                    y += 1
                x +=1
            ans.append(b)
            b=[]


#clauses for showing all rows contain all value form 1-9

b = []
for i in range(1,k*k+1):
    for temp in range(1,k*k+1):
        for j in range(1,k*k+1):
            b.append(int(str(1)+str(i)+str(j)+str(temp)))
        ans.append(b)
        b=[]

b = []
for i in range(1,k*k+1):
    for temp in range(1,k*k+1):
        for j in range(1,k*k+1):
            b.append(int(str(2)+str(i)+str(j)+str(temp)))
        ans.append(b)
        b=[]



#clauses for showing all columns contain all value form 1-9
b = []
for j in range(1,k*k+1):
    for temp in range(1,k*k+1):
        for i in range(1,k*k+1):
            b.append(int(str(1)+str(i)+str(j)+str(temp)))
        ans.append(b)
        b=[]

b = []
for j in range(1,k*k+1):
    for temp in range(1,k*k+1):
        for i in range(1,k*k+1):
            b.append(int(str(2)+str(i)+str(j)+str(temp)))
        ans.append(b)
        b=[]

#pair should not have same value at same place

for i in range(1,k*k+1):
    for j in range(1, k*k+1):
        for temp in range(1,k*k+1):
            b=[]
            b.append(int(str(-1)+str(i)+str(j)+str(temp)))
            b.append(int(str(-2)+str(i)+str(j)+str(temp)))
            ans.append(b)
            
g = Glucose3()

for temp in ans:
    g.add_clause(temp)

print(g.solve())
answer =  g.get_model()

for temp in answer:
    if temp > 0:
        print(temp)