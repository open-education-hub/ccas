dat<-read.table("http://tutor-web.net/math/math612.1/lecture70/set115.dat", header=T)
mat<-dat$kt
barplot(table(mat), xlab="Maturity stage", ylab="Frequency")