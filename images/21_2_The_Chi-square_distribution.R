library(MASS)   # for truehist
y<-rnorm(1000)  # 1000 n(0,1)
mn<-mean(y)
vr<-var(y)
x<-y^2
truehist(x)

xvec<-seq(0,12,0.01)    # generate the x-axis
yvec<-dchisq(xvec, df=1)       # theoretical n(0,1) density
lines(xvec,yvec,lwd=2,col="black")