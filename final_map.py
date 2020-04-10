import numpy as np
import argparse

def findd(strr):
    for i in range(len(strr)):
        if strr[i] == "-":
            return i

parser = argparse.ArgumentParser()
parser.add_argument("map", type=str, help="Map File")     #input map file
parser.add_argument("alignment", type=str, help="Alignment File")     #input alignment file
args = parser.parse_args()

temp = ""
newfile = args.alignment + ".mapped"
final_strr = ""
dict = {}

flag = 1
for line in open(args.map,'r'):
    if(line!="\n"):
        if(flag == 1):
            tmp = line.replace("\n","")
            flag = 0
        else:
            dict[tmp] = line.replace("\n","")
            flag = 1

final_strr = ""
tmp = ""
unalign_strr = ""
maxx = 0
############get max########################
for line in open(args.alignment,'r'):
    if (line[0] == '@'):
        key_strr = line.split(" ")
        key_strr.pop(0)
        end = len(key_strr)-1
        print((1 + int((key_strr[end])[findd(key_strr[end])+1:len(key_strr[end])])))
        if((1 + int((key_strr[end])[findd(key_strr[end])+1:len(key_strr[end])])) > maxx):
            maxx = (1 + int((key_strr[end])[findd(key_strr[end])+1:len(key_strr[end])]))

###########################################
print(maxx)
for line in open(args.alignment,'r'):
    if (line[0] == '>'):
        if(tmp!=""):
            final_strr += tmp + "\n"
        tmp = ">" + dict[(line.replace(">","")).replace("\n","")] + "\n"
    elif (line[0] != '@'):
        unalign_strr = line.replace("\n","")
    else: #transfer stuff after @
        key_strr = line.split(" ")
        key_strr.pop(0)
        end = len(key_strr)-1
        real_strr = ["-" for i in range(maxx)]
        array = set(range(0, maxx))
        for j in range(len(key_strr)):
            array -= set(range(int((key_strr[j])[0:findd(key_strr[j])]), \
                        1 + int((key_strr[j])[findd(key_strr[j])+1:len(key_strr[j])])))
        i = 0
        index = 0
        #print(int((key_strr[end])[findd(key_strr[end])+1:len(key_strr[end])])+1)
        print(tmp)
        for index in list(array):
            real_strr[index] = unalign_strr[i]
            i += 1
        print(maxx)
        print(len("".join(real_strr)))
        assert(("".join(real_strr)).replace("-","") == unalign_strr)
        #print(("".join(real_strr)).replace("-",""))
        #print(unalign_strr)
        #print("----------------------")
        assert(maxx == len("".join(real_strr)))
        tmp += "".join(real_strr)
        #print(len(tmp))

final_strr += tmp + "\n"

f = open(newfile,'w')
f.write(final_strr)
f.close()
