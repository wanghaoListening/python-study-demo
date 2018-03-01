import csv

csvFile = open("/home/wang/test.csv",'w+',newline='')
try:
    write = csv.writer(csvFile)
    write.writerow(('number', 'number plus 2', 'number times 2'))
    for i in range(10):
        write.writerow((i,i+2,i*2))
finally:
    csvFile.close()
