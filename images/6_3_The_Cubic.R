a<-1
b<--20
c<--30
d<-4

p<-function(x){
  yhat<- a*x^3+b*x^2+c*x+d
  return(yhat)
}

x<-seq(-15,30, .2)
y<-p(x)
plot(x,y, type="l")
grid()