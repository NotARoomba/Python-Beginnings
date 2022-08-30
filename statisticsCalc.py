import math
from tabulate import tabulate
# 38 70 49 47 60 48 72 48 64 58 58 72 39 50 61 43 45 59 71 49 49 75 40 51 64 44 63 55 49 62 50 77 41 53 67 49 49 66 62 55 67 36 43 55 53 53 67 70 51 50
numbers = input("Enter data plot numbers: ").split(" ")

highest= (int)(numbers[0])
lowest = (int)(numbers[0])
R=0
T=0
for i in numbers:
    i=(int)(i)
    if i>highest:
        highest=i
    if i<lowest:
        lowest=i 
R=highest-lowest
t=round(math.sqrt(len(numbers)))
T=round(R/round(math.sqrt(len(numbers))))
intv,f,fr,fp,F,x = [""]*t,[0]*t,[0]*t,[0]*t,[0]*t,[0]*t
index=0
for i in range(lowest, highest, T):
    for k in numbers:
        k=(int)(k)
        if i<=k<i+T:
            f[index]+=1
            fr[index]=round(f[index]/len(numbers), 2)
            fp[index]=round(fr[index]*100)
    x[index]=(i+(i+T))/2
    intv[index]="[" + str(i) + "-" + str(i+T) + ")"
    index+=1

for i in range(len(f)):
    if i==0:
        F[0] = f[0]
    else:
        F[i] = F[i-1]+f[i]
table=[[intv[i], f[i], fr[i], fp[i], F[i], x[i]] for i in range(T)]
table.insert(0, ['Interval', 'f', 'fr', 'fp', 'F', 'x;'])
print(tabulate(table))
