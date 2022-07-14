library(MASS)   # for truehist
y1<-rnorm(1000,0,1)
x1<-y1^2
var(x1)
y2<-rnorm(1000,0,1)
x2<-y2^2
var(x2)

X<-x1+x2
truehist(X)

xvec<-seq(0,200,0.01)    # generate the x-axis
yvec<-dchisq(xvec, df=1)       # theoretical n(0,1) density
lines(xvec,yvec,lwd=2,col="red")