import dendropy
import argparse 

def locate(str):
    for i in range(len(str)):
        if(str[i]=="." or str[i]=="-" or str[i]=="_" or str[i]==" "):
            return i
    return None 

#if two strings are the same species 
def help(sp1,sp2):
    if(sp1[:locate(sp1)]==sp2[:locate(sp2)]):
        return 1
    else:
        return 0
#if two normal list have intersect
def judge(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if(help(list1[i],list2[j])==1):
                return 1
    return 0  

#solve some edge cases
def if_all_1(list):
    for i in range(len(list)):
        if list[i] == 0:
            return 0
    return 1

def standardize_tree(tree):
    to_tackle = dendropy.Tree.get(data = "[&U] " + tree, schema = "newick", rooting = "force-rooted")
    for node in to_tackle.preorder_node_iter():
        if (node.child_nodes() == []):
            node.taxon.label = node.taxon.label[:locate(node.taxon.label)]
        else:
            node.label = None
            node.taxon = None
    return to_tackle.as_string(schema="newick").replace("\n","")[5:]

#combine two super lists
def merge_super_list(list1,list2):
    final = []
    record1 = [0 for i in range(len(list1))]
    record2 = [0 for i in range(len(list2))]
    for i in range(len(list1)):
        for j in range(len(list2)):
            if(judge(list1[i],list2[j]) == 1):
                record1[i] = 1
                record2[j] = 1
    for i in range(len(list1)):
        for j in range(len(list2)):
            if(record1[i] == 0 and record2[j] == 0):
                final.append(list1[i]+list2[j])
    #edge case---------------------------------------------------
    if(if_all_1(record1)==1):
        for j in range(len(record2)):
            if(record2[j]==0):
                final.append(list2[j]) 
    if(if_all_1(record2)==1):
        for i in range(len(record1)):
            if(record1[i]==0):
                final.append(list1[i])
    #edge case---------------------------------------------------
    for i in range(len(record1)):
        if(record1[i]==1):
            final.append(list1[i])
    for j in range(len(record2)):
        if(record2[j]==1):
            final.append(list2[j])
    #print(record1)
    #print(record2)
    return final

#transfer list to string
def list_2_string(list):
    store = list.copy()
    for i in range(len(store)):
        store[i] = ",".join(store[i])
    return ";".join(store)

parser = argparse.ArgumentParser()
parser.add_argument("Tree", type=str, help="Input Fasta File Name")
args = parser.parse_args()

final_result = ""
f = open(args.Tree,'r')
for line in f.readlines():
#-----------------------------------------------------------------------------------------------
    temp = (line.replace("\n",""))
    tree = dendropy.Tree.get(data = "[&R] " + temp, schema = "newick", rooting = "force-rooted")
    tree.reroot_at_midpoint(update_bipartitions=False)
    for node in tree.postorder_node_iter():
        if node.taxon == None:
            result = []
            children = [n.taxon.label for n in node.child_nodes()]
            child1 = children[0].split(";")
            child2 = children[1].split(";")
            for i in range(len(child1)):
                child1[i] = child1[i].split(",")
            for i in range(len(child2)):
                child2[i] = child2[i].split(",")
            #----------------------------------------------------
            result = merge_super_list(child1,child2)
            #----------------------------------------------------
            node.taxon = dendropy.datamodel.taxonmodel.Taxon(label=list_2_string(result))
    for node in tree.postorder_node_iter():
        if node.child_nodes() != []:
            node.label = None
            node.taxon = None
    for i in range(len(result)):
        temp_tree = (tree.extract_tree_with_taxa_labels(labels=result[i])).as_string(schema="newick").replace("\n","")[5:]
        temp_tree = standardize_tree(temp_tree)
        final_result += temp_tree + "\n"
    #------------------------------------------------------------------------------------------------
#print(final_result)
f = open((args.Tree + ".tree"),'w')
f.write(final_result)
f.close()
