import re
import dendropy
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_tree", type=str, help="Input Fasta File Name")
parser.add_argument("output_map", type=str, help="Output File Name")
args = parser.parse_args()

record = [-1 for i in range(100000)] #use to record how many species in the input file that we need to map

f = open(args.input_tree,'r')
for line in f.readlines():
    temp_string = line
    temp_record = [-1 for i in range(100000)] # refresh temp_record
    for i in range(1,len(temp_string)-1): #record the number of species (and how many copies) 
        if((temp_string[i-1]=="(" and temp_string[i+1]==":") or (temp_string[i-1] == "," and temp_string[i+1] == ":")):
            #print(int(temp_string[i]))
            temp_record[int(temp_string[i])] += 1
    for i in range(len(temp_record)):
        if(temp_record[i] >= record[i]):
            record[i] = temp_record[i]

result = ""
for i in range(len(record)):
    if(record[i] != -1):
        count = record[i]
        result += str(i) + " : "
        for j in range(count+1):
            result += str(i) + "_" + str(j) + ", "
        result = result[0:len(result)-2]
        result += "\n"

f = open(args.output_map,'w')
f.write(result)
f.close()
