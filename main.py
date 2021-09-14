import csv
import pandas as pd
file1="stars.csv"
file2="stars2.csv"
data1=[]
data2=[]
with open(file1,"r",encoding="utf8") as f:
    csv_reader=csv.reader(f)
    for i in csv_reader:
        data1.append(i)

with open(file2,"r",encoding="utf8") as f:
    csv_reader=csv.reader(f)
    for i in csv_reader:
        data2.append(i)
h1=data1[0]
p_data1=data1[1:]
h2=data2[0]
p_data2=data2[1:]
h=h1+h2
star_data=[]
for i in p_data1:
    star_data.append(i)
for j in p_data2:
    star_data.append(j)    

with open("totalstar.csv","w",encoding="utf8") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(h)
    csvwriter.writerows(star_data)