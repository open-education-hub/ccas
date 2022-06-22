library(MASS)
n<-5          
mu<-1         
lambda<-1     
tvec<-NULL    
for(sim in 1:1000){ 
  x<-rexp(n,lambda)  
  xbar<-mean(x)      
  s<-sd(x)           
  t<-(xbar-mu)/(s/sqrt(n)) 
  tvec<-c(tvec,t)          
}                       
truehist(tvec) 	#truehist gives a better histogram 