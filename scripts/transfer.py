import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_tree", type=str, help="Input Fasta File Name")
parser.add_argument("output_tree", type=str, help="Output file")
args = parser.parse_args()

f = open(args.input_tree,'r')
for line in f.readlines():
    temp_string = list(line)
    dic = {}
    while(i != len(temp_String)-2):
        if((temp_string[i-1]=="(" and temp_string[i+1]==":") or (temp_string[i-1] == "," and temp_string[i+1] == ":")):
            if(dic.__contains__(temp_string[i])):
                
            else:

