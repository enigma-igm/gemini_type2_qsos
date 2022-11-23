#test the apture used to mathc with Legacy survey

import random
import csv


with open('test.csv','w') as file:

    writer = csv.writer(file)
    writer.writerow(["name","ra","dec"])
    for i in range(0,1000):
        ra = random.uniform(10,100) #random coordinates in the ra dec range
        dec = random.uniform(-10,10)
        writer.writerow(['test%s'%i,ra,dec])



