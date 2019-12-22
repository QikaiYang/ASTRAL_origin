args<-commandArgs(TRUE)
con <- file("delete.txt", "r")
line=readLines(con,n=1)
countline<-0
while(length(line) != 0)
{
    print(line)
    line=readLines(con,n=1)
    countline<-(countline+1)
}
count_array<-seq(1,countline,by=1)

con<-file("delete.txt", "r")
line=readLines(con,n=1)
i<-1
while(length(line) != 0)
{	    
    temp<-strsplit(as.character(line),",")
    count_array[i]<-length(temp[[1]])
    line=readLines(con,n=1)
    i<-(i+1)
}
print(count_array)
