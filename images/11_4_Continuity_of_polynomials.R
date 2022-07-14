x<-seq(-20,20,1)
a<--2
a2<-6
a3<-4
a4<- -0.1
b<- x*a + x^2*a2+ x^3*a3 + x^4*a4
plot(b, type="l",frame=FALSE, xlab="x", ylab="Y", main="Polynomial Function")