library(phytools)
setwd("/Users/Bryan/Desktop/COVID/MORE_TANGLEGRAMS")

t1 = read.newick("original-1.nh")
t2 = read.newick("usher-1.nh")
assoc<-cbind(t1$tip.label,t2$tip.label)
obj = cophylo(t1,t2,rotate=FALSE,link.lwd=0.0001)
write.table(x=assoc,file='t1_assoc_table.txt',sep='\t',row.names=FALSE,col.names=FALSE,quote=FALSE)

write.table(x=obj$trees[[1]]$edge,file="original-1.edges",sep="\t",row.names=TRUE,col.names=FALSE,quote=FALSE)
write.table(x=obj$trees[[2]]$edge,file="usher-1.edges",sep="\t",row.names=TRUE,col.names=FALSE,quote=FALSE)
write(x=t1$tip.label,file="original-1.tiplabels")
write(x=t2$tip.label,file="usher-1.tiplabels")


t1 = read.newick("original-2.nh")
t2 = read.newick("usher-2.nh")
assoc<-cbind(t1$tip.label,t2$tip.label)
obj = cophylo(t1,t2,rotate=FALSE,link.lwd=0.0001)
write.table(x=assoc,file='t2_assoc_table.txt',sep='\t',row.names=FALSE,col.names=FALSE,quote=FALSE)

write.table(x=obj$trees[[1]]$edge,file="original-2.edges",sep="\t",row.names=TRUE,col.names=FALSE,quote=FALSE)
write.table(x=obj$trees[[2]]$edge,file="usher-2.edges",sep="\t",row.names=TRUE,col.names=FALSE,quote=FALSE)
write(x=t1$tip.label,file="original-2.tiplabels")
write(x=t2$tip.label,file="usher-2.tiplabels")


t1 = read.newick("original-3.nh")
t2 = read.newick("usher-3.nh")
assoc<-cbind(t1$tip.label,t2$tip.label)
obj = cophylo(t1,t2,rotate=FALSE,link.lwd=0.0001)
write.table(x=assoc,file='t3_assoc_table.txt',sep='\t',row.names=FALSE,col.names=FALSE,quote=FALSE)

write.table(x=obj$trees[[1]]$edge,file="original-3.edges",sep="\t",row.names=TRUE,col.names=FALSE,quote=FALSE)
write.table(x=obj$trees[[2]]$edge,file="usher-3.edges",sep="\t",row.names=TRUE,col.names=FALSE,quote=FALSE)
write(x=t1$tip.label,file="original-3.tiplabels")
write(x=t2$tip.label,file="usher-3.tiplabels")


t1 = read.newick("original-4.nh")
t2 = read.newick("usher-4.nh")
assoc<-cbind(t1$tip.label,t2$tip.label)
obj = cophylo(t1,t2,rotate=FALSE,link.lwd=0.0001)
write.table(x=assoc,file='t4_assoc_table.txt',sep='\t',row.names=FALSE,col.names=FALSE,quote=FALSE)

write.table(x=obj$trees[[1]]$edge,file="original-4.edges",sep="\t",row.names=TRUE,col.names=FALSE,quote=FALSE)
write.table(x=obj$trees[[2]]$edge,file="usher-4.edges",sep="\t",row.names=TRUE,col.names=FALSE,quote=FALSE)
write(x=t1$tip.label,file="original-4.tiplabels")
write(x=t2$tip.label,file="usher-4.tiplabels")


t1 = read.newick("original-5.nh")
t2 = read.newick("usher-5.nh")
assoc<-cbind(t1$tip.label,t2$tip.label)
obj = cophylo(t1,t2,rotate=FALSE,link.lwd=0.0001)
write.table(x=assoc,file='t5_assoc_table.txt',sep='\t',row.names=FALSE,col.names=FALSE,quote=FALSE)

write.table(x=obj$trees[[1]]$edge,file="original-5.edges",sep="\t",row.names=TRUE,col.names=FALSE,quote=FALSE)
write.table(x=obj$trees[[2]]$edge,file="usher-5.edges",sep="\t",row.names=TRUE,col.names=FALSE,quote=FALSE)
write(x=t1$tip.label,file="original-5.tiplabels")
write(x=t2$tip.label,file="usher-5.tiplabels")




t1 = read.newick("original-6.nh")
t2 = read.newick("usher-6.nh")
assoc<-cbind(t1$tip.label,t2$tip.label)
obj = cophylo(t1,t2,rotate=FALSE,link.lwd=0.0001)
write.table(x=assoc,file='t6_assoc_table.txt',sep='\t',row.names=FALSE,col.names=FALSE,quote=FALSE)

write.table(x=obj$trees[[1]]$edge,file="original-6.edges",sep="\t",row.names=TRUE,col.names=FALSE,quote=FALSE)
write.table(x=obj$trees[[2]]$edge,file="usher-6.edges",sep="\t",row.names=TRUE,col.names=FALSE,quote=FALSE)
write(x=t1$tip.label,file="original-6.tiplabels")
write(x=t2$tip.label,file="usher-6.tiplabels")
