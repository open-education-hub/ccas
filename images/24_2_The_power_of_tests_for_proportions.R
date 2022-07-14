n=21
beta<-function(p){
  return(
    choose(n,0)*p^0*(1-p)^(n-0)+
      choose(n,1)*p^1*(1-p)^(n-1)+
      choose(n,8)*p^8*(1-p)^(n-8)+
      choose(n,9)*p^9*(1-p)^(n-9)
  )
}
pvals<-seq(0,1,0.01)
betavec<-beta(pvals)
plot(pvals,betavec,type='l',xlab="true proportion, p",ylab="power")
lines(c(0,1),c(0.05,0.05))