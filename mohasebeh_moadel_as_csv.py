#project moadel ha
#in barnameh listy az nomarat danesh amooz ha ra migirad va moadel anhara hesab mikonad va ....
import csv
from statistics import mean
from collections import OrderedDict

#/////////////////////////////////task1/////////////////////////////////////////////

def calculate_averages(input_file_name, output_file_name):
    averages = OrderedDict()
    with open(input_file_name) as csv_file:
        csvfile = csv.reader(csv_file)
        for row in csvfile:
            scores = []
            for i in range(1, len(row)):
                scores.append (float(row[i]))
            avg = mean(scores)
            averages [row[0]] = avg
            
    with open (output_file_name, 'w') as out:
        count = 0
        for person in averages:
            count += 1
            if count == 1:
                out.write(person+ ","+ str(averages[person]))
            else:
                out.write("\n"+ person+ "," + str(averages[person]))

#///////////////////////////task2//////////////////////////////////////////////////////////

def calculate_sorted_averages(input_file_name, output_file_name):
    averages = OrderedDict()
    with open(input_file_name) as csv_file:
        csvfile = csv.reader(csv_file)
        for row in csvfile:
            scores = []
            for i in range(1, len(row)):
                scores.append(float(row[i]))
            avg = mean(scores)
            averages[row[0]] = avg
    
    averages_ord = OrderedDict (sorted (averages.items(), key=lambda x:(x[1], x[0])))
  
    with open(output_file_name, 'w') as out:
        count = 0
        for person in averages_ord:
            count += 1
            if count == 1:
                out.write(person + ',' + str(averages_ord[person]))
            else:
                out.write('\n' + person + ',' + str(averages_ord[person]))

#/////////////////////////////////////task3/////////////////////////////////////////////////////////

def calculate_three_best(input_file_name, output_file_name):
    averages = OrderedDict()
    with open(input_file_name) as csv_file:
        csvfile = csv.reader(csv_file)
        for row in csvfile:
            scores = []
            for i in range(1, len(row)):
                scores.append(float(row[i]))
            avg = mean(scores)
            averages[row[0]] = avg

    
    averages_ord = OrderedDict (sorted (averages.items(), key=lambda x:(x[1], x[0]), reverse=True))

    with open(output_file_name, "w") as out:
        count1 = 0
        for person in averages_ord:
            count1 += 1
            if count1 == 1 and count1 <= 3:
                out.write(person + ',' + str(averages_ord[person]))
            elif count1 <= 3:
                out.write('\n' + person + ',' + str(averages_ord[person]))

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\tassk4\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def calculate_three_worst(input_file_name, output_file_name):
    averages = OrderedDict()
    with open(input_file_name) as csv_file:
        csvfile = csv.reader(csv_file)
        for row in csvfile:
            scores = []
            for i in range(1, len(row)):
                scores.append(float(row[i]))
            avg = mean(scores)
            averages[row[0]] = avg

    
    averages_ord = OrderedDict (sorted (averages.items(), key=lambda x:(x[1], x[0])))

    with open(output_file_name, "w") as out:
        count1 = 0
        for person in averages_ord:
            count1 += 1
            if count1 == 1 and count1 <= 3:
                out.write(str(averages_ord[person]))
            elif count1 <= 3:
                out.write('\n' + str(averages_ord[person]))

#//////////////////////////////task5////////////////////////////////////////

def calculate_average_of_averages(input_file_name, output_file_name):
    averages = []
    with open(input_file_name) as csv_file:
        csvfile = csv.reader(csv_file)
        for row in csvfile:
            scores = []
            for i in range(1, len(row)):
                scores.append (float(row[i]))
            avg = mean(scores)
            averages.append(avg)
        
    with open(output_file_name, "w") as out:
        out.write(str(mean(averages)))

#//////////////////////////////////main/////////////////////////////////////

input_file_name = 'C:/Users/Ahmad/tamrinhay_maktabkhooneh/mohasbeh_moadel.csv'

output_file_name =  'C:/Users/Ahmad/tamrinhay_maktabkhooneh/file_csv_khoroogi_mohasbeh_moadel.csv'

calculate_averages(input_file_name, output_file_name)
calculate_sorted_averages(input_file_name, output_file_name)
calculate_three_best(input_file_name, output_file_name)
calculate_three_worst(input_file_name, output_file_name)
calculate_average_of_averages(input_file_name, output_file_name)