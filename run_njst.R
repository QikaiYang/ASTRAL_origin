#!/usr/local/R/3.5.1/bin/Rscript
args<-commandArgs(TRUE)
library("phybase")
#---------------------------------------------------------------------------------------------------
con <- file(args[1], "r")
line=readLines(con,n=1)
countline<-0
while(length(line) != 0)
{
    #print(line)
    line=readLines(con,n=1)
    countline<-(countline+1)
}
count_array<-seq(1,countline,by=1)

con<-file(args[1], "r")
line=readLines(con,n=1)
while(length(line) != 0)
{	    
    temp<-strsplit(as.character(line),",")
    if(substring(temp[[1]][1],3,3)==":")
    {
        count_array[as.numeric(substring(temp[[1]][1],2,2))]<-length(temp[[1]])
    }
    else
    {
	count_array[as.numeric(substring(temp[[1]][1],2,3))]<-length(temp[[1]])
    }
    line=readLines(con,n=1)
}
# print(count_array)
#----------------------------------------------------------------------------------------------------
# count_array is the holder that contains the relationships between species and taxas 
#----------------------------------------------------------------------------------------------------
taxaname<-"a1_1" 		# Generate from map(con)
spname<-"a1"             	# Generate from map(con)
for(i in 1:countline)
{
    if(i!=1)
    {
        spname<-append(spname, paste0("a",as.character(i)))
    }
    for(j in 1:count_array[i])
    {
	if((i!=1) || (j!=1))
	{
	    taxaname<-append(taxaname, paste0("a", paste0(as.character(i),"_",as.character(j))))
	}	
    }
}
nspecies<-length(spname)
ntaxa<-length(taxaname)
#length(taxaname)
#length(spname)
#----------------------------------------------------------------------------------------------------
species.structure<-matrix(0,nrow=nspecies,ncol=ntaxa)
count = 0
for(i in 1:nspecies)
{
    if(i==1)
    {
        species.structure[i,]<-append(rep(1,times=count_array[i]), rep(0,times=ntaxa-count_array[i]))
	count<-(count+count_array[i])
    }
    else if(i!=nspecies)
    {
	species.structure[i,]<-append(append(rep(0,times=count), rep(1,times=count_array[i])), rep(0,times=(ntaxa-count-count_array[i])))
	count<-(count+count_array[i])
    }
    else
    {
        species.structure[i,]<-append(rep(0,times=count), rep(1,times=(ntaxa-count)))	    
    }
}
#species.structure
#----------------------------------------------------------------------------------------------------
genetrees<-read.tree.string(args[2],format="phylip")
# population size, theta
genetree<-rep("",length(genetrees[[1]]))
# generate gene trees
for(i in 1:length(genetree))
{
    genetree[i]<-genetrees[[1]][i]
}
#print(spname)
#print(taxaname)
#print(species.structure)
#print(genetree)
#----------------------------------------------------------------------------------------------------
final_result<-sptree.njst(genetree, taxaname, spname, species.structure)

out_con<-file(args[3], "w")
write(sprintf(final_result,1),out_con,append=T)
close(out_con)
