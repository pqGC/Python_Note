import csv

stu1 = ['男人', 20]
stu2 = ['女人', 15]
stu3 = ['未知', 30]

wirte_in = open('test.csv','a',newline='')

csv_write = csv.writer(wirte_in, dialect='excel', delimiter='\t')
"""
tab分隔符：\t
换行：\n
"""
li = list()
for i in range(5):
    li.append(stu3)
    lis = set(li)
csv_write.writerow(li)
print("已写入")
