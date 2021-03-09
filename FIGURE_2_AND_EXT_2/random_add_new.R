

library(phytools)
for (p in c(1:100)){
	myTree = read.tree(paste("PRUNED_NH/pruned_10_",p,".new.nh",sep=""))
	myList = as.vector(read.table(paste("MISSING_LIST/missing_10_",p,".list",sep=""))$V1)
	for (i in c(1:10)){
		node<-sample(c(1:length(myTree$tip), 2:myTree$Nnode+length(myTree$tip)),size=1)
		myTree<-bind.tip(myTree,myList[i],where=node)
		print(i)
	}
	write.tree(myTree,file=paste("RANDOM_ADD/randomly_add_",p,".nh",sep=""))
}


