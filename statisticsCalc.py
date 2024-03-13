import math
from tabulate import tabulate
# 38 70 49 47 60 48 72 48 64 58 58 72 39 50 61 43 45 59 71 49 49 75 40 51 64 44 63 55 49 62 50 77 41 53 67 49 49 66 62 55 67 36 43 55 53 53 67 70 51 50
# 17 16 14 20 19 17 14 13 17 14 15 12 10 14 17 20 23 21 14 20 16 15 13 19 20 17 14 13 18 19 10 14 12 12 19 21 18 14 19 22

# Estadistica 
# 1. 60 94 75 82 72 57 92 75 85 77 91 72 85 64 78 75 62 49 70 94 72 84 55 90 88 81 64 91 79 66 68 67 74 45 76 73 68 85 73 83 85 71 87 57 82 78 68 70 71 78 69 98 65 61 83 84 69 77 81 87 79 64 72 55 76 68 93 56 67 71 83 72 82 78 62 82 49 63 73 89 78 81 93 72 76 73 90 76
# 2. 10 13 22 26 16 23 35 53 17 32 41 35 24 23 27 16 20 60 48 43 52 31 17 20 33 18 23 8 24 15 26 46 30 19 22 13 22 14 21 39 28 43 37 15 20 11 25 9 15 21 21 25 34 10 23 29 28 18 17 24 16 26 7 12 28 20 36 16 14 18 16 57 31 34 28 42 19 26
# 3. 27 19 10 33 13 18 26 37 31 22 30 34 31 22 19 31 34 30 35 30 24 30 34 24 24 32 33 27 35 32 31 33 21 15 27 24 34 33 30 38 14 26 29 21 26 15 28 23 33 31 16 28 23 28 32 28 28 38 14 19 33 29 20 32
numbers = input("Enter data plot numbers: ").split(" ")
numbers = list(map(int, numbers))
numbers.sort()
def freq_table():
   
    print(f'Number of numbers: {len(numbers)}')

    is_float = False

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
    t=round((math.sqrt(len(numbers))))
    # t=round(10)
    T=round(R/round(math.sqrt(len(numbers))))
    # T=round(R/10)
    t+=1
    intv,f,fr,fp,F,x,Fr = [""]*t,[0]*t,[0]*t,[0]*t,[0]*t,[0]*t,[0]*t
    t-=1
    index=0
    for i in range(lowest, highest, T):
        for k in numbers:
            k=(int)(k)
            if i<=k<i+T:
                f[index]+=1
                fr[index]=round(f[index]/len(numbers), 2)
                fp[index]=round(fr[index]*100)
        x[index]=(i+(i+T))/2
        intv[index]="[" + str(i/10 if is_float else i) + "-" + str((i+T)/10 if is_float else i+T) + ")"
        index+=1
    for i in range(len(f)):
        if i==0:
            F[0] = f[0]
            Fr[0] = round(F[0]/len(numbers), 2)
        else:
            F[i] = F[i-1]+f[i]
            Fr[i]=round(F[i]/len(numbers), 2)
    table=["" if intv[i] == "" else [intv[i], x[i]/10 if is_float else x[i], f[i], fr[i], F[i], Fr[i], f'{fp[i]}%'] for i in range(t+1)]
    table.insert(0, ['Interval', 'x;', 'f', 'fr', 'F', 'Fr', '%'])
    print(tabulate(table))
    #WRITEING TO CSV
    # csv_content=tabulate(table, tablefmt="tsv")
    # text_file=open("output.csv","w")
    # text_file.write(csv_content)
    # text_file.close()
    ###
    mean = round(sum(list(map(lambda x: x/10, numbers)) if is_float else numbers)/len(numbers), 2)
    median = (numbers[len(numbers)//2]+numbers[round(len(numbers)/2)])/2 if len(numbers) % 2 == 1 else numbers[len(numbers)//2]
    mode = max(set(numbers), key=numbers.count)
    print(f'Mean: {mean}, Median: {median/10 if is_float else median}, Mode: {mode/10 if is_float else mode}')
    return t+1

# NON-GROUPED DATA
def non_grouped_deviation():
    median = sum(numbers)/len(numbers)
    deviation = 0
    for num in numbers:
        deviation+= abs(median-num)
    deviation /= len(numbers)
    print(f'Deviation is: {round(deviation, 2)}')
def grouped_deviation():
    intervals = freq_table()
    # print(intervals)
    # intervals = int(input("Enter number of intervals: "))
    median = sum([(i+i+(len(numbers)//intervals))/2 for i in range(min(numbers), max(numbers), len(numbers)//intervals)])/len(numbers)
    # print(median)
    deviation = 0
    for num in numbers:
        deviation+= abs(median-num) * numbers.count(num)
    deviation /= len(numbers)
    print(f'Deviation is: {round(deviation, 2)}')
grouped_deviation()